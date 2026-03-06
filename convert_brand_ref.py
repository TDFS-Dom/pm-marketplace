"""
Script chuyển đổi ảnh trong thư mục Brand-Ref thành file Markdown
sử dụng Amazon Bedrock Vision (Claude Sonnet).

Yêu cầu:
  - pip install boto3
  - AWS credentials đã cấu hình (aws configure)
  - Quyền truy cập Bedrock model claude trong region của bạn

Chạy:
  python convert_brand_ref.py
"""

import base64
import glob
import json
import os
import sys

import boto3

# --- Cấu hình ---
IMAGE_DIR = "Brand-Ref"
OUTPUT_FILE = "Brand-Ref.md"
MODEL_ID = "us.anthropic.claude-sonnet-4-20250514-v1:0"  # Inference profile
REGION = os.environ.get("AWS_REGION", "us-east-1")
# Workaround SSL cert issue với pyenv Python + OpenSSL 3.6
VERIFY_SSL = False

SYSTEM_PROMPT = """Bạn là chuyên gia phân tích brand guidelines và UI/UX.
Hãy mô tả chi tiết nội dung trong ảnh bằng tiếng Việt, bao gồm:
- Nội dung text/copy hiển thị (trích nguyên văn nếu có)
- Màu sắc, typography, layout
- UI components, patterns
- Brand elements (logo, tagline, tone)
- Bất kỳ thông tin nào hữu ích cho việc tái tạo hoặc tham khảo thiết kế

Trả về dạng Markdown có cấu trúc rõ ràng."""


def encode_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.standard_b64encode(f.read()).decode("utf-8")


def get_media_type(path: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    return {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "gif": "image/gif", "webp": "image/webp"}.get(ext.lstrip("."), "image/png")


def analyze_image(client, image_path: str) -> str:
    print(f"  Đang phân tích: {os.path.basename(image_path)} ...")
    b64 = encode_image(image_path)
    media_type = get_media_type(image_path)

    response = client.invoke_model(
        modelId=MODEL_ID,
        contentType="application/json",
        accept="application/json",
        body=json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 4096,
            "system": SYSTEM_PROMPT,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": media_type,
                                "data": b64,
                            },
                        },
                        {
                            "type": "text",
                            "text": "Phân tích chi tiết nội dung ảnh này.",
                        },
                    ],
                }
            ],
        }),
    )

    result = json.loads(response["body"].read())
    return result["content"][0]["text"]


def main():
    images = sorted(glob.glob(os.path.join(IMAGE_DIR, "*.png")))
    if not images:
        print(f"Không tìm thấy ảnh PNG trong {IMAGE_DIR}/")
        sys.exit(1)

    print(f"Tìm thấy {len(images)} ảnh. Bắt đầu phân tích với Bedrock ({MODEL_ID})...\n")

    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    client = boto3.client("bedrock-runtime", region_name=REGION, verify=VERIFY_SSL)
    sections = []

    for i, img_path in enumerate(images, 1):
        filename = os.path.basename(img_path)
        try:
            analysis = analyze_image(client, img_path)
            sections.append(f"## Ảnh {i}: {filename}\n\n{analysis}")
        except Exception as e:
            print(f"  ⚠ Lỗi khi phân tích {filename}: {e}")
            sections.append(f"## Ảnh {i}: {filename}\n\n> ⚠ Lỗi phân tích: {e}")

    # Ghi file markdown
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Brand Reference Analysis\n\n")
        f.write(f"Tự động tạo từ {len(images)} ảnh trong `{IMAGE_DIR}/` ")
        f.write(f"bằng Amazon Bedrock Vision ({MODEL_ID}).\n\n---\n\n")
        f.write("\n\n---\n\n".join(sections))
        f.write("\n")

    print(f"\n✅ Đã xuất: {OUTPUT_FILE} ({len(sections)} ảnh)")


if __name__ == "__main__":
    main()
