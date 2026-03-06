---
inclusion: manual
---

# Bedrock AWS — Hướng dẫn sử dụng trong workspace

## Cấu hình môi trường

- AWS credentials phải được cấu hình sẵn (`aws configure` hoặc env vars)
- Region mặc định: `us-east-1` (đổi qua biến `AWS_REGION`)
- Python >= 3.11, cài `boto3`: `pip install boto3`

## Lưu ý quan trọng khi gọi Bedrock

### 1. Dùng Inference Profile, KHÔNG dùng Model ID trực tiếp

Bedrock yêu cầu inference profile cho on-demand invocation. Không dùng model ID gốc.

```
❌ SAI:  anthropic.claude-sonnet-4-20250514-v1:0
✅ ĐÚNG: us.anthropic.claude-sonnet-4-20250514-v1:0
```

Các inference profile phổ biến:
| Model | Inference Profile ID |
|-------|---------------------|
| Claude Sonnet 4 | `us.anthropic.claude-sonnet-4-20250514-v1:0` |
| Claude Sonnet 4.6 | `us.anthropic.claude-sonnet-4-6` |
| Claude Opus 4.6 | `global.anthropic.claude-opus-4-6-v1` |
| Claude 3.5 Sonnet v2 | `us.anthropic.claude-3-5-sonnet-20241022-v2:0` |
| Claude 3.5 Haiku | `us.anthropic.claude-3-5-haiku-20241022-v1:0` |

Để list tất cả inference profiles:
```python
client = boto3.client('bedrock', region_name='us-east-1')
resp = client.list_inference_profiles()
for p in resp['inferenceProfileSummaries']:
    print(p['inferenceProfileId'], '-', p.get('inferenceProfileName',''))
```

### 2. SSL Certificate Issue (pyenv + OpenSSL 3.6)

Môi trường hiện tại gặp lỗi SSL khi gọi Bedrock:
```
ValueError: empty or no certificate, match_hostname needs a SSL socket or SSL context with either CERT_OPTIONAL or CERT_REQUIRED
```

Workaround (chỉ dùng cho dev/local):
```python
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
client = boto3.client('bedrock-runtime', region_name=REGION, verify=False)
```

### 3. API Format cho Claude trên Bedrock

```python
import json
response = client.invoke_model(
    modelId="us.anthropic.claude-sonnet-4-20250514-v1:0",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "system": "System prompt here",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": "<base64_encoded_image>"
                        }
                    },
                    {
                        "type": "text",
                        "text": "Mô tả ảnh này."
                    }
                ]
            }
        ]
    })
)
result = json.loads(response["body"].read())
text = result["content"][0]["text"]
```

## Script có sẵn trong workspace

### `convert_brand_ref.py`
- Chuyển đổi ảnh trong thư mục thành file Markdown bằng Bedrock Vision
- Cấu hình: `IMAGE_DIR`, `OUTPUT_FILE`, `MODEL_ID` ở đầu file
- Chạy: `python convert_brand_ref.py`

## Khi nào dùng Bedrock trong workflow

- Phân tích ảnh (brand ref, wireframe, screenshot) → dùng Vision API
- Tạo nội dung dài, phức tạp → dùng Claude qua Bedrock
- Batch processing nhiều ảnh/files → viết script Python + boto3
- Nếu chỉ cần phân tích 1-2 ảnh → kéo vào Kiro chat nhanh hơn
