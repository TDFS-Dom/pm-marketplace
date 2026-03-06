# EduCareer VN — Full Product Management Flow
## Nền tảng AI hỗ trợ học tập, giảng dạy & phát triển sự nghiệp cho người Việt

> Tài liệu này trình bày toàn bộ quy trình PM từ nghiên cứu thị trường → chiến lược sản phẩm → thực thi → go-to-market cho sản phẩm EduCareer VN — nền tảng kết hợp sức mạnh của NotebookLM (nghiên cứu AI), MagicSchool (AI cho giáo dục), và Career.io (AI cho sự nghiệp), được thiết kế riêng cho người Việt Nam.

---

## Mục lục

1. [Phân tích đối thủ cạnh tranh](#1-phân-tích-đối-thủ-cạnh-tranh)
2. [Ước tính quy mô thị trường (TAM/SAM/SOM)](#2-ước-tính-quy-mô-thị-trường)
3. [Phân khúc thị trường](#3-phân-khúc-thị-trường)
4. [User Personas](#4-user-personas)
5. [Value Proposition](#5-value-proposition)
6. [Lean Canvas](#6-lean-canvas)
7. [PRD — Product Requirements Document](#7-prd--product-requirements-document)
8. [User Stories](#8-user-stories)
9. [Customer Journey Map](#9-customer-journey-map)
10. [North Star Metric](#10-north-star-metric)
11. [GTM Strategy](#11-gtm-strategy)

---

## 1. Phân tích đối thủ cạnh tranh

### Tổng quan thị trường

Thị trường AI trong giáo dục và phát triển sự nghiệp tại Việt Nam đang bùng nổ:

- Thị trường EdTech VN đạt ~$1.1B (2025), dự kiến $3.2B vào 2034 (CAGR 12.31%)
- Thị trường AI trong giáo dục VN đạt $24M (2024), dự kiến $507.8M vào 2033 (CAGR 35.69%)
- 78% người dùng internet VN đã thử AI (2025)
- Chính phủ đẩy mạnh chuyển đổi số giáo dục, tích hợp AI vào trường học
- Dân số ~100 triệu, ~25 triệu sinh viên/học sinh, ~1.5 triệu giáo viên
- AI Hay (make-in-Vietnam) đã vượt Google Gemini và DeepSeek về số người dùng thực tế tại VN

Cường độ cạnh tranh: Trung bình-cao ở mảng EdTech truyền thống, nhưng thấp ở mảng AI all-in-one (học tập + giảng dạy + sự nghiệp).

### 5 Đối thủ trực tiếp

#### 1. NotebookLM (Google)

| Hạng mục | Chi tiết |
|----------|----------|
| Thành lập | 2023, Google (Mỹ) |
| Người dùng | Hàng triệu toàn cầu (Google Workspace core service) |
| Vị thế | Global leader về AI research assistant |
| Định vị | AI notebook grounded trong tài liệu người dùng |

**Thế mạnh cốt lõi:**
- Powered by Gemini 1.5 Pro — AI mạnh nhất của Google
- Grounded responses: trả lời chỉ dựa trên tài liệu user upload, giảm hallucination
- Audio Overviews: biến tài liệu thành podcast AI
- Hỗ trợ đa dạng nguồn: PDF, Google Docs, Slides, YouTube, URLs, audio
- Deep Research với citations chi tiết
- Tích hợp Google Workspace, enterprise-grade data protection

**Điểm yếu & Gaps:**
- Không hỗ trợ tiếng Việt tối ưu (audio overview chỉ tiếng Anh tốt)
- Không có tính năng cho giáo viên (lesson plan, rubric, IEP)
- Không có career development tools
- Không localize cho chương trình giáo dục VN
- Yêu cầu Google account, không phổ biến ở VN bằng Facebook

**Mô hình kinh doanh:** Miễn phí (NotebookLM), Plus plan cho enterprise

**Mối đe dọa cho EduCareer VN:** Cao về mặt AI research, nhưng thấp về localization và tính năng giáo dục/sự nghiệp VN

---

#### 2. MagicSchool AI

| Hạng mục | Chi tiết |
|----------|----------|
| Thành lập | 2023, MagicSchool Inc. (Mỹ) |
| Người dùng | >6 triệu giáo viên tại 160 quốc gia |
| Vị thế | #1 AI platform cho giáo dục K-12 toàn cầu |
| Định vị | Safe, district-aligned AI cho trường học |

**Thế mạnh cốt lõi:**
- 80+ AI tools cho giáo viên (lesson plans, quizzes, rubrics, IEPs, worksheets)
- 50+ student tools qua MagicStudent
- SOC 2 certified, FERPA/COPPA compliant
- Raina AI coach cho giáo viên
- Tích hợp Google Classroom, Canvas, Schoology
- Free-forever model cho cá nhân

**Điểm yếu & Gaps:**
- Không có tiếng Việt
- Không align với chương trình giáo dục VN (MOET curriculum)
- Không có tính năng career development
- Không có research/notebook features
- Phụ thuộc vào prompt quality
- Không có community/social features cho giáo viên VN

**Mô hình kinh doanh:** Freemium cá nhân, tiered pricing cho schools/districts

**Mối đe dọa cho EduCareer VN:** Trung bình — mạnh về features nhưng không localize cho VN

---

#### 3. Career.io (formerly Talent Inc.)

| Hạng mục | Chi tiết |
|----------|----------|
| Thành lập | Talent Inc., rebrand thành Career.io |
| Người dùng | Global user base, chủ yếu thị trường Anh ngữ |
| Vị thế | All-in-one AI career platform |
| Định vị | AI + human expertise cho mọi giai đoạn sự nghiệp |

**Thế mạnh cốt lõi:**
- Resume Builder với 30+ ATS-friendly templates
- Cover Letter Builder tự động từ resume
- AI Resume Optimizer match job descriptions
- Interview Prep với mock interviews
- Job Tracker và Career Pathways
- Expert coaching từ professional writers
- AI Headshots từ selfie

**Điểm yếu & Gaps:**
- Hoàn toàn tiếng Anh, không hỗ trợ tiếng Việt
- Templates không phù hợp thị trường tuyển dụng VN
- Không hiểu văn hóa CV/phỏng vấn VN
- Không có tính năng giáo dục hay research
- Giá cao cho thị trường VN
- Không tích hợp với các nền tảng tuyển dụng VN (TopCV, VietnamWorks)

**Mô hình kinh doanh:** Subscription-based, tiered pricing

**Mối đe dọa cho EduCareer VN:** Thấp tại VN — không localize, nhưng là benchmark tốt về career features

---

#### 4. Prep Edu (Việt Nam)

| Hạng mục | Chi tiết |
|----------|----------|
| Thành lập | Startup EdTech Việt Nam, expanding across Asia |
| Người dùng | Đang mở rộng nhanh tại VN và châu Á |
| Vị thế | AI-powered learning & testing platform VN |
| Định vị | Giải quyết thách thức học ngoại ngữ và luyện thi |

**Thế mạnh cốt lõi:**
- AI personalized learning cho tiếng Anh
- Luyện thi IELTS, TOEIC với AI
- Localize hoàn toàn cho VN
- Giá phù hợp thị trường VN
- Mobile-first approach

**Điểm yếu & Gaps:**
- Chỉ focus vào ngoại ngữ/luyện thi
- Không có tools cho giáo viên
- Không có career development
- Không có research/notebook features
- Phạm vi hẹp, không all-in-one

**Mô hình kinh doanh:** Freemium, subscription cho premium content

**Mối đe dọa cho EduCareer VN:** Trung bình — mạnh ở niche ngoại ngữ nhưng không cạnh tranh trực tiếp ở all-in-one

---

#### 5. Vuihoc.vn / Hocmai / Vietjack (Hệ sinh thái EdTech VN)

| Hạng mục | Chi tiết |
|----------|----------|
| Thành lập | Nhiều nền tảng EdTech VN lâu đời |
| Người dùng | Hàng triệu học sinh VN |
| Vị thế | Market leaders EdTech truyền thống VN |
| Định vị | Nền tảng học trực tuyến theo chương trình MOET |

**Thế mạnh cốt lõi:**
- Content align 100% với chương trình MOET
- Brand awareness cao tại VN
- Đội ngũ giáo viên VN chất lượng
- Giá rẻ, phù hợp đại chúng
- SEO mạnh, traffic organic lớn

**Điểm yếu & Gaps:**
- AI integration rất hạn chế hoặc không có
- Mô hình video bài giảng truyền thống, không interactive
- Không có tools cho giáo viên tạo content
- Không có career development
- UX/UI cũ, không hấp dẫn Gen Z
- Không có personalization AI

**Mô hình kinh doanh:** Freemium, subscription cho khóa học premium

**Mối đe dọa cho EduCareer VN:** Trung bình — user base lớn nhưng technology gap lớn, có thể partner thay vì cạnh tranh

---

### Ma trận cơ hội khác biệt hóa

| Yếu tố | NotebookLM | MagicSchool | Career.io | Prep Edu | Vuihoc/Hocmai | **EduCareer VN** |
|---------|------------|-------------|-----------|----------|---------------|-------------------|
| Tiếng Việt native | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| AI Research/Notebook | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Teacher Tools (80+) | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Career Development | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |
| MOET Curriculum | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Audio/Podcast AI | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| All-in-one platform | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| VN Job Market Integration | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

### Khuyến nghị định vị cạnh tranh

EduCareer VN nên định vị là **"nền tảng AI all-in-one đầu tiên cho người Việt — từ học tập, giảng dạy đến phát triển sự nghiệp"**. Không đối thủ nào kết hợp cả 3 trụ cột này với deep localization cho VN.

---

## 2. Ước tính quy mô thị trường

### Định nghĩa thị trường
- **Vấn đề**: Người Việt (sinh viên, giáo viên, người đi làm) thiếu nền tảng AI tích hợp bằng tiếng Việt để hỗ trợ học tập, giảng dạy và phát triển sự nghiệp
- **Phạm vi**: Việt Nam, người dùng 16-45 tuổi, sử dụng smartphone/máy tính

### TAM (Total Addressable Market)

**Top-down:**
- Thị trường EdTech VN: ~$1.1B (2025)
- Thị trường AI trong giáo dục VN: ~$24M (2024), dự kiến $507.8M (2033)
- Thị trường online education VN: ~$7.8B (2025)
- Phần AI-powered learning + teaching + career tools: ước tính ~5% thị trường EdTech
- **TAM ≈ $55M/năm (~1,375 tỷ VNĐ)**

**Bottom-up:**
- Sinh viên đại học/cao đẳng: ~2.5 triệu
- Giáo viên các cấp: ~1.5 triệu
- Người đi làm 22-35 tuổi cần career development: ~8 triệu
- Học sinh THPT: ~3 triệu
- Tổng addressable users: ~15 triệu
- ARPU (mix free + premium): ~$3.5/user/năm
- **TAM ≈ $52.5M/năm (~1,312 tỷ VNĐ)**

### SAM (Serviceable Addressable Market)

- Users có nhu cầu AI tools thực sự (không chỉ content truyền thống): ~40% → 6 triệu
- Có khả năng tiếp cận digital (smartphone + internet ổn định): ~85% → 5.1 triệu
- Sẵn sàng thử nền tảng mới: ~50% → 2.55 triệu
- **SAM ≈ $8.9M/năm (~222 tỷ VNĐ)** (~17% TAM)

### SOM (Serviceable Obtainable Market)

- Năm 1-3: Mục tiêu 5-10% SAM
- **SOM ≈ $450K-890K/năm (~11-22 tỷ VNĐ)**
- Tương đương ~130K-250K active users

### Bảng tổng hợp

| Metric | Ước tính hiện tại | Dự báo 3 năm |
|--------|-------------------|---------------|
| TAM | $54M (~1,350 tỷ VNĐ) | $120M (~3,000 tỷ VNĐ) |
| SAM | $8.9M (~222 tỷ VNĐ) | $25M (~625 tỷ VNĐ) |
| SOM | $670K (~17 tỷ VNĐ) | $4M (~100 tỷ VNĐ) |

### Growth Drivers

1. Chính phủ VN đẩy mạnh AI trong giáo dục (Quyết định 127/QĐ-TTg về AI)
2. CAGR 35.69% cho AI in education tại VN (2025-2033)
3. 78% người dùng internet VN đã thử AI — adoption barrier thấp
4. Xu hướng "upskilling" và "career change" tăng mạnh post-COVID
5. Chi phí AI inference giảm nhanh → margin cải thiện

### Giả định chính

1. Premium conversion rate ~5-8% (confidence: medium)
2. ARPU tăng khi thêm B2B/school licensing (confidence: high)
3. AI in education VN tiếp tục CAGR >30% (confidence: high)
4. Người dùng VN sẵn sàng trả phí cho AI tools chất lượng (confidence: medium — cần validate)

---

## 3. Phân khúc thị trường

### Segment 1: "Sinh viên & Học sinh" (35% thị trường)

- **Demographics**: 16-24 tuổi, học sinh THPT và sinh viên đại học
- **Quy mô**: ~5.5 triệu người
- **Thu nhập**: 0-5 triệu/tháng (phụ thuộc gia đình hoặc part-time)
- **JTBD**: "Khi tôi cần nghiên cứu tài liệu hoặc viết bài luận, tôi muốn có AI hiểu tiếng Việt giúp tôi tổng hợp, phân tích và viết nhanh hơn để đạt điểm cao mà không mất quá nhiều thời gian"
- **Pain points**:
  - Tài liệu học thuật bằng tiếng Anh khó hiểu
  - ChatGPT hallucinate khi hỏi về kiến thức chuyên ngành VN
  - Không biết cách viết CV/xin việc khi sắp ra trường
  - Thiếu công cụ tổng hợp tài liệu thông minh bằng tiếng Việt
- **Product fit**: Rất cao — cần AI research + career prep, price-sensitive nên cần free tier mạnh

### Segment 2: "Giáo viên & Giảng viên" (25% thị trường)

- **Demographics**: 25-55 tuổi, giáo viên các cấp và giảng viên đại học
- **Quy mô**: ~1.5 triệu người
- **Thu nhập**: 8-25 triệu/tháng
- **JTBD**: "Khi tôi cần soạn giáo án, đề thi, và tài liệu giảng dạy, tôi muốn có AI hiểu chương trình MOET giúp tôi tạo nội dung chất lượng trong vài phút thay vì hàng giờ"
- **Pain points**:
  - Soạn giáo án, đề thi tốn rất nhiều thời gian (5-10 giờ/tuần)
  - MagicSchool không hiểu chương trình VN
  - Thiếu công cụ tạo rubric, worksheet theo chuẩn MOET
  - Áp lực đổi mới phương pháp giảng dạy nhưng thiếu hỗ trợ
- **Product fit**: Rất cao — sẵn sàng trả phí nếu tiết kiệm >5 giờ/tuần, B2B potential qua trường học

### Segment 3: "Người đi làm cần upskill/career change" (30% thị trường)

- **Demographics**: 22-35 tuổi, nhân viên văn phòng, muốn thăng tiến hoặc đổi nghề
- **Quy mô**: ~8 triệu người
- **Thu nhập**: 8-30 triệu/tháng
- **JTBD**: "Khi tôi muốn thăng tiến hoặc chuyển nghề, tôi cần AI giúp tôi viết CV chuyên nghiệp, chuẩn bị phỏng vấn, và nghiên cứu ngành mới một cách hiệu quả"
- **Pain points**:
  - CV tiếng Việt không biết viết sao cho chuyên nghiệp
  - Không biết cách chuẩn bị phỏng vấn cho vị trí mới
  - Cần nghiên cứu ngành/công ty nhưng tốn thời gian
  - Career.io không hiểu thị trường tuyển dụng VN
- **Product fit**: Cao — sẵn sàng trả phí, cần career tools + research capabilities

### Segment 4: "Content Creator & Freelancer" (10% thị trường)

- **Demographics**: 20-35 tuổi, blogger, YouTuber, copywriter, freelance writer
- **Quy mô**: ~1 triệu người
- **Thu nhập**: 5-50 triệu/tháng (biến động)
- **JTBD**: "Khi tôi cần tạo content chất lượng nhanh, tôi muốn AI giúp tôi research, outline, và viết draft bằng tiếng Việt tự nhiên để tăng output mà không giảm chất lượng"
- **Pain points**:
  - AI viết tiếng Việt thường không tự nhiên, "máy móc"
  - Cần research nhiều nguồn nhưng tốn thời gian
  - Thiếu công cụ tổng hợp và biến tài liệu thành content
  - ChatGPT không cite sources, khó verify thông tin
- **Product fit**: Trung bình-cao — cần research + writing tools, sẵn sàng trả phí cho productivity

---

## 4. User Personas

### Persona 1: Hà — "Sinh viên năm cuối"

- **Tuổi**: 22, sinh viên năm 4 ngành Quản trị Kinh doanh, ĐH Kinh tế TP.HCM
- **Thu nhập**: 4 triệu/tháng (part-time marketing)
- **JTBD chính**: Hoàn thành luận văn tốt nghiệp và tìm được việc làm đầu tiên trong 6 tháng

**Top 3 Pain Points:**
1. Phải đọc 50+ tài liệu tham khảo (cả tiếng Anh lẫn tiếng Việt) cho luận văn — không biết bắt đầu từ đâu
2. Viết CV lần đầu, không biết format nào phù hợp thị trường VN, nộp TopCV nhưng không ai gọi
3. ChatGPT viết tiếng Việt "nghe như dịch máy", không dùng được cho luận văn

**Top 3 Desired Gains:**
1. Upload tài liệu → AI tổng hợp key findings, tạo literature review draft
2. CV builder hiểu thị trường VN, gợi ý keywords cho từng ngành
3. Mock interview bằng tiếng Việt, feedback cụ thể cho từng câu trả lời

**Unexpected Insight:** Hà dùng NotebookLM cho tài liệu tiếng Anh nhưng phải copy-paste sang ChatGPT để dịch và tóm tắt tiếng Việt — workflow rời rạc, mất 2x thời gian. Nếu có 1 tool làm cả 2 bằng tiếng Việt, Hà sẽ dùng ngay.

**Product Fit:** EduCareer VN cần: AI notebook tiếng Việt mạnh, CV builder cho thị trường VN, mock interview tiếng Việt. Hà sẽ dùng free tier và upgrade khi cần career features.

---

### Persona 2: Thầy Tuấn — "Giáo viên THPT"

- **Tuổi**: 35, giáo viên Toán THPT tại Đà Nẵng, 10 năm kinh nghiệm
- **Thu nhập**: 12 triệu/tháng (lương + dạy thêm)
- **JTBD chính**: Giảm thời gian soạn giáo án và đề thi từ 10 giờ/tuần xuống 3 giờ/tuần

**Top 3 Pain Points:**
1. Mỗi tuần mất 8-10 giờ soạn giáo án, đề thi, worksheet — thời gian này có thể dành cho học sinh
2. Chương trình mới (2018) yêu cầu đổi mới phương pháp nhưng thiếu tài liệu mẫu
3. Đã thử MagicSchool nhưng output không match chương trình MOET, phải sửa lại 80%

**Top 3 Desired Gains:**
1. Tạo đề thi Toán theo ma trận đề MOET trong 5 phút
2. Giáo án theo format chuẩn của Sở GD&ĐT, chỉ cần review và tinh chỉnh
3. Worksheet differentiated cho 3 level học sinh (giỏi/khá/trung bình)

**Unexpected Insight:** Thầy Tuấn chia sẻ đề thi trong group Zalo 500 giáo viên Toán — nếu EduCareer VN có tính năng share templates, viral coefficient sẽ rất cao trong cộng đồng giáo viên.

**Product Fit:** EduCareer VN cần: 50+ teacher tools align MOET, đề thi generator theo ma trận, giáo án builder theo format Sở. Thầy Tuấn sẵn sàng trả 99K/tháng nếu tiết kiệm >5 giờ/tuần. B2B opportunity: trường mua license cho toàn bộ giáo viên.

---

### Persona 3: Lan — "Marketing Manager muốn chuyển nghề"

- **Tuổi**: 28, Marketing Manager tại công ty FMCG, Hà Nội
- **Thu nhập**: 22 triệu/tháng
- **JTBD chính**: Chuyển sang Product Management trong 6 tháng với CV và portfolio thuyết phục

**Top 3 Pain Points:**
1. Không biết cách "translate" kinh nghiệm Marketing sang PM trên CV
2. Cần research về PM career path, salary range, required skills ở VN nhưng thông tin rời rạc
3. Phỏng vấn PM khác hoàn toàn Marketing — cần practice case study và behavioral questions

**Top 3 Desired Gains:**
1. AI phân tích CV hiện tại và gợi ý cách reframe cho PM role
2. Research hub: tổng hợp thông tin về PM career tại VN (salary, companies, skills gap)
3. Mock interview với AI: practice PM case studies, nhận feedback chi tiết

**Unexpected Insight:** Lan đã mua Career.io subscription ($24.95/tháng) nhưng cancel sau 1 tháng vì templates không phù hợp VN — "CV kiểu Mỹ nộp công ty VN trông rất lạ". Sẵn sàng trả tương đương nếu tool hiểu thị trường VN.

**Product Fit:** EduCareer VN cần: Career pivot advisor, CV rewriter cho thị trường VN, mock interview tiếng Việt, research notebook cho career exploration. Lan sẽ trả Premium ngay từ đầu.

---

## 5. Value Proposition

### Cho Segment chính: "Người đi làm cần upskill/career change" (Persona: Lan)

**1. Who (Ai)**
Người Việt 22-35 tuổi đang đi làm, muốn thăng tiến hoặc chuyển nghề, cần công cụ AI hiểu thị trường VN để nghiên cứu, chuẩn bị CV, và luyện phỏng vấn.

**2. Why (Vấn đề)**
Muốn phát triển sự nghiệp nhưng thiếu công cụ phù hợp: Career.io không hiểu VN, ChatGPT hallucinate về thị trường lao động VN, NotebookLM không có career features. Phải dùng 3-4 tools rời rạc, tốn thời gian và tiền.

**3. What Before (Hiện trạng)**
- Dùng ChatGPT viết CV nhưng output "nghe như dịch máy"
- Google từng thông tin về salary, skills, companies — mất hàng giờ
- Nhờ bạn bè review CV — feedback chủ quan, không chuyên
- Xem YouTube về phỏng vấn nhưng không practice được
- Thử Career.io nhưng templates không phù hợp VN

**4. How (Giải pháp)**
EduCareer VN giúp bạn:
- Upload tài liệu nghiên cứu → AI tổng hợp insights về ngành, công ty, career path
- CV Builder hiểu thị trường VN: templates phù hợp, keywords cho từng ngành, ATS-optimized cho TopCV/VietnamWorks
- Mock Interview AI bằng tiếng Việt: behavioral, technical, case study — feedback chi tiết từng câu
- Career Advisor AI: phân tích skills gap, gợi ý lộ trình upskill cá nhân hóa
- Tất cả trong 1 nền tảng, tiếng Việt native

**5. What After (Kết quả)**
- CV chuyên nghiệp, tối ưu cho thị trường VN trong 30 phút
- Tự tin phỏng vấn sau 10+ mock sessions với AI
- Hiểu rõ career path, salary range, skills cần thiết
- Tiết kiệm 10+ giờ/tuần so với research thủ công
- Tỷ lệ được gọi phỏng vấn tăng 2-3x

**6. Alternatives (Lựa chọn thay thế)**

| Giải pháp | Hạn chế |
|-----------|---------|
| Career.io | Không hiểu thị trường VN, templates kiểu Mỹ, giá cao |
| ChatGPT | Hallucinate, không cite sources, tiếng Việt không tự nhiên |
| NotebookLM | Không có career tools, tiếng Việt hạn chế |
| TopCV Resume Builder | Chỉ có templates, không AI insights, không mock interview |
| Nhờ bạn bè/mentor | Chủ quan, không scalable, phụ thuộc availability |

### Value Proposition Statement

> **EduCareer VN — nền tảng AI đầu tiên giúp người Việt học tập, giảng dạy và phát triển sự nghiệp trong 1 ứng dụng duy nhất. Nghiên cứu thông minh, soạn giáo án trong 5 phút, viết CV chuẩn VN, luyện phỏng vấn với AI — tất cả bằng tiếng Việt tự nhiên.**

---

## 6. Lean Canvas

| # | Section | Chi tiết |
|---|---------|----------|
| **1** | **Problem** | 1. Sinh viên/người đi làm thiếu AI research tool tiếng Việt (NotebookLM không localize) |
| | | 2. Giáo viên VN mất 8-10 giờ/tuần soạn giáo án (MagicSchool không hiểu MOET) |
| | | 3. Career tools (Career.io) không hiểu thị trường tuyển dụng VN |
| **2** | **Solution** | 1. AI Notebook tiếng Việt: upload tài liệu → tổng hợp, Q&A, audio overview |
| | | 2. Teacher AI Tools: 50+ tools align chương trình MOET (đề thi, giáo án, worksheet) |
| | | 3. Career AI: CV builder VN, mock interview tiếng Việt, career advisor |
| **3** | **UVP** | "Nền tảng AI all-in-one đầu tiên cho người Việt — học, dạy, và phát triển sự nghiệp" |
| **4** | **Unfair Advantage** | Deep localization: MOET curriculum database, VN job market data, tiếng Việt NLP fine-tuned. Cộng đồng giáo viên VN (viral qua Zalo groups) |
| **5** | **Customer Segments** | Primary: Giáo viên (25-55), Người đi làm (22-35) |
| | | Secondary: Sinh viên (18-24), Content creators |
| | | Early adopters: Giáo viên tech-savvy trong Zalo groups, sinh viên năm cuối |
| **6** | **Channels** | Zalo groups giáo viên, TikTok/YouTube education content, Facebook groups ngành, partnerships với trường ĐH, SEO tiếng Việt |
| **7** | **Revenue** | Freemium: Free (basic AI tools) → Pro 99K/tháng (unlimited + career) → School License 2M/tháng/trường |
| | | Target LTV: 800K-1.5M VNĐ/user |
| **8** | **Cost Structure** | Fixed: Dev team (8-10 người), AI inference costs, MOET content licensing |
| | | Variable: Marketing, cloud infrastructure, customer support |
| | | CAC target: < 50K VNĐ/user |
| **9** | **Key Metrics** | Activation: Tạo ≥ 1 document/notebook trong tuần đầu |
| | | Retention: D30 retention ≥ 30% |
| | | Revenue: Pro conversion ≥ 6% |
| | | North Star: Weekly Active Creators (WAC) |

---

## 7. PRD — Product Requirements Document

### 1. Summary

EduCareer VN là nền tảng AI all-in-one được thiết kế riêng cho người Việt Nam, kết hợp 3 trụ cột: AI Research Notebook (lấy cảm hứng từ NotebookLM), AI Teacher Tools (lấy cảm hứng từ MagicSchool), và AI Career Development (lấy cảm hứng từ Career.io). Nền tảng sử dụng AI fine-tuned cho tiếng Việt, align với chương trình giáo dục MOET và thị trường tuyển dụng VN.

### 2. Contacts

| Tên | Vai trò | Ghi chú |
|-----|---------|---------|
| [PM Name] | Product Manager | Owner PRD |
| [Design Lead] | UX/UI Designer | Thiết kế cho thị trường VN |
| [Tech Lead] | Engineering Lead | AI/ML architecture |
| [Education Lead] | Education Specialist | MOET curriculum alignment |
| [Career Lead] | Career Advisor | VN job market expertise |

### 3. Background

**Context**: Thị trường AI trong giáo dục VN tăng trưởng CAGR 35.69% (2025-2033). 78% người dùng internet VN đã thử AI nhưng chưa có nền tảng nào kết hợp học tập + giảng dạy + sự nghiệp bằng tiếng Việt. Các giải pháp global (NotebookLM, MagicSchool, Career.io) không localize cho VN.

**Why now**:
- Chi phí AI inference giảm mạnh (GPT-4 level giá giảm 10x trong 2 năm)
- Chính phủ VN đẩy mạnh AI trong giáo dục (Quyết định 127/QĐ-TTg)
- 1.5 triệu giáo viên VN cần tools nhưng MagicSchool không hiểu MOET
- Gen Z VN bắt đầu đi làm, cần career tools phù hợp văn hóa VN
- AI Hay (make-in-Vietnam) chứng minh người Việt prefer AI tiếng Việt

### 4. Objective

**Mục tiêu**: Trở thành nền tảng AI #1 cho học tập, giảng dạy và phát triển sự nghiệp tại Việt Nam trong 24 tháng.

**Key Results (OKR):**
- KR1: Đạt 300K MAU trong 12 tháng sau launch
- KR2: D30 retention ≥ 30%
- KR3: Pro conversion rate ≥ 6%
- KR4: NPS ≥ 50
- KR5: 500+ trường học sử dụng (B2B)
- KR6: 4.5+ rating trên App Store/Google Play

### 5. Market Segments

**Primary**: Giáo viên các cấp (25-55 tuổi)
- 1.5 triệu giáo viên VN, mất 8-10 giờ/tuần soạn bài
- Sẵn sàng trả phí nếu tiết kiệm thời gian đáng kể
- Viral potential cao qua Zalo groups (500-2000 thành viên/group)

**Primary**: Người đi làm cần career development (22-35 tuổi)
- 8 triệu người, thu nhập 8-30 triệu/tháng
- Nhu cầu CV, phỏng vấn, career planning tăng cao
- Sẵn sàng trả phí cho kết quả cụ thể (được gọi phỏng vấn)

**Secondary**: Sinh viên đại học (18-24 tuổi)
- 2.5 triệu sinh viên, cần research + career prep
- Price-sensitive, cần free tier mạnh
- Viral potential cao, future paying customers

### 6. Value Propositions

- **Job**: Nghiên cứu, học tập, soạn bài giảng, viết CV, chuẩn bị phỏng vấn — tất cả bằng tiếng Việt
- **Gain**: Tiết kiệm 5-10 giờ/tuần, tự tin hơn trong sự nghiệp, giảng dạy hiệu quả hơn
- **Pain relieved**: Không còn phải dùng 3-4 tools rời rạc, không còn AI "nghe như dịch máy"
- **Differentiator**: All-in-one + Deep VN localization — không đối thủ nào có cả hai

### 7. Solution

#### 7.1 Key Features — MVP (v1.0)

**Trụ cột 1: AI Research Notebook (Học tập)**

**F1: Smart Notebook**
- Upload tài liệu (PDF, Word, URL, YouTube) → AI tổng hợp tiếng Việt
- Q&A với citations từ tài liệu gốc (grounded responses)
- Tạo summary, outline, flashcards tự động
- Hỗ trợ cả tài liệu tiếng Anh → output tiếng Việt

**F2: Audio Overview tiếng Việt**
- Biến tài liệu thành podcast/audio summary bằng tiếng Việt
- Giọng đọc tự nhiên, không robotic
- Download offline để nghe trên đường đi

**Trụ cột 2: AI Teacher Tools (Giảng dạy)**

**F3: Lesson Plan Generator**
- Tạo giáo án theo format chuẩn Sở GD&ĐT
- Align với chương trình MOET 2018
- Chọn môn, lớp, bài → AI generate đầy đủ
- Hỗ trợ differentiation (3 levels)

**F4: Exam & Quiz Builder**
- Tạo đề thi theo ma trận đề MOET
- Hỗ trợ trắc nghiệm + tự luận
- Tự động tạo đáp án và rubric chấm điểm
- Bank đề theo môn/lớp/chương

**F5: Worksheet & Activity Generator**
- Tạo worksheet, phiếu bài tập
- Hoạt động nhóm, project-based learning
- Export PDF sẵn sàng in

**Trụ cột 3: AI Career Development (Sự nghiệp)**

**F6: CV Builder VN**
- Templates tối ưu cho thị trường VN
- AI gợi ý keywords theo ngành/vị trí
- ATS-optimized cho TopCV, VietnamWorks, LinkedIn VN
- Hỗ trợ cả CV tiếng Việt và tiếng Anh

**F7: Mock Interview AI**
- Phỏng vấn giả lập bằng tiếng Việt
- Behavioral, technical, case study questions
- AI feedback chi tiết: nội dung, cấu trúc, ngôn ngữ cơ thể (video)
- Database câu hỏi theo ngành/công ty VN

**F8: Career Advisor**
- Phân tích skills gap dựa trên CV hiện tại vs vị trí mong muốn
- Gợi ý lộ trình upskill cá nhân hóa
- Salary insights cho thị trường VN
- Career path mapping

#### 7.2 Features — v2.0 (Post-MVP)
- AI Writing Assistant: viết email, báo cáo, proposal tiếng Việt chuyên nghiệp
- Collaboration: giáo viên share templates, cộng đồng đánh giá
- School Dashboard: admin quản lý license, usage analytics
- Integration: Zalo, Google Classroom, Microsoft Teams
- AI Tutor: hỗ trợ học sinh 1-on-1 theo chương trình MOET
- Job Matching: kết nối với TopCV, VietnamWorks API

#### 7.3 Technology
- Frontend: Next.js (Web) + React Native (Mobile)
- Backend: Node.js + Python (AI services)
- AI: Fine-tuned LLM cho tiếng Việt (base: Llama/Mistral hoặc GPT-4o)
- Database: PostgreSQL + Vector DB (Pinecone/Qdrant) cho RAG
- Cloud: AWS ap-southeast-1 (Singapore) cho latency thấp
- Vietnamese NLP: PhoBERT, VnCoreNLP cho tokenization/NER

#### 7.4 Assumptions
1. Giáo viên VN sẵn sàng dùng AI nếu output align MOET (cần validate với 50 giáo viên)
2. Fine-tuned model đạt quality ≥ 90% cho tiếng Việt academic writing (cần benchmark)
3. 6-8% users sẵn sàng trả 99K/tháng cho Pro (cần A/B test pricing)
4. Trường học sẵn sàng mua B2B license (cần pilot 10 trường)
5. MOET curriculum data có thể digitize và structure (cần partnership)

### 8. Release Plan

| Phase | Timeline | Scope |
|-------|----------|-------|
| Alpha | T+0 → T+3 tháng | Smart Notebook + CV Builder (internal + 100 beta users) |
| Beta | T+3 → T+5 tháng | + Teacher Tools (Lesson Plan, Exam Builder) — 1000 beta users |
| v1.0 Launch | T+5 → T+7 tháng | Full MVP 8 features, public launch |
| v1.1 | T+7 → T+10 tháng | Audio Overview VN, School Dashboard, Collaboration |
| v2.0 | T+10 → T+14 tháng | AI Writing Assistant, Job Matching, AI Tutor |

---

## 8. User Stories

### Epic 1: Smart Notebook (AI Research)

**Story 1.1: Upload và tổng hợp tài liệu**
- **Description**: As a student, I want to upload multiple documents and get an AI-generated summary in Vietnamese, so that I can quickly understand key points without reading everything.
- **Acceptance Criteria**:
  1. Upload tối đa 10 tài liệu (PDF, Word, URL) vào 1 notebook
  2. AI tạo summary tiếng Việt trong ≤ 30 giây
  3. Summary có structure: key findings, main arguments, conclusions
  4. Mỗi point có citation link về tài liệu gốc
  5. Hỗ trợ tài liệu tiếng Anh → summary tiếng Việt
  6. Cho phép edit và save summary

**Story 1.2: Q&A với tài liệu**
- **Description**: As a researcher, I want to ask questions about my uploaded documents and get answers with citations, so that I can find specific information quickly.
- **Acceptance Criteria**:
  1. Chat interface để hỏi bằng tiếng Việt hoặc tiếng Anh
  2. AI trả lời chỉ dựa trên tài liệu đã upload (grounded)
  3. Mỗi câu trả lời có inline citations [1], [2]...
  4. Click citation → highlight đoạn gốc trong tài liệu
  5. Nếu không tìm thấy trong tài liệu → thông báo rõ ràng
  6. Lưu lịch sử chat cho mỗi notebook

**Story 1.3: Tạo flashcards tự động**
- **Description**: As a student preparing for exams, I want AI to generate flashcards from my study materials, so that I can review key concepts efficiently.
- **Acceptance Criteria**:
  1. Chọn tài liệu → AI tạo 10-30 flashcards
  2. Mỗi card có: câu hỏi (front) + câu trả lời (back)
  3. Hỗ trợ spaced repetition scheduling
  4. Export sang Anki format
  5. Cho phép edit, thêm, xóa cards
  6. Track progress: đã thuộc / cần ôn lại

### Epic 2: Teacher Tools

**Story 2.1: Tạo giáo án theo MOET**
- **Description**: As a teacher, I want to generate a lesson plan aligned with MOET curriculum in 5 minutes, so that I can spend more time teaching instead of planning.
- **Acceptance Criteria**:
  1. Chọn: môn học, lớp, bài/chương, số tiết
  2. AI generate giáo án theo format chuẩn Sở GD&ĐT
  3. Bao gồm: mục tiêu, hoạt động, phương pháp, đánh giá, rút kinh nghiệm
  4. Hỗ trợ differentiation: 3 levels (giỏi/khá/trung bình)
  5. Export Word/PDF theo đúng format trường yêu cầu
  6. Lưu và tái sử dụng templates

**Story 2.2: Tạo đề thi theo ma trận**
- **Description**: As a teacher, I want to create an exam with a proper MOET question matrix, so that my tests meet official standards without manual effort.
- **Acceptance Criteria**:
  1. Chọn: môn, lớp, loại đề (15 phút/45 phút/cuối kỳ)
  2. AI tạo ma trận đề: nhận biết/thông hiểu/vận dụng/vận dụng cao
  3. Generate câu hỏi trắc nghiệm + tự luận theo ma trận
  4. Tự động tạo đáp án và thang điểm
  5. Tạo 2-4 mã đề khác nhau (cùng ma trận, khác câu hỏi)
  6. Export PDF sẵn sàng in

### Epic 3: Career Development

**Story 3.1: Tạo CV cho thị trường VN**
- **Description**: As a job seeker, I want to create a professional CV optimized for the Vietnamese job market, so that I get more interview callbacks.
- **Acceptance Criteria**:
  1. Chọn template phù hợp ngành (IT, Marketing, Finance, Education...)
  2. Nhập thông tin → AI gợi ý cách viết chuyên nghiệp hơn
  3. AI suggest keywords theo job description (paste JD → optimize)
  4. ATS score checker: kiểm tra tương thích với TopCV/VietnamWorks
  5. Export PDF, Word — format đẹp, chuyên nghiệp
  6. Hỗ trợ cả CV tiếng Việt và tiếng Anh

**Story 3.2: Mock Interview AI**
- **Description**: As a job candidate, I want to practice interviews with AI in Vietnamese, so that I feel confident and prepared for real interviews.
- **Acceptance Criteria**:
  1. Chọn: ngành, vị trí, level (junior/mid/senior)
  2. AI đặt câu hỏi bằng tiếng Việt (behavioral + technical)
  3. User trả lời bằng text hoặc voice
  4. AI feedback: điểm mạnh, điểm cần cải thiện, gợi ý câu trả lời mẫu
  5. Scoring: 1-10 cho mỗi câu trả lời
  6. Lưu lịch sử sessions, track improvement

---

## 9. Customer Journey Map

### Persona: Thầy Tuấn (35 tuổi, Giáo viên Toán THPT)

| Giai đoạn | Touchpoint | Hành động | Cảm xúc | Pain Point | Cơ hội |
|-----------|------------|-----------|---------|------------|--------|
| **Awareness** | Zalo group giáo viên, Facebook | Thấy đồng nghiệp share đề thi tạo bằng EduCareer VN | Tò mò 🤔 | "AI có hiểu chương trình VN không?" | Demo video tạo đề thi MOET trong 5 phút |
| **Consideration** | Website, YouTube review | Xem demo, so sánh với MagicSchool | Quan tâm nhưng hoài nghi 😐 | "Output có đúng format Sở không?" | Free trial 14 ngày, sample outputs theo MOET |
| **Acquisition** | Website signup | Đăng ký bằng Zalo/Google, chọn "Giáo viên" | Kỳ vọng 😊 | Nếu phải nhập nhiều thông tin → bỏ | 1-click signup, chọn môn + lớp là xong |
| **Onboarding** | In-app | Tạo đề thi đầu tiên: chọn Toán → Lớp 10 → Chương 1 | Ấn tượng nếu output tốt 😮 | Nếu đề sai kiến thức → mất trust ngay | QA kỹ content Toán, cho sửa dễ dàng |
| **Aha Moment** | In-app (ngày 1-3) | Tạo đề thi 45 phút hoàn chỉnh trong 5 phút, đúng ma trận | "Wow, tiết kiệm 2 giờ!" 🎉 | Nếu phải sửa >30% → chưa đủ wow | Đảm bảo accuracy ≥ 90% cho môn Toán |
| **Engagement** | In-app (tuần 1-4) | Tạo giáo án, worksheet, đề thi hàng tuần | Hài lòng, tiết kiệm thời gian 😄 | Thiếu môn/lớp cụ thể | Mở rộng coverage nhanh theo feedback |
| **Retention** | In-app + Zalo | Dùng hàng tuần, share templates với đồng nghiệp | Trở thành habit 💪 | Hết free trial → cân nhắc trả phí | Pricing hợp lý 99K, show ROI (tiết kiệm X giờ) |
| **Advocacy** | Zalo groups, họp tổ bộ môn | Giới thiệu cho tổ Toán, share link referral | Tự hào là "early adopter" 🌟 | Đồng nghiệp lớn tuổi ngại công nghệ | Tạo video hướng dẫn đơn giản, referral reward |

### Các khoảnh khắc quan trọng

- **Aha Moment**: Khi giáo viên tạo đề thi đầu tiên đúng ma trận MOET trong <5 phút
- **Moment of Truth**: Đề thi/giáo án có đúng kiến thức và format không? (accuracy quyết định trust)
- **Churn Trigger**: Output sai kiến thức chuyên môn → mất trust vĩnh viễn

### Cải thiện ưu tiên

1. **Quick win**: 1-click signup bằng Zalo, chọn môn + lớp → tạo đề thi đầu tiên trong 2 phút
2. **Quick win**: Share templates đẹp qua Zalo — viral trong cộng đồng giáo viên
3. **Đầu tư lớn**: Content accuracy cho từng môn — cần education specialists review

---

## 10. North Star Metric

### Phân loại Business Game

EduCareer VN thuộc **Productivity Game** — giúp người dùng hoàn thành công việc (nghiên cứu, soạn bài, viết CV) hiệu quả hơn.

### North Star Metric

> **Weekly Active Creators (WAC)** — Số người dùng tạo ≥ 1 document/output có giá trị trong 7 ngày qua

"Document có giá trị" bao gồm: notebook summary, giáo án, đề thi, worksheet, CV, mock interview session.

**Tại sao WAC?**

| Tiêu chí | Đánh giá |
|----------|----------|
| Dễ hiểu | ✅ "Người dùng tạo content hàng tuần" — ai cũng hiểu |
| Customer-centric | ✅ Phản ánh giá trị thực: user đang dùng AI để tạo output hữu ích |
| Sustainable value | ✅ Tạo content hàng tuần = đã integrate vào workflow |
| Vision alignment | ✅ "Giúp người Việt học, dạy, phát triển sự nghiệp" = phải tạo output |
| Quantitative | ✅ Đo được chính xác từ database |
| Actionable | ✅ Teams cải thiện qua UX, AI quality, content coverage |
| Leading indicator | ✅ WAC tăng → retention tăng → revenue tăng |

### Input Metrics

| Input Metric | Mô tả | Tác động lên WAC |
|-------------|--------|-------------------|
| **Activation Rate** | % new users tạo ≥ 1 output trong tuần đầu | Activated → likely trở thành WAC |
| **AI Output Quality Score** | Rating trung bình của user cho AI output (1-5) | Quality cao → dùng tiếp → WAC ổn định |
| **Time to First Value** | Thời gian từ signup → tạo output đầu tiên | Nhanh hơn → activation cao hơn |
| **Feature Breadth** | Số features khác nhau user dùng/tuần | Dùng nhiều features → stickier → WAC cao |
| **D7 Retention** | % users quay lại sau 7 ngày | Trực tiếp đo WAC potential |

### Metrics Constellation

```
                    ┌─────────────────────┐
                    │  Weekly Active       │
                    │  Creators (WAC)      │  ← North Star
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                     │
   ┌──────┴──────┐    ┌───────┴───────┐    ┌───────┴───────┐
   │ Activation  │    │ AI Output     │    │ Feature       │
   │ Rate        │    │ Quality Score │    │ Breadth       │
   └─────────────┘    └───────────────┘    └───────────────┘
          │                    │                     │
   ┌──────┴──────┐    ┌───────┴───────┐    ┌───────┴───────┐
   │ Time to     │    │ D7            │    │ Pro           │
   │ First Value │    │ Retention     │    │ Conversion    │
   └─────────────┘    └───────────────┘    └───────────────┘
```

---

## 11. GTM Strategy

### Chiến lược tổng quan

**Approach**: Community-Led Growth (giáo viên Zalo groups) + Product-Led Growth (free tier mạnh)
**Thị trường đầu tiên**: Giáo viên THPT tại HCM + Hà Nội + Đà Nẵng (beachhead segment)

**Tại sao giáo viên là beachhead?**
- Pain point rõ ràng và cấp bách (8-10 giờ/tuần soạn bài)
- Viral coefficient cao (Zalo groups 500-2000 người, họp tổ bộ môn)
- Willingness to pay (99K/tháng = 1 buổi dạy thêm)
- B2B upsell: 1 giáo viên → cả trường → cả Sở GD&ĐT

### Phase 1: Pre-Launch (T-2 → T0)

| Kênh | Hoạt động | Mục tiêu |
|------|-----------|----------|
| Zalo Groups | Join 50+ groups giáo viên, share free templates tạo bằng EduCareer VN | 5K giáo viên biết đến |
| YouTube | Series "Soạn giáo án trong 5 phút với AI" — demo thực tế | 200K views, 5K subscribers |
| Facebook Groups | Content trong groups giáo viên theo môn (Toán, Văn, Anh...) | 10K reach |
| Waitlist | Landing page "Đăng ký sớm — miễn phí Pro 3 tháng" | 3K signups |
| Pilot Schools | Partner 10 trường THPT tại HCM, HN, ĐN cho beta testing | 200 giáo viên beta |

### Phase 2: Launch (T0 → T+2 tháng)

**Messaging chính**: "Soạn giáo án trong 5 phút. Tạo đề thi chuẩn MOET. Viết CV chuyên nghiệp. Tất cả bằng AI tiếng Việt."

| Kênh | Hoạt động | Budget |
|------|-----------|--------|
| Zalo Ads + Groups | Targeted ads cho giáo viên, share trong groups | 25% budget |
| Facebook/Instagram Ads | Video ads demo teacher tools, career tools | 20% budget |
| YouTube Content | Tutorial series, teacher testimonials, career tips | 15% budget |
| KOL Education | 10 giáo viên nổi tiếng trên TikTok/YouTube review | 15% budget |
| University Partnerships | Workshop "AI cho sinh viên" tại 20 trường ĐH | 10% budget |
| Referral Program | "Mời đồng nghiệp, cả hai nhận 1 tháng Pro free" | 10% budget |
| PR | Bài viết trên VnExpress, Dân Trí, Giáo dục Việt Nam | 5% budget |

### Phase 3: Growth (T+2 → T+8 tháng)

| Kênh | Hoạt động |
|------|-----------|
| B2B School Sales | Tiếp cận Sở GD&ĐT, bán school license (2M/tháng/trường) |
| Viral loops | Giáo viên share templates → đồng nghiệp signup |
| SEO tiếng Việt | "Mẫu giáo án Toán lớp 10", "Cách viết CV tiếng Việt", "Đề thi THPT" |
| Content Marketing | Blog: tips giảng dạy, career advice, AI trong giáo dục |
| Partnerships | TopCV, VietnamWorks (career tools integration) |
| Community | Facebook Group "EduCareer VN Community" — giáo viên share templates |
| Seasonal | Đầu năm học (tháng 9): campaign giáo án. Mùa tuyển dụng (Q1, Q3): campaign CV |

### KPI Targets

| Metric | T+2 tháng | T+4 tháng | T+8 tháng | T+12 tháng |
|--------|-----------|-----------|-----------|------------|
| Signups | 15K | 60K | 200K | 500K |
| MAU | 8K | 40K | 120K | 300K |
| WAC (North Star) | 4K | 25K | 80K | 200K |
| Pro conversion | 4% | 6% | 7% | 8% |
| School licenses | 10 | 50 | 200 | 500 |
| CAC | 40K VNĐ | 30K VNĐ | 20K VNĐ | 15K VNĐ |
| NPS | 40 | 48 | 52 | 55 |

### Rủi ro và giảm thiểu

| Rủi ro | Xác suất | Giảm thiểu |
|--------|----------|------------|
| AI output sai kiến thức chuyên môn | Cao | Hire education specialists review, user feedback loop, human-in-the-loop |
| Giáo viên lớn tuổi ngại dùng AI | Trung bình | Video hướng dẫn đơn giản, onboarding 1-click, support qua Zalo |
| NotebookLM/MagicSchool localize VN | Thấp-Trung bình | First-mover advantage, deep MOET integration khó copy |
| Chi phí AI inference cao | Trung bình | Optimize model size, caching, batch processing |
| MOET thay đổi chương trình | Thấp | Modular content system, update nhanh |
| Privacy concerns (dữ liệu học sinh) | Trung bình | On-premise option cho trường, data residency VN |

---

## Tổng kết Flow

```
Market Research          Strategy              Execution           Go-to-Market
─────────────────    ─────────────────    ─────────────────    ─────────────────
1. Competitor         5. Value Prop         7. PRD               10. North Star
   Analysis           6. Lean Canvas        8. User Stories          Metric
2. Market Sizing                            9. Journey Map       11. GTM Strategy
3. Market Segments
4. User Personas
```

> Tài liệu này là living document — cần được cập nhật liên tục dựa trên data thực tế sau khi launch. Ưu tiên validate assumptions với 50 giáo viên và 50 người đi làm trước khi commit vào development.
