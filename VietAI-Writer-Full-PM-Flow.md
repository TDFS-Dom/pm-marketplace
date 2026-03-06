# ViếtAI — Full Product Management Flow
## Nền tảng AI viết nội dung cho thị trường Việt Nam (Writesonic cho VN)

> Tài liệu này trình bày toàn bộ quy trình PM từ nghiên cứu thị trường → chiến lược sản phẩm → thực thi → go-to-market cho sản phẩm ViếtAI — một nền tảng AI content creation được thiết kế riêng cho người Việt.

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

Thị trường AI writing tools tại Việt Nam đang bùng nổ:
- Thị trường AI Việt Nam đạt ~$753M (2024), dự kiến ~$1B (2025) với CAGR ~15-28%
- 89% doanh nghiệp VN đã sử dụng AI trong marketing
- 78% người dùng online VN đã dùng ít nhất 1 công cụ AI trong 3 tháng gần nhất
- ChatGPT (81%) và Gemini (51%) dẫn đầu về adoption
- AI Hay — app AI Việt Nam đạt ~15 triệu downloads, vượt Gemini và DeepSeek về số user thực tế
- Content marketing là nhu cầu lớn nhất: blog, social media, email, quảng cáo, SEO

### 5 đối thủ trực tiếp

#### 1. AI Hay (Việt Nam)
- **Thành lập**: 2023, Việt Nam
- **Người dùng**: ~15 triệu downloads, 100 triệu Q&A/tháng
- **Funding**: $18M từ các nhà đầu tư lớn (tính đến 08/2025)
- **Thế mạnh**: Hiểu tiếng Việt tốt nhất, UX đơn giản, giá rẻ, brand awareness cao tại VN, đa năng (viết, dịch, chat, hỗ trợ học tập)
- **Điểm yếu**: Chưa chuyên sâu cho content marketing/SEO, thiếu template chuyên nghiệp, không có team collaboration, output quality không ổn định cho long-form
- **Giá**: Freemium, Premium từ ~50K-150K/tháng
- **Mối đe dọa**: Rất cao — brand #1 AI tại VN, user base khổng lồ

#### 2. Writesonic (Global)
- **Thành lập**: 2021, Mỹ
- **Người dùng**: 13,000+ marketing teams toàn cầu
- **Thế mạnh**: All-in-one platform (AI writing + SEO + GEO), 100+ templates, brand voice, API, tích hợp đa nền tảng, AI Article Writer 6.0
- **Điểm yếu**: Tiếng Việt chất lượng trung bình, giá cao cho thị trường VN ($10-49/tháng), không hiểu ngữ cảnh văn hóa VN, support tiếng Anh
- **Giá**: Free (25 credits) → Lite $10/tháng → Professional $49/tháng
- **Mối đe dọa**: Trung bình — sản phẩm tốt nhưng localization kém

#### 3. WriterZen (Việt Nam)
- **Thành lập**: Việt Nam, phục vụ SEA
- **Người dùng**: Phổ biến trong agencies VN
- **Thế mạnh**: SEO-focused, keyword research mạnh, topic clustering, plagiarism check, hiểu thị trường VN
- **Điểm yếu**: Chủ yếu SEO, thiếu tính năng viết đa dạng (social, email, ads), UX phức tạp cho người mới, giá hướng agency
- **Giá**: Từ $23/tháng
- **Mối đe dọa**: Trung bình — mạnh ở SEO nhưng không phải all-in-one writing

#### 4. ChatGPT / GPT-based tools (OpenAI)
- **Thành lập**: 2022, OpenAI
- **Người dùng**: 81% marketers VN sử dụng
- **Thế mạnh**: Đa năng, chất lượng output cao, liên tục cải tiến, brand trust toàn cầu
- **Điểm yếu**: Không chuyên cho content marketing VN, không có template, không SEO tools, không brand voice management, cần prompt engineering skill
- **Giá**: Free → Plus $20/tháng → Team $25/user/tháng
- **Mối đe dọa**: Rất cao — "good enough" cho nhiều use cases

#### 5. Copy.ai (Global)
- **Thành lập**: 2020, Mỹ
- **Người dùng**: >10 triệu users toàn cầu
- **Thế mạnh**: 90+ templates, workflow automation, brand voice, team collaboration, API
- **Điểm yếu**: Tiếng Việt kém, giá cao ($36-49/tháng), không hiểu SEO VN, support tiếng Anh
- **Giá**: Free (2,000 words) → Starter $36/tháng → Advanced $49/tháng
- **Mối đe dọa**: Thấp-trung bình — sản phẩm tốt nhưng không localize

### Cơ hội khác biệt hóa cho ViếtAI

| Yếu tố | Đối thủ hiện tại | Cơ hội ViếtAI |
|---------|-------------------|---------------|
| Tiếng Việt native | AI Hay tốt nhưng chưa chuyên content; global tools kém | AI được train riêng cho content tiếng Việt, hiểu ngữ cảnh văn hóa |
| SEO tiếng Việt | WriterZen mạnh nhưng đắt; global tools không hiểu SEO VN | Tích hợp SEO cho Google VN, keyword research tiếng Việt |
| Templates VN | Hầu như không có | 100+ templates cho content VN: Shopee listing, Zalo OA, Facebook ads VN, email marketing VN |
| Brand Voice VN | Không ai có | Tùy chỉnh giọng văn: formal, Gen Z, miền Bắc/Nam, ngành hàng |
| Giá VN-friendly | Global tools quá đắt | Pricing phù hợp thu nhập VN: từ 99K/tháng |
| All-in-one cho VN | Phân mảnh: AI Hay (chat), WriterZen (SEO), ChatGPT (general) | 1 platform: viết + SEO + social + ads + email |

---

## 2. Ước tính quy mô thị trường

### Định nghĩa thị trường
- **Vấn đề**: Doanh nghiệp và content creators VN cần công cụ AI viết nội dung chất lượng bằng tiếng Việt, tối ưu SEO, với giá phù hợp
- **Phạm vi**: Việt Nam, doanh nghiệp SME + freelancers + agencies + creators

### TAM (Total Addressable Market)

**Top-down:**
- Thị trường AI VN: ~$1B (2025), content/marketing AI chiếm ~15-20%
- Thị trường content marketing VN: ước tính ~$500M/năm
- AI writing tools chiếm ~10-15% chi tiêu content marketing
- **TAM ≈ $50-75M/năm (~1,250-1,875 tỷ VNĐ)**

**Bottom-up:**
- Doanh nghiệp SME VN: ~900,000 (đang hoạt động)
- Có nhu cầu content marketing: ~30% → 270,000 DN
- Freelancers/creators: ~200,000 người
- Agencies: ~5,000
- Tổng addressable users: ~475,000
- ARPU trung bình: $120/năm (mix free + paid)
- **TAM ≈ $57M/năm (~1,425 tỷ VNĐ)**

### SAM (Serviceable Addressable Market)

- SME có ngân sách cho AI tools: ~40% → 108,000 DN
- Freelancers sẵn sàng trả phí: ~30% → 60,000
- Agencies: ~3,000
- Tổng SAM users: ~171,000
- ARPU: $150/năm (paid users)
- **SAM ≈ $25.6M/năm (~640 tỷ VNĐ)** (~45% TAM)

### SOM (Serviceable Obtainable Market)

- Năm 1-3: Mục tiêu 3-6% SAM
- **SOM ≈ $770K-1.5M/năm (~19-38 tỷ VNĐ)**
- Tương đương ~5,000-10,000 paying users

### Bảng tổng hợp

| Metric | Ước tính hiện tại | Dự báo 3 năm |
|--------|-------------------|---------------|
| TAM | $57M (~1,425 tỷ VNĐ) | $95M (~2,375 tỷ VNĐ) |
| SAM | $25.6M (~640 tỷ VNĐ) | $45M (~1,125 tỷ VNĐ) |
| SOM | $1.1M (~28 tỷ VNĐ) | $5M (~125 tỷ VNĐ) |

### Động lực tăng trưởng
1. AI adoption tại VN tăng CAGR 15-28% (confidence: high)
2. E-commerce VN đạt $15.3B → nhu cầu content cho Shopee, Lazada, TikTok Shop tăng mạnh (confidence: high)
3. Chi phí nhân sự content writer tăng → doanh nghiệp tìm AI thay thế (confidence: medium)
4. Google SGE/AI Overviews thay đổi SEO → cần content chất lượng hơn (confidence: medium)

### Giả định chính
1. 89% DN dùng AI nhưng chỉ ~30-40% sẵn sàng trả phí cho tool chuyên dụng (confidence: medium)
2. ARPU tại VN thấp hơn 3-5x so với global market (confidence: high)
3. Thị trường content marketing VN tiếp tục tăng >20%/năm (confidence: high)
4. Không có "winner takes all" — nhiều tools cùng tồn tại (confidence: medium)

---

## 3. Phân khúc thị trường

### Segment 1: "SME Marketing Team" (40% thị trường)
- **Demographics**: Doanh nghiệp 10-200 nhân viên, có 1-3 người làm marketing
- **Ngành**: E-commerce, F&B, giáo dục, bất động sản, dịch vụ
- **JTBD**: "Khi tôi cần tạo content cho nhiều kênh (website, Facebook, Shopee, email) mỗi ngày, tôi muốn có công cụ giúp viết nhanh và đúng tone thương hiệu để không phải thuê thêm content writer"
- **Pain points**: Thiếu nhân sự content, chất lượng không đều, tốn thời gian viết, không biết SEO
- **Budget**: 200K-1M VNĐ/tháng cho tools
- **Product fit**: Rất cao — cần templates, brand voice, multi-channel output

### Segment 2: "Freelance Content Creator" (25% thị trường)
- **Demographics**: 22-35 tuổi, freelance writer/copywriter/social media manager
- **Thu nhập**: 10-40 triệu/tháng
- **JTBD**: "Khi tôi nhận nhiều dự án cùng lúc, tôi muốn có AI hỗ trợ viết draft nhanh để tôi tập trung vào editing và sáng tạo, tăng output gấp 3-5x"
- **Pain points**: Deadline gấp, writer's block, cần viết nhiều tone khác nhau cho nhiều client, research tốn thời gian
- **Budget**: 99K-299K VNĐ/tháng (chi phí cá nhân)
- **Product fit**: Cao — cần speed, quality, đa dạng template

### Segment 3: "Digital Agency" (15% thị trường)
- **Demographics**: Agency marketing/content 5-50 người, phục vụ nhiều client
- **JTBD**: "Khi team tôi quản lý content cho 10-20 clients, tôi muốn có platform giúp standardize quy trình, quản lý brand voice từng client, và scale output mà không tăng headcount"
- **Pain points**: Quản lý nhiều brand voice, QC chất lượng, onboard nhân viên mới, báo cáo cho client
- **Budget**: 2-10M VNĐ/tháng
- **Product fit**: Rất cao — cần team collaboration, multi-brand, workflow management

### Segment 4: "E-commerce Seller" (15% thị trường)
- **Demographics**: Chủ shop Shopee/Lazada/TikTok Shop, 1-5 người
- **JTBD**: "Khi tôi cần đăng 50-100 sản phẩm mới mỗi tuần, tôi muốn AI viết mô tả sản phẩm hấp dẫn và tối ưu search trên sàn để tăng traffic và chuyển đổi"
- **Pain points**: Viết mô tả sản phẩm lặp đi lặp lại, không biết tối ưu keyword trên sàn, cần bulk generation
- **Budget**: 99K-499K VNĐ/tháng
- **Product fit**: Cao — cần product description templates, bulk generation, marketplace SEO

### Segment 5: "Blogger/KOL" (5% thị trường)
- **Demographics**: Blogger, YouTuber, TikToker cần viết script/caption/blog
- **JTBD**: "Khi tôi cần đăng content hàng ngày trên nhiều nền tảng, tôi muốn AI giúp repurpose 1 ý tưởng thành nhiều format (blog → caption → script → thread) để tiết kiệm thời gian"
- **Pain points**: Content fatigue, cần đăng đều đặn, repurpose content tốn thời gian
- **Budget**: 99K-199K VNĐ/tháng
- **Product fit**: Trung bình-cao — cần content repurposing, social media templates

---

## 4. User Personas

### Persona 1: Hương — "Marketing Manager SME"
- **Tuổi**: 29, Marketing Manager tại công ty mỹ phẩm nội địa, HCM
- **Team**: 2 người (Hương + 1 junior)
- **Kênh quản lý**: Website (WordPress), Facebook Page, Instagram, Shopee, email newsletter
- **JTBD chính**: Tạo 30+ bài content/tuần cho tất cả kênh mà không cần thuê thêm người
- **Pain points**:
  1. Junior writer viết chưa đúng tone thương hiệu, phải sửa nhiều
  2. Tốn 2-3 giờ/bài blog SEO, chỉ xuất được 2 bài/tuần
  3. Content Facebook và Shopee listing lặp đi lặp lại, nhàm chán
- **Desired gains**:
  1. Giảm thời gian viết blog từ 3 giờ xuống 30 phút
  2. Brand voice nhất quán trên mọi kênh
  3. SEO ranking tăng cho các keyword mục tiêu
- **Unexpected insight**: Hương không cần AI viết hoàn hảo — cô cần AI viết "80% done" để cô chỉ cần edit 20%. Cô sợ AI viết quá generic hơn là sợ AI viết sai.
- **Product fit**: ViếtAI cần brand voice training, multi-channel templates, SEO integration, và team workspace để junior có thể dùng với guardrails.

### Persona 2: Tuấn — "Freelance Copywriter"
- **Tuổi**: 26, freelance copywriter, làm việc remote từ Đà Nẵng
- **Clients**: 5-8 clients đồng thời (F&B, tech startup, bất động sản, giáo dục)
- **Output**: 40-60 bài content/tháng
- **JTBD chính**: Tăng output từ 60 lên 150 bài/tháng mà không giảm chất lượng
- **Pain points**:
  1. Writer's block khi chuyển giữa các ngành khác nhau trong ngày
  2. Research cho mỗi bài blog tốn 30-60 phút
  3. Mỗi client có tone khác nhau — dễ nhầm lẫn
- **Desired gains**:
  1. AI draft nhanh → Tuấn chỉ cần polish và thêm góc nhìn cá nhân
  2. Lưu profile từng client (tone, keywords, style guide)
  3. Research tự động: AI tổng hợp thông tin từ nhiều nguồn
- **Unexpected insight**: Tuấn dùng ChatGPT nhưng tốn 40% thời gian viết prompt và sửa output. Anh sẵn sàng trả tiền cho tool "hiểu mình muốn gì mà không cần giải thích nhiều".
- **Product fit**: ViếtAI cần client profiles/brand voice switching, research assistant, và output quality cao cho tiếng Việt. Tuấn trả 199K-299K/tháng nếu tiết kiệm được >10 giờ/tháng.

### Persona 3: Ngọc — "Agency Content Lead"
- **Tuổi**: 32, Content Lead tại digital agency 25 người, HN
- **Team**: 8 content writers, phục vụ 15 clients
- **JTBD chính**: Scale content production 3x mà không tăng headcount, đồng thời maintain quality standards
- **Pain points**:
  1. Onboard writer mới mất 2-3 tháng để hiểu tone từng client
  2. QC review tốn 30% thời gian của Ngọc — bottleneck
  3. Client yêu cầu báo cáo content performance nhưng team không có bandwidth
- **Desired gains**:
  1. Brand voice templates cho từng client → writer mới dùng được ngay
  2. AI-assisted QC: check tone, grammar, SEO trước khi Ngọc review
  3. Content calendar và workflow management tích hợp
- **Unexpected insight**: Ngọc không muốn AI thay thế writers — cô muốn AI nâng cấp junior writers thành mid-level. "Nếu AI giúp junior viết được 70% chất lượng senior, tôi tiết kiệm được 3 headcount."
- **Product fit**: ViếtAI cần team workspace, role-based access, multi-brand management, content approval workflow, và usage analytics. Ngọc sẵn sàng trả 3-5M/tháng cho team plan.

---

## 5. Value Proposition

### Cho Segment chính: "SME Marketing Team" (Persona: Hương)

**1. Who (Ai)**
Marketing teams tại SME Việt Nam (1-5 người) cần tạo content đa kênh hàng ngày bằng tiếng Việt với ngân sách hạn chế.

**2. Why (Vấn đề)**
Team nhỏ nhưng phải quản lý 4-6 kênh content (website, Facebook, Instagram, Shopee, email, Zalo). Viết content tốn thời gian, chất lượng không đều giữa các thành viên, và không có chuyên gia SEO. Thuê thêm người hoặc agency thì vượt ngân sách.

**3. What Before (Hiện trạng)**
- Dùng ChatGPT nhưng phải viết prompt dài, output generic, không đúng tone thương hiệu
- Copy-paste từ đối thủ rồi sửa lại → content không unique
- Junior writer viết → Marketing Manager phải sửa lại 50-70%
- Không có quy trình SEO → blog không lên top Google
- Mỗi bài blog tốn 2-3 giờ, Facebook post tốn 30-45 phút

**4. How (Giải pháp)**
ViếtAI giúp bạn:
- 100+ templates tiếng Việt cho mọi kênh: blog SEO, Facebook post, Shopee listing, email, Zalo OA, Instagram caption
- Brand Voice AI: train AI với tone thương hiệu của bạn 1 lần, mọi output sau đó đều nhất quán
- SEO Assistant: keyword research tiếng Việt, content optimization, meta tags tự động
- 1-click repurpose: biến 1 blog thành 5 Facebook posts + 3 email snippets + 1 Shopee description
- Team workspace: junior dùng templates + brand voice → output đạt chuẩn ngay

**5. What After (Kết quả)**
- Giảm thời gian viết blog từ 3 giờ xuống 30 phút
- Tăng output content 3-5x mà không tăng headcount
- Brand voice nhất quán trên mọi kênh
- Blog SEO bắt đầu rank trên Google VN sau 2-3 tháng
- Marketing Manager tập trung vào strategy thay vì viết/sửa content

**6. Alternatives (Lựa chọn thay thế)**

| Giải pháp | Hạn chế |
|-----------|---------|
| ChatGPT | Generic, không templates, không SEO, không brand voice, cần prompt skill |
| AI Hay | Chưa chuyên content marketing, thiếu SEO, không team features |
| Writesonic | Tiếng Việt kém, giá cao ($10-49/tháng), không hiểu văn hóa VN |
| WriterZen | Chỉ SEO, không viết đa kênh, giá cao ($23/tháng), UX phức tạp |
| Thuê content writer | 8-15M/tháng/người, chất lượng phụ thuộc cá nhân, khó scale |

### Value Proposition Statement
> **ViếtAI là nền tảng AI viết nội dung đầu tiên được xây dựng riêng cho thị trường Việt Nam — giúp marketing teams tạo content đa kênh nhanh gấp 5x, đúng tone thương hiệu, tối ưu SEO tiếng Việt, với giá chỉ bằng 1/10 chi phí thuê thêm người.**

---

## 6. Lean Canvas

| # | Section | Chi tiết |
|---|---------|----------|
| **1** | **Problem** | 1. SME VN thiếu nhân sự content nhưng cần đăng 4-6 kênh mỗi ngày |
| | | 2. ChatGPT output tiếng Việt generic, không đúng tone, cần prompt engineering |
| | | 3. Không có tool SEO tiếng Việt tích hợp với content creation |
| **2** | **Solution** | 1. 100+ templates tiếng Việt cho mọi kênh (blog, social, e-commerce, email) |
| | | 2. Brand Voice AI — train 1 lần, output nhất quán mãi mãi |
| | | 3. SEO Assistant tích hợp: keyword research VN + content optimization |
| **3** | **UVP** | "Viết content tiếng Việt chuyên nghiệp trong 1 phút — đúng tone, đúng SEO, đúng kênh" |
| **4** | **Unfair Advantage** | AI model fine-tuned cho tiếng Việt + database 10,000+ mẫu content VN thành công + deep understanding văn hóa tiêu dùng VN |
| **5** | **Customer Segments** | Primary: SME marketing teams (1-5 người) |
| | | Secondary: Freelance copywriters, Digital agencies |
| | | Early adopters: Marketers đang dùng ChatGPT cho content và thấy chưa đủ |
| **6** | **Channels** | Facebook Groups marketing VN, LinkedIn VN, SEO blog, KOL marketing, partnerships với Haravan/Sapo/KiotViet, webinars |
| **7** | **Revenue** | Freemium: Free (5 bài/tháng) → Starter 99K/tháng → Pro 299K/tháng → Team 199K/user/tháng → Agency 149K/user/tháng (min 5 users) |
| | | Target LTV: 3.6M-7.2M VNĐ/user (12-24 tháng retention) |
| **8** | **Cost Structure** | Fixed: Engineering team (8-12 người), AI compute (GPT-4/Claude API + fine-tuned models), cloud infrastructure |
| | | Variable: API costs per generation, marketing/UA, customer support, KOL partnerships |
| | | CAC target: < 200K VNĐ/paying user |
| **9** | **Key Metrics** | Activation: Tạo ≥ 3 bài content trong tuần đầu |
| | | Retention: M3 retention ≥ 40% (paying users) |
| | | Revenue: MRR growth ≥ 15%/tháng trong 12 tháng đầu |
| | | North Star: Weekly Active Creators (WAC) |

---

## 7. PRD — Product Requirements Document

### 1. Summary
ViếtAI là nền tảng AI content creation được thiết kế riêng cho thị trường Việt Nam. Platform kết hợp AI writing (fine-tuned cho tiếng Việt), SEO tools, brand voice management, và multi-channel templates để giúp marketing teams, freelancers, và agencies tạo content chuyên nghiệp nhanh gấp 5x.

### 2. Contacts

| Tên | Vai trò | Ghi chú |
|-----|---------|---------|
| [PM Name] | Product Manager | Owner PRD |
| [AI/ML Lead] | AI/ML Engineer | Fine-tune models tiếng Việt |
| [Frontend Lead] | Frontend Engineer | Web app + Chrome extension |
| [Backend Lead] | Backend Engineer | API, infrastructure, billing |
| [Content Lead] | Content Strategist | Templates library, brand voice |
| [Growth Lead] | Growth Marketing | GTM, partnerships |

### 3. Background

**Context**: 89% doanh nghiệp VN đã dùng AI trong marketing, nhưng chủ yếu dùng ChatGPT — một tool general-purpose không được tối ưu cho content marketing tiếng Việt. Thị trường thiếu một Writesonic/Jasper/Copy.ai phiên bản Việt Nam.

**Why now**:
- AI writing quality đã đủ tốt cho production use (GPT-4, Claude 3.5+)
- Chi phí API giảm mạnh → viable business model với giá VN-friendly
- E-commerce VN bùng nổ ($15.3B) → nhu cầu content cho Shopee/Lazada/TikTok Shop cực lớn
- Google SGE thay đổi SEO → doanh nghiệp cần content chất lượng cao hơn, nhiều hơn
- Chưa có player nào dominate segment "AI writing chuyên cho VN"

### 4. Objective

**Mục tiêu**: Trở thành nền tảng AI writing #1 cho thị trường Việt Nam trong 18 tháng.

**Key Results (OKR)**:
- KR1: Đạt 50K registered users và 5K paying users trong 12 tháng
- KR2: MRR đạt 500M VNĐ (~$20K) vào tháng 12
- KR3: M3 retention (paying users) ≥ 40%
- KR4: NPS ≥ 45
- KR5: Average content quality score ≥ 4.0/5.0 (user rating)

### 5. Market Segments

**Primary**: SME Marketing Teams (1-5 người)
- Doanh nghiệp 10-200 nhân viên
- Cần content cho 4-6 kênh: website, Facebook, Instagram, Shopee, email, Zalo
- Budget cho tools: 200K-1M VNĐ/tháng

**Secondary**: Freelance Copywriters
- 22-35 tuổi, làm việc với 5-10 clients
- Cần tăng output và đa dạng hóa tone/style
- Budget: 99K-299K VNĐ/tháng

**Tertiary**: Digital Agencies
- 5-50 người, phục vụ 10-20+ clients
- Cần team collaboration, multi-brand management
- Budget: 2-10M VNĐ/tháng

### 6. Value Propositions

- **Job**: Tạo content marketing tiếng Việt chuyên nghiệp cho đa kênh
- **Gain**: Tăng output 3-5x, nhất quán brand voice, rank SEO tốt hơn
- **Pain relieved**: Không còn writer's block, không cần prompt engineering, không lo content generic
- **Differentiator**: Duy nhất tại VN kết hợp AI writing native tiếng Việt + SEO VN + brand voice + multi-channel templates

### 7. Solution

#### 7.1 Key Features — MVP (v1.0)

**F1: AI Writer Engine (Core)**
- Viết content tiếng Việt chất lượng cao với nhiều tone: chuyên nghiệp, thân thiện, Gen Z, luxury, casual
- Hỗ trợ long-form (blog 1,500-3,000 từ) và short-form (caption, headline, tagline)
- Auto-research: AI tổng hợp thông tin từ web trước khi viết
- Plagiarism check tích hợp
- Output editing: rewrite, expand, shorten, change tone

**F2: Templates Library (100+ templates)**
- Blog SEO (how-to, listicle, comparison, review, pillar page)
- Facebook (post, ad copy, carousel script)
- Instagram (caption, story script, Reels script)
- E-commerce (Shopee listing, product description, review response)
- Email (newsletter, welcome series, promotional, abandoned cart)
- Zalo OA (broadcast message, mini-app content)
- Ads (Google Ads, Facebook Ads, TikTok Ads)
- PR (press release, company profile, case study)

**F3: Brand Voice AI**
- Upload mẫu content → AI học tone, style, vocabulary
- Tạo brand voice profile: formal/casual, miền Bắc/Nam, ngành hàng
- Apply brand voice cho mọi output tự động
- Hỗ trợ nhiều brand voices (cho agencies/freelancers)

**F4: SEO Assistant**
- Keyword research tiếng Việt (volume, difficulty, suggestions)
- Content optimization score (real-time khi viết)
- Auto-generate meta title, meta description, heading structure
- Internal linking suggestions
- Competitor content analysis

**F5: Content Repurposer**
- Input: 1 blog post → Output: 5 Facebook posts + 3 email snippets + 1 Shopee description + 3 Instagram captions
- Tự động adjust tone và format cho từng kênh
- Bulk generation cho e-commerce (upload CSV sản phẩm → generate descriptions)

#### 7.2 Features — v2.0 (Post-MVP)
- Team workspace với roles (admin, editor, writer)
- Content calendar và publishing scheduler
- AI image generation (thumbnail, social media graphics)
- Chrome extension (viết trực tiếp trên Facebook, Shopee, WordPress)
- API cho developers và agencies
- Analytics dashboard (content performance tracking)
- Integrations: WordPress, Haravan, Sapo, Shopee, Facebook Business
- AI chatbot assistant cho content strategy

#### 7.3 Technology
- Frontend: Next.js (web app) + Chrome Extension
- Backend: Node.js + PostgreSQL + Redis
- AI: GPT-4o / Claude API + fine-tuned Vietnamese model (Llama-based)
- Search/SEO: Custom crawling + Google Search API + Ahrefs/SEMrush API
- Cloud: AWS ap-southeast-1 (Singapore) cho latency thấp
- CDN: CloudFront cho static assets

#### 7.4 Assumptions
1. Fine-tuned model cho tiếng Việt sẽ outperform base GPT-4 về chất lượng content VN (cần validate)
2. Users sẵn sàng trả 99-299K/tháng thay vì dùng ChatGPT miễn phí (cần validate pricing)
3. Templates library là key differentiator — users muốn "click and generate" hơn là viết prompt (cần validate)
4. Brand voice AI đạt accuracy ≥ 80% sau training với 10-20 mẫu content (cần validate)
5. SEO tiếng Việt có đủ data để keyword research chính xác (cần validate data sources)

### 8. Release Plan

| Phase | Timeline | Scope |
|-------|----------|-------|
| Alpha | T+0 → T+3 tháng | AI Writer + 30 templates + basic SEO (internal + 50 beta users) |
| Beta | T+3 → T+5 tháng | + Brand Voice + 70 templates + Repurposer (500 beta users) |
| v1.0 Launch | T+5 → T+6 tháng | Full MVP, 100+ templates, public launch |
| v1.5 | T+6 → T+9 tháng | Team workspace, Chrome extension, API |
| v2.0 | T+9 → T+14 tháng | Integrations, AI images, analytics, content calendar |

---

## 8. User Stories

### Epic 1: AI Writer Engine

**Story 1.1: Viết blog SEO từ keyword**
- **Description**: As a marketing manager, I want to input a keyword and get a full SEO-optimized blog post in Vietnamese, so that I can publish quality content without spending 3 hours writing.
- **Acceptance Criteria**:
  1. Nhập keyword chính (ví dụ: "cách chăm sóc da mùa hè") → AI generate outline trước
  2. User review/edit outline → confirm → AI viết full bài 1,500-3,000 từ
  3. Bài viết có heading structure (H2, H3), keyword density hợp lý, internal linking suggestions
  4. Auto-generate meta title (≤60 ký tự) và meta description (≤160 ký tự)
  5. Plagiarism score hiển thị real-time (target: < 15% similarity)
  6. Thời gian generate ≤ 90 giây cho bài 2,000 từ

**Story 1.2: Viết Facebook post từ brief**
- **Description**: As a social media manager, I want to describe my promotion briefly and get 3 Facebook post variations, so that I can A/B test different angles.
- **Acceptance Criteria**:
  1. Nhập brief ngắn (ví dụ: "Giảm giá 30% son môi, target nữ 20-30 tuổi, tone vui vẻ")
  2. AI generate 3 variations với hook, body, CTA khác nhau
  3. Mỗi variation có emoji suggestions phù hợp
  4. Độ dài tối ưu cho Facebook (150-300 từ)
  5. Option: thêm hashtag suggestions
  6. 1-click copy hoặc export

**Story 1.3: Rewrite và adjust tone**
- **Description**: As a copywriter, I want to paste existing content and rewrite it in a different tone, so that I can adapt content for different clients quickly.
- **Acceptance Criteria**:
  1. Paste text gốc vào editor
  2. Chọn tone mới: chuyên nghiệp, thân thiện, Gen Z, luxury, hài hước, formal
  3. AI rewrite giữ nguyên ý chính nhưng thay đổi tone hoàn toàn
  4. Hiển thị side-by-side: original vs rewritten
  5. Highlight những thay đổi chính
  6. Option: adjust thêm (ngắn hơn, dài hơn, đơn giản hơn)

### Epic 2: Templates Library

**Story 2.1: Browse và sử dụng template**
- **Description**: As a user, I want to browse templates by category and channel, so that I can quickly find the right starting point for my content.
- **Acceptance Criteria**:
  1. Templates organized theo category: Blog, Social, E-commerce, Email, Ads, PR
  2. Filter theo kênh: Facebook, Instagram, Shopee, Zalo, Google, TikTok
  3. Mỗi template có: tên, mô tả, preview output mẫu, input fields cần điền
  4. "Popular" và "New" tags cho templates
  5. Search templates bằng keyword
  6. Favorite templates để truy cập nhanh

**Story 2.2: Shopee product listing bulk generation**
- **Description**: As an e-commerce seller, I want to upload a CSV of products and generate optimized Shopee listings for all of them, so that I can list 100 products in 1 hour instead of 1 week.
- **Acceptance Criteria**:
  1. Upload CSV với columns: tên sản phẩm, category, đặc điểm chính, giá
  2. AI generate cho mỗi sản phẩm: tiêu đề tối ưu, mô tả hấp dẫn, bullet points, keywords
  3. Preview tất cả listings trước khi export
  4. Edit individual listings inline
  5. Export CSV ready-to-upload lên Shopee
  6. Xử lý batch ≤ 100 sản phẩm/lần, thời gian ≤ 10 phút

### Epic 3: Brand Voice AI

**Story 3.1: Tạo brand voice profile**
- **Description**: As a marketing manager, I want to train the AI with my brand's writing style, so that all generated content sounds like my brand.
- **Acceptance Criteria**:
  1. Upload 5-20 mẫu content đại diện cho brand voice (blog, social, email)
  2. AI phân tích và tạo brand voice profile: tone, vocabulary, sentence structure, do's & don'ts
  3. Hiển thị summary: "Brand voice của bạn: Thân thiện, chuyên nghiệp, hay dùng câu hỏi, tránh từ ngữ quá formal"
  4. User review và adjust profile
  5. Test: generate 1 mẫu content với brand voice → user rate quality
  6. Lưu profile, apply tự động cho mọi generation sau

**Story 3.2: Switch brand voice (cho freelancers/agencies)**
- **Description**: As a freelancer working with multiple clients, I want to switch between brand voice profiles quickly, so that I don't mix up tones between clients.
- **Acceptance Criteria**:
  1. Dropdown chọn brand voice profile trên mọi màn hình generation
  2. Hiển thị tên client/brand + tone summary khi hover
  3. Tạo tối đa 3 profiles (Free), 10 (Pro), unlimited (Team/Agency)
  4. Duplicate profile để tạo variation
  5. Color-coded profiles để phân biệt nhanh
  6. Warning nếu user generate content mà chưa chọn brand voice

### Epic 4: SEO Assistant

**Story 4.1: Keyword research tiếng Việt**
- **Description**: As a content marketer, I want to research Vietnamese keywords with search volume and difficulty, so that I can target the right topics for my blog.
- **Acceptance Criteria**:
  1. Nhập seed keyword tiếng Việt → hiển thị: search volume, keyword difficulty, CPC
  2. Gợi ý 20-50 related keywords và long-tail variations
  3. Group keywords theo topic clusters
  4. Filter: volume range, difficulty range, intent (informational, transactional, navigational)
  5. Save keywords vào lists
  6. "Write about this" button → chuyển thẳng sang AI Writer với keyword đã chọn

**Story 4.2: Content SEO score real-time**
- **Description**: As a writer, I want to see my content's SEO score update in real-time as I write, so that I can optimize before publishing.
- **Acceptance Criteria**:
  1. SEO score 0-100 hiển thị bên phải editor
  2. Checklist: keyword density, heading structure, meta tags, content length, readability
  3. Mỗi item có status: ✅ tốt, ⚠️ cần cải thiện, ❌ thiếu
  4. Gợi ý cụ thể: "Thêm keyword 'chăm sóc da' vào H2 đầu tiên"
  5. Score cập nhật real-time khi user edit
  6. Competitor comparison: "Top 3 bài rank cho keyword này có trung bình 2,500 từ"

### Epic 5: Content Repurposer

**Story 5.1: Blog → Multi-channel content**
- **Description**: As a marketing manager, I want to turn one blog post into content for 5 different channels, so that I maximize the value of every piece of content.
- **Acceptance Criteria**:
  1. Paste hoặc chọn blog post đã viết
  2. Chọn output channels: Facebook, Instagram, Email, Shopee, Zalo, TikTok script
  3. AI generate content phù hợp format và tone từng kênh
  4. Preview tất cả outputs trên 1 màn hình
  5. Edit individual outputs inline
  6. 1-click copy all hoặc export package (ZIP với từng file)

---

## 9. Customer Journey Map

### Persona: Hương (29 tuổi, Marketing Manager SME mỹ phẩm)

| Giai đoạn | Touchpoint | Hành động | Cảm xúc | Pain Point | Cơ hội |
|-----------|------------|-----------|---------|------------|--------|
| **Awareness** | Facebook Group "Marketing VN", LinkedIn | Thấy bài review ViếtAI từ marketer khác: "Viết blog SEO trong 10 phút" | Tò mò nhưng hoài nghi 🤔 | "AI viết tiếng Việt có tốt không? Chắc lại generic" | Demo video thực tế: before/after content quality |
| **Consideration** | Website ViếtAI, blog, so sánh | So sánh ViếtAI vs ChatGPT vs AI Hay, đọc case studies | Quan tâm, đang evaluate 😐 | "Giá có đáng không? Team tôi có dùng được không?" | Free trial 7 ngày không cần thẻ, case study ngành mỹ phẩm |
| **Acquisition** | Website signup | Đăng ký free trial, tạo account | Kỳ vọng 😊 | Nếu signup phức tạp → bỏ | 1-click signup với Google/Facebook, không cần thẻ tín dụng |
| **Onboarding** | In-app | Setup: chọn ngành, upload brand samples, chọn kênh chính | Hơi mất thời gian nhưng thấy giá trị 😅 | Nếu phải upload quá nhiều → skip | Quick start: chọn ngành → AI gợi ý brand voice mẫu, upload samples là optional |
| **Aha Moment** | In-app (ngày 1-2) | Dùng template "Blog SEO mỹ phẩm" → generate bài 2,000 từ trong 2 phút | Wow, chất lượng tốt hơn mong đợi 😮 | Nếu output kém → mất trust ngay | Đảm bảo first-run experience xuất sắc: curated templates cho ngành user chọn |
| **Engagement** | In-app (tuần 1-4) | Dùng hàng ngày: blog, Facebook posts, Shopee listings | Productive, tiết kiệm thời gian 😄 | Một số output cần edit nhiều, brand voice chưa chính xác 100% | Feedback loop: user rate output → AI improve, brand voice fine-tuning |
| **Conversion** | In-app + email | Hết free trial, nhận email "Bạn đã tiết kiệm 15 giờ tuần này" | Cân nhắc, thấy giá trị rõ ràng 💰 | Giá có phù hợp budget SME? | Show ROI: "299K/tháng = tiết kiệm 60 giờ = 15M tiền nhân sự" |
| **Retention** | In-app + email | Dùng hàng ngày, train brand voice, thử templates mới | Không thể thiếu, đã thành workflow 🔄 | Content bắt đầu lặp pattern → cần variety | New templates monthly, AI model updates, seasonal content packs |
| **Advocacy** | Facebook, LinkedIn, word of mouth | Recommend cho bạn bè marketer, viết review | Tự hào đã tìm được tool tốt 🌟 | Không có incentive để refer | Referral program: mời bạn → cả hai nhận 1 tháng free |

### Các khoảnh khắc quan trọng

- **Aha Moment**: Khi user generate bài blog đầu tiên và thấy chất lượng "80% done" — chỉ cần edit nhẹ là publish được
- **Moment of Truth**: Cuối free trial — user có thấy đủ giá trị để trả tiền không?
- **Churn Triggers**:
  - Output quality giảm hoặc lặp lại sau 1-2 tháng
  - Brand voice không chính xác → user phải edit nhiều → mất lợi thế tốc độ
  - Competitor (ChatGPT) cải thiện tiếng Việt → "free is good enough"

### Cải thiện ưu tiên

1. **Quick win**: First-run experience — template curated theo ngành, output chất lượng cao ngay lần đầu
2. **Quick win**: ROI calculator trong trial: "Tuần này bạn đã tạo X bài, tiết kiệm Y giờ, trị giá Z VNĐ"
3. **Đầu tư lớn**: Brand voice accuracy — quyết định retention dài hạn
4. **Đầu tư lớn**: Content variety — AI không lặp pattern, luôn fresh

---

## 10. North Star Metric

### Phân loại Business Game
ViếtAI thuộc **Productivity Game** — giúp người dùng tạo content hiệu quả hơn, nhanh hơn.

### North Star Metric

> **Weekly Active Creators (WAC)** — Số người dùng tạo ≥ 1 content piece (bất kỳ loại nào) trong 7 ngày qua

**Tại sao WAC?**

| Tiêu chí | Đánh giá |
|----------|----------|
| Dễ hiểu | ✅ "Người dùng tạo content hàng tuần" — ai cũng hiểu |
| Customer-centric | ✅ Phản ánh giá trị cốt lõi: user đang dùng AI để tạo content |
| Sustainable value | ✅ Tạo content hàng tuần = tool đã trở thành phần workflow |
| Vision alignment | ✅ "Giúp mọi marketer VN tạo content chuyên nghiệp" = họ phải thực sự tạo content |
| Quantitative | ✅ Đo chính xác từ database |
| Actionable | ✅ Cải thiện qua templates, quality, UX, onboarding |
| Leading indicator | ✅ WAC tăng → retention tăng → conversion tăng → revenue tăng |

### Input Metrics (Chỉ số đầu vào)

| Input Metric | Mô tả | Tác động lên WAC |
|-------------|--------|-------------------|
| **Activation Rate** | % new users tạo ≥ 3 content pieces trong tuần đầu | Activated users có 4x khả năng trở thành WAC |
| **Avg. Content Pieces/Week** | Số content trung bình/user/tuần | Nhiều content hơn → engagement sâu hơn → sticky |
| **Content Quality Score** | Rating trung bình user cho output (1-5) | Quality cao → user tin tưởng → dùng tiếp |
| **Template Usage Rate** | % content tạo từ templates vs blank | Templates giảm friction → tăng frequency |
| **Brand Voice Adoption** | % users đã setup brand voice | Brand voice → output relevant hơn → satisfaction cao hơn |

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
   │ Activation  │    │ Content       │    │ Brand Voice   │
   │ Rate        │    │ Quality Score │    │ Adoption      │
   └─────────────┘    └───────────────┘    └───────────────┘
          │                    │                     │
   ┌──────┴──────┐    ┌───────┴───────┐    ┌───────┴───────┐
   │ Template    │    │ Avg Content   │    │ Premium       │
   │ Usage Rate  │    │ Pieces/Week   │    │ Conversion    │
   └─────────────┘    └───────────────┘    └───────────────┘
```

---

## 11. GTM Strategy

### Chiến lược tổng quan
**Approach**: Product-Led Growth (PLG) + Community-Led Growth + Partnership-Led Growth
**Thị trường đầu tiên**: HCM + Hà Nội, SME marketing teams và freelance copywriters

### Messaging chính
> "Viết content tiếng Việt chuyên nghiệp trong 1 phút. Không cần prompt. Không cần edit nhiều. Chỉ cần chọn template và generate."

### Phase 1: Pre-Launch — Xây dựng waitlist & community (T-3 → T0)

| Kênh | Hoạt động | Mục tiêu |
|------|-----------|----------|
| Facebook Groups | Tham gia 20+ groups marketing VN, chia sẻ tips content + soft mention ViếtAI | 2K waitlist signups |
| LinkedIn VN | Founder content: hành trình xây dựng AI writing tool cho VN | 5K followers, 1K waitlist |
| Blog SEO | 20 bài blog: "Cách viết content...", "AI tools cho marketer VN" | Rank 10 keywords, 3K organic visits/tháng |
| Webinar series | "AI Content Marketing 2026" — 4 webinars miễn phí | 500 attendees, 300 waitlist |
| Beta program | 500 beta users (marketers, freelancers, agencies) | Product feedback, testimonials |
| KOL seeding | Gửi beta cho 30 marketing KOLs/educators | 30 authentic reviews ready for launch |

### Phase 2: Launch (T0 → T+2 tháng)

| Kênh | Hoạt động | Budget allocation |
|------|-----------|-------------------|
| Facebook/Instagram Ads | Video ads: "Viết blog SEO trong 2 phút" demo thực tế | 25% |
| KOL Campaign | 10 macro KOLs (marketing educators) + 30 micro KOLs review | 20% |
| Product Hunt VN | Launch trên Product Hunt + các cộng đồng tech VN | 5% |
| PR & Media | Bài viết trên Vietcetera, CafeBiz, GenK, Brands Vietnam | 10% |
| Referral Program | "Mời bạn → cả hai nhận 1 tháng Pro miễn phí" | 10% |
| Partnership Launch | Co-marketing với Haravan, Sapo (e-commerce platforms VN) | 15% |
| SEO & Content | Tiếp tục blog SEO + case studies từ beta users | 10% |
| Community | Facebook Group "ViếtAI Community" — tips, templates, Q&A | 5% |

### Phase 3: Growth (T+2 → T+12 tháng)

| Kênh | Hoạt động |
|------|-----------|
| Viral loops | "Powered by ViếtAI" watermark trên free content → organic discovery |
| Template marketplace | User-generated templates → community grows itself |
| Agency partner program | Agencies nhận commission khi refer clients → channel sales |
| Education partnerships | Hợp tác với khóa học marketing (CASK, AIM Academy, Tomorrow Marketers) |
| E-commerce integrations | Plugin cho Haravan, Sapo, KiotViet → reach 100K+ merchants |
| Enterprise sales | Outbound cho doanh nghiệp lớn: ngân hàng, bất động sản, FMCG |
| International expansion | Mở rộng sang SEA: Thailand, Indonesia (T+12 → T+18) |

### Partnerships chiến lược

| Partner | Giá trị cho ViếtAI | Giá trị cho Partner |
|---------|---------------------|---------------------|
| Haravan/Sapo | Reach 100K+ e-commerce merchants | Thêm giá trị cho platform, giảm churn |
| CASK/AIM Academy | Reach 10K+ marketing students/professionals | Content tool cho học viên, co-branded courses |
| Brands Vietnam | PR + credibility trong marketing community | Exclusive content, sponsored features |
| Zalo Business | Distribution qua Zalo OA ecosystem | AI content cho 50K+ Zalo OA accounts |

### KPI Targets

| Metric | T+1 tháng | T+3 tháng | T+6 tháng | T+12 tháng |
|--------|-----------|-----------|-----------|------------|
| Registered users | 5K | 20K | 50K | 120K |
| WAC (North Star) | 1K | 5K | 15K | 40K |
| Paying users | 200 | 1.5K | 5K | 12K |
| MRR | 30M VNĐ | 200M VNĐ | 500M VNĐ | 1.5B VNĐ |
| Premium conversion | 4% | 7.5% | 10% | 10% |
| CAC | 300K VNĐ | 200K VNĐ | 150K VNĐ | 120K VNĐ |
| M3 Retention (paid) | — | 35% | 40% | 45% |
| NPS | 35 | 40 | 45 | 50 |

### Rủi ro và giảm thiểu

| Rủi ro | Xác suất | Impact | Giảm thiểu |
|--------|----------|--------|------------|
| ChatGPT cải thiện tiếng Việt đáng kể | Cao | Cao | Differentiate bằng templates, SEO, brand voice, workflow — không cạnh tranh ở "AI quality" mà ở "productivity platform" |
| AI Hay mở rộng sang content marketing | Trung bình | Cao | First-mover advantage trong segment chuyên content, build switching costs qua brand voice data |
| Output quality không đủ tốt cho production | Trung bình | Rất cao | Invest mạnh vào fine-tuning, human-in-the-loop QC, feedback loop liên tục |
| Giá quá cao cho thị trường VN | Trung bình | Cao | Freemium generous, pricing A/B test, ROI messaging rõ ràng |
| API costs tăng (OpenAI/Anthropic tăng giá) | Thấp | Trung bình | Diversify: fine-tune open-source models (Llama, Qwen), hybrid approach |
| Quy định về AI content tại VN | Thấp | Trung bình | Compliance team, content disclaimer, transparency về AI-generated content |

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

### Điểm khác biệt cốt lõi của ViếtAI so với Writesonic

| Yếu tố | Writesonic | ViếtAI |
|---------|-----------|--------|
| Ngôn ngữ chính | English-first, multi-language | Vietnamese-first, hiểu ngữ cảnh văn hóa VN |
| Templates | Global templates | Templates cho kênh VN: Shopee, Zalo OA, Facebook VN |
| SEO | Global SEO | SEO tiếng Việt, Google VN |
| Giá | $10-49/tháng (~250K-1.2M VNĐ) | 99K-299K/tháng |
| Brand Voice | English-trained | Hiểu tone miền Bắc/Nam, formal/Gen Z, ngành hàng VN |
| E-commerce | Amazon, Shopify | Shopee, Lazada, TikTok Shop, Haravan, Sapo |
| Support | English | Tiếng Việt, chat, Zalo |

> Tài liệu này là living document — cần được cập nhật liên tục dựa trên data thực tế từ beta users và sau khi launch.
