# MoneyZ — Full Product Management Flow
## Ứng dụng quản lý tài chính cá nhân cho Gen Z Việt Nam

> Tài liệu này trình bày toàn bộ quy trình PM từ nghiên cứu thị trường → chiến lược sản phẩm → thực thi → go-to-market cho sản phẩm MoneyZ.

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

Thị trường ứng dụng quản lý tài chính cá nhân tại Việt Nam đang tăng trưởng mạnh nhờ:
- Tỷ lệ smartphone penetration đạt ~75% dân số
- Gen Z (18-27 tuổi) chiếm ~25% dân số, là thế hệ digital-native đầu tiên
- Thanh toán không tiền mặt tăng trưởng >30%/năm
- Nhận thức về quản lý tài chính cá nhân ngày càng cao qua mạng xã hội

### 5 đối thủ trực tiếp

#### 1. Money Lover
- **Thành lập**: 2013, Finsify (Việt Nam)
- **Người dùng**: >10 triệu downloads toàn cầu
- **Thế mạnh**: Giao diện tiếng Việt tốt, đa nền tảng, tính năng ví chia sẻ, liên kết ngân hàng
- **Điểm yếu**: UI cũ, không gamification, thiếu nội dung giáo dục tài chính, quảng cáo nhiều ở bản miễn phí
- **Giá**: Freemium, Premium ~79.000đ/tháng
- **Mối đe dọa**: Brand awareness cao nhất tại VN, user base lớn

#### 2. MISA (amis.vn / MISA MoneyKeeper)
- **Thành lập**: 1994, MISA JSC (Việt Nam)
- **Người dùng**: >5 triệu downloads
- **Thế mạnh**: Hệ sinh thái kế toán mạnh, tích hợp hóa đơn điện tử, báo cáo chi tiết
- **Điểm yếu**: Giao diện phức tạp, hướng đến người dùng lớn tuổi hơn, thiếu tính social
- **Giá**: Miễn phí với quảng cáo
- **Mối đe dọa**: Uy tín thương hiệu trong lĩnh vực tài chính

#### 3. Mint / Credit Karma (Intuit)
- **Thành lập**: 2006, Mỹ (đã merge vào Credit Karma)
- **Người dùng**: >30 triệu (toàn cầu)
- **Thế mạnh**: Auto-sync ngân hàng, credit score, AI insights
- **Điểm yếu**: Không hỗ trợ ngân hàng VN, giao diện tiếng Anh, không phù hợp văn hóa chi tiêu VN
- **Giá**: Miễn phí (monetize qua referral tài chính)
- **Mối đe dọa**: Thấp tại VN do thiếu localization

#### 4. Toshl Finance
- **Thành lập**: 2010, Slovenia
- **Người dùng**: >2 triệu downloads
- **Thế mạnh**: UI đẹp, data visualization tốt, đa tiền tệ
- **Điểm yếu**: Không tiếng Việt, giá cao cho thị trường VN, không tích hợp ngân hàng VN
- **Giá**: Pro ~$2.99/tháng
- **Mối đe dọa**: Thấp, niche player

#### 5. Sổ Thu Chi (Monefy alternatives VN)
- **Thành lập**: Nhiều app nhỏ lẻ của dev VN
- **Người dùng**: ~500K-1M mỗi app
- **Thế mạnh**: Đơn giản, nhẹ, miễn phí, tiếng Việt
- **Điểm yếu**: Tính năng hạn chế, không cloud sync, thiếu insights, UX kém
- **Giá**: Miễn phí hoặc one-time purchase
- **Mối đe dọa**: Cạnh tranh ở phân khúc "đủ dùng"

### Cơ hội khác biệt hóa cho MoneyZ

| Yếu tố | Đối thủ hiện tại | Cơ hội MoneyZ |
|---------|-------------------|---------------|
| Gamification | Hầu như không có | Streak, badges, challenges tài chính |
| Social/Community | Rất hạn chế | Chia sẻ mục tiêu tiết kiệm, thử thách nhóm |
| Giáo dục tài chính | Không có hoặc rời rạc | Content ngắn kiểu TikTok, tips hàng ngày |
| UX cho Gen Z | Giao diện truyền thống | UI hiện đại, dark mode, stickers, reactions |
| AI Insights | Cơ bản | Dự đoán chi tiêu, gợi ý tiết kiệm cá nhân hóa |

---

## 2. Ước tính quy mô thị trường

### Định nghĩa thị trường
- **Vấn đề**: Gen Z Việt Nam thiếu công cụ quản lý tài chính phù hợp với hành vi và văn hóa chi tiêu của họ
- **Phạm vi**: Việt Nam, người dùng 18-27 tuổi, sử dụng smartphone

### TAM (Total Addressable Market)

**Top-down:**
- Dân số VN: ~100 triệu
- Gen Z (18-27): ~22 triệu người
- Tỷ lệ smartphone: ~75% → 16.5 triệu người
- Thị trường app tài chính cá nhân toàn cầu: ~$1.5B (2025), VN chiếm ~1.5%
- **TAM ≈ $22.5M/năm (~560 tỷ VNĐ)**

**Bottom-up:**
- 16.5 triệu Gen Z có smartphone
- Giả sử ARPU (doanh thu trung bình/user/năm) = $1.5 (mix free + premium)
- **TAM ≈ $24.75M/năm (~620 tỷ VNĐ)**

### SAM (Serviceable Addressable Market)

- Gen Z có thu nhập (đi làm hoặc part-time): ~60% → 9.9 triệu
- Quan tâm đến quản lý tài chính: ~40% → 3.96 triệu
- **SAM ≈ $5.94M/năm (~150 tỷ VNĐ)** (~24% TAM)

### SOM (Serviceable Obtainable Market)

- Năm 1-3: Mục tiêu 5-8% SAM
- **SOM ≈ $300K-475K/năm (~7.5-12 tỷ VNĐ)**
- Tương đương ~200K-320K active users

### Bảng tổng hợp

| Metric | Ước tính hiện tại | Dự báo 3 năm |
|--------|-------------------|---------------|
| TAM | $23M (~575 tỷ VNĐ) | $35M (~875 tỷ VNĐ) |
| SAM | $5.9M (~150 tỷ VNĐ) | $10M (~250 tỷ VNĐ) |
| SOM | $400K (~10 tỷ VNĐ) | $1.5M (~37 tỷ VNĐ) |

### Giả định chính
1. Tỷ lệ chuyển đổi Premium ~5-8% (confidence: medium)
2. ARPU tăng theo thời gian nhờ tính năng mới (confidence: medium)
3. Thị trường fintech VN tiếp tục tăng trưởng >20%/năm (confidence: high)

---

## 3. Phân khúc thị trường

### Segment 1: "Sinh viên tự lập" (35% thị trường)
- **Demographics**: 18-22 tuổi, sinh viên đại học, sống xa nhà
- **Thu nhập**: 2-5 triệu/tháng (trợ cấp gia đình + part-time)
- **JTBD**: "Khi tôi nhận tiền trợ cấp hàng tháng, tôi muốn biết mình có thể chi bao nhiêu mỗi ngày để không hết tiền trước cuối tháng"
- **Pain points**: Hết tiền giữa tháng, không biết tiền đi đâu, ngại ghi chép
- **Product fit**: Cao — cần công cụ đơn giản, miễn phí, gamification để tạo thói quen

### Segment 2: "Người đi làm đầu tiên" (40% thị trường)
- **Demographics**: 22-27 tuổi, mới đi làm 1-3 năm
- **Thu nhập**: 8-20 triệu/tháng
- **JTBD**: "Khi tôi bắt đầu có lương, tôi muốn tiết kiệm được ít nhất 20% thu nhập để có quỹ khẩn cấp và đầu tư"
- **Pain points**: Chi tiêu lifestyle creep, không có kế hoạch tài chính, FOMO mua sắm
- **Product fit**: Rất cao — sẵn sàng trả phí, cần insights và mục tiêu tiết kiệm

### Segment 3: "Freelancer/Creator" (15% thị trường)
- **Demographics**: 20-27 tuổi, thu nhập không ổn định
- **Thu nhập**: 5-30 triệu/tháng (biến động)
- **JTBD**: "Khi thu nhập tôi không đều, tôi muốn dự đoán được dòng tiền để biết tháng nào cần tiết kiệm nhiều hơn"
- **Pain points**: Thu nhập bất thường, khó lập ngân sách cố định, trộn lẫn chi phí cá nhân/công việc
- **Product fit**: Trung bình-cao — cần tính năng dự báo và phân loại thu nhập

### Segment 4: "Couple quản lý chung" (10% thị trường)
- **Demographics**: 23-27 tuổi, đang hẹn hò hoặc mới kết hôn
- **Thu nhập**: 15-40 triệu/tháng (tổng 2 người)
- **JTBD**: "Khi chúng tôi muốn tiết kiệm cho mục tiêu chung (du lịch, mua nhà), tôi muốn theo dõi chi tiêu cùng nhau một cách minh bạch"
- **Pain points**: Khó chia sẻ tài chính, thiếu minh bạch, mục tiêu chung không rõ ràng
- **Product fit**: Trung bình — cần tính năng ví chia sẻ và mục tiêu nhóm

---

## 4. User Personas

### Persona 1: Minh — "Sinh viên tự lập"
- **Tuổi**: 20, sinh viên năm 3 ĐH Bách Khoa HCM
- **Thu nhập**: 3.5 triệu/tháng (2.5tr bố mẹ gửi + 1tr gia sư)
- **JTBD chính**: Không hết tiền trước ngày 25 hàng tháng
- **Pain points**:
  1. Hay quên ghi chép chi tiêu, chỉ nhớ khi hết tiền
  2. Chi tiêu impulsive cho trà sữa, ăn ngoài với bạn bè
  3. Không biết cách phân bổ tiền cho từng khoản
- **Desired gains**:
  1. Biết ngay hôm nay còn bao nhiêu tiền có thể chi
  2. Nhận nhắc nhở khi chi tiêu vượt mức
  3. Cảm giác "thành tựu" khi tiết kiệm được
- **Unexpected insight**: Minh sẵn sàng chia sẻ thành tích tiết kiệm lên story Instagram — social proof là động lực lớn hơn cả tiền
- **Product fit**: MoneyZ cần UX cực kỳ nhanh (ghi chi tiêu < 5 giây), gamification mạnh, và tính năng share lên social

### Persona 2: Linh — "Người đi làm đầu tiên"
- **Tuổi**: 24, Marketing Executive tại agency, HN
- **Thu nhập**: 14 triệu/tháng
- **JTBD chính**: Tiết kiệm 30 triệu trong 12 tháng cho quỹ khẩn cấp
- **Pain points**:
  1. Lifestyle creep — lương tăng nhưng tiết kiệm không tăng
  2. Subscription trap (Spotify, Netflix, gym, cloud storage...)
  3. Không biết bắt đầu đầu tư từ đâu
- **Desired gains**:
  1. Dashboard rõ ràng: thu nhập - chi tiêu - tiết kiệm
  2. Gợi ý cắt giảm chi tiêu không cần thiết
  3. Lộ trình tài chính cá nhân hóa
- **Unexpected insight**: Linh tin tưởng gợi ý từ app hơn từ bố mẹ về tài chính — "bố mẹ không hiểu chi phí sống ở HN bây giờ"
- **Product fit**: MoneyZ cần AI insights mạnh, subscription tracker, và savings goal tracking. Linh sẵn sàng trả 49K-79K/tháng cho Premium.

### Persona 3: Đức — "Freelancer/Creator"
- **Tuổi**: 26, Graphic Designer freelance, Đà Nẵng
- **Thu nhập**: 8-25 triệu/tháng (biến động theo dự án)
- **JTBD chính**: Dự đoán dòng tiền 3 tháng tới để biết khi nào cần nhận thêm dự án
- **Pain points**:
  1. Thu nhập không đều, tháng nhiều tháng ít
  2. Trộn lẫn chi phí cá nhân và chi phí công việc (mua font, stock photo...)
  3. Quên invoice khách hàng, bị trễ thanh toán
- **Desired gains**:
  1. Biểu đồ dòng tiền dự báo theo tháng
  2. Tách biệt chi tiêu cá nhân vs công việc
  3. Nhắc nhở thu tiền khách hàng
- **Unexpected insight**: Đức dùng Google Sheets để quản lý tài chính nhưng bỏ cuộc sau 2 tuần mỗi lần — vấn đề không phải thiếu công cụ mà là thiếu automation
- **Product fit**: MoneyZ cần tính năng multi-wallet, income categorization, và cash flow forecast. Đức sẽ trả phí nếu app thực sự giảm thời gian quản lý tài chính.

---

## 5. Value Proposition

### Cho Segment chính: "Người đi làm đầu tiên" (Persona: Linh)

**1. Who (Ai)**
Gen Z Việt Nam (22-27 tuổi) mới đi làm, có thu nhập ổn định lần đầu, muốn xây dựng thói quen tài chính lành mạnh.

**2. Why (Vấn đề)**
Lần đầu có lương nhưng không biết cách quản lý: chi tiêu tăng theo lương (lifestyle creep), không có quỹ khẩn cấp, không biết bắt đầu tiết kiệm/đầu tư từ đâu. Cảm giác "kiếm được tiền nhưng không giữ được tiền".

**3. What Before (Hiện trạng)**
- Dùng ghi chú điện thoại hoặc không ghi chép gì
- Kiểm tra số dư ngân hàng cuối tháng và "shock"
- Thử dùng Money Lover nhưng bỏ vì giao diện nhàm chán, phải nhập thủ công nhiều
- Đọc tips tài chính trên TikTok nhưng không áp dụng được

**4. How (Giải pháp)**
MoneyZ giúp bạn:
- Ghi chi tiêu trong 3 giây với smart categorization
- AI phân tích pattern chi tiêu và gợi ý cắt giảm cụ thể
- Savings challenges với gamification (streak, badges, leaderboard bạn bè)
- Daily spending limit tự động tính dựa trên thu nhập và mục tiêu
- Nội dung giáo dục tài chính ngắn gọn, dễ hiểu, phong cách Gen Z

**5. What After (Kết quả)**
- Biết chính xác tiền đi đâu mỗi tháng
- Tiết kiệm được 15-25% thu nhập một cách tự nhiên
- Có quỹ khẩn cấp sau 6-12 tháng
- Tự tin hơn về tài chính, giảm stress về tiền
- Chia sẻ thành tích với bạn bè, tạo văn hóa tiết kiệm tích cực

**6. Alternatives (Lựa chọn thay thế)**
| Giải pháp | Hạn chế |
|-----------|---------|
| Money Lover | UI cũ, không gamification, thiếu AI insights |
| Google Sheets | Tốn thời gian, dễ bỏ cuộc, không insights |
| Không làm gì | Stress tài chính tăng, không có quỹ khẩn cấp |
| Sổ Thu Chi apps | Quá đơn giản, không motivate |

### Value Proposition Statement
> **MoneyZ giúp Gen Z Việt Nam biến việc quản lý tiền từ "gánh nặng" thành "trò chơi" — ghi chi tiêu trong 3 giây, nhận gợi ý AI cá nhân hóa, và đạt mục tiêu tiết kiệm cùng bạn bè.**

---

## 6. Lean Canvas

| # | Section | Chi tiết |
|---|---------|----------|
| **1** | **Problem** | 1. Gen Z không có thói quen ghi chép chi tiêu (quá nhàm chán) |
| | | 2. Lifestyle creep — lương tăng nhưng tiết kiệm không tăng |
| | | 3. Thiếu kiến thức tài chính cá nhân thực tế |
| **2** | **Solution** | 1. Quick-log chi tiêu < 3 giây + AI auto-categorize |
| | | 2. Smart budget với daily spending limit + savings challenges |
| | | 3. Bite-sized financial tips hàng ngày (60 giây đọc) |
| **3** | **UVP** | "Quản lý tiền như chơi game — 3 giây ghi, AI gợi ý, tiết kiệm cùng bạn bè" |
| **4** | **Unfair Advantage** | Deep localization cho VN (ngân hàng, văn hóa chi tiêu, ngôn ngữ Gen Z), community-driven savings challenges |
| **5** | **Customer Segments** | Primary: Gen Z đi làm (22-27), Secondary: Sinh viên (18-22) |
| | | Early adopters: Gen Z quan tâm tài chính trên TikTok/Instagram |
| **6** | **Channels** | TikTok/Instagram content marketing, KOL tài chính, App Store/Google Play, referral program |
| **7** | **Revenue** | Freemium: Free (basic tracking) → Premium 49K/tháng (AI insights, unlimited goals, no ads) |
| | | Target LTV: 400K-600K VNĐ/user |
| **8** | **Cost Structure** | Fixed: Dev team (5-7 người), cloud infrastructure, content creation |
| | | Variable: Marketing/UA, KOL partnerships, customer support |
| | | CAC target: < 30K VNĐ/user |
| **9** | **Key Metrics** | Activation: Ghi ≥3 giao dịch trong tuần đầu |
| | | Retention: D30 retention ≥ 25% |
| | | Revenue: Premium conversion ≥ 5% |
| | | North Star: Weekly Active Loggers |

---

## 7. PRD — Product Requirements Document

### 1. Summary
MoneyZ là ứng dụng quản lý tài chính cá nhân được thiết kế riêng cho Gen Z Việt Nam. App kết hợp ghi chép chi tiêu nhanh, AI insights, gamification, và tính năng social để biến việc quản lý tiền thành thói quen tích cực.

### 2. Contacts

| Tên | Vai trò | Ghi chú |
|-----|---------|---------|
| [PM Name] | Product Manager | Owner PRD |
| [Design Lead] | UX/UI Designer | Thiết kế giao diện Gen Z |
| [Tech Lead] | Engineering Lead | Kiến trúc hệ thống |
| [Data Lead] | Data Scientist | AI/ML models |
| [Marketing Lead] | Growth Marketing | GTM strategy |

### 3. Background

**Context**: Thị trường fintech VN tăng trưởng >30%/năm. Gen Z chiếm 25% dân số nhưng chưa có app tài chính nào thực sự phục vụ đúng nhu cầu và hành vi của họ. Các app hiện tại (Money Lover, MISA) thiết kế cho người dùng lớn tuổi hơn.

**Why now**:
- Gen Z đầu tiên bắt đầu đi làm và có thu nhập (2022-2026)
- AI/LLM cho phép tạo insights cá nhân hóa với chi phí thấp
- Thanh toán số phổ biến → dữ liệu chi tiêu dễ thu thập hơn
- Xu hướng "financial wellness" trên social media đang peak

### 4. Objective

**Mục tiêu**: Trở thành app quản lý tài chính #1 cho Gen Z Việt Nam trong 18 tháng.

**Key Results (OKR)**:
- KR1: Đạt 200K MAU trong 12 tháng sau launch
- KR2: D30 retention ≥ 25%
- KR3: Premium conversion rate ≥ 5%
- KR4: NPS ≥ 50
- KR5: 4.5+ rating trên App Store/Google Play

### 5. Market Segments

**Primary**: Gen Z đi làm (22-27 tuổi)
- Thu nhập 8-20 triệu/tháng
- Lần đầu quản lý tài chính độc lập
- Digital-native, quen dùng app cho mọi thứ

**Secondary**: Sinh viên tự lập (18-22 tuổi)
- Thu nhập hạn chế, cần quản lý chặt
- Sẵn sàng adopt app mới, viral potential cao

### 6. Value Propositions

- **Job**: Quản lý chi tiêu hàng ngày và tiết kiệm cho mục tiêu
- **Gain**: Tự tin về tài chính, đạt mục tiêu tiết kiệm, cảm giác thành tựu
- **Pain relieved**: Hết stress "tiền đi đâu hết", không còn hết tiền giữa tháng
- **Differentiator**: Gamification + Social + AI — không app nào ở VN kết hợp cả 3

### 7. Solution

#### 7.1 Key Features — MVP (v1.0)

**F1: Quick Log (Core)**
- Ghi chi tiêu trong ≤ 3 giây
- AI auto-categorize (ăn uống, di chuyển, giải trí, mua sắm...)
- Hỗ trợ voice input tiếng Việt
- Scan receipt bằng camera (OCR)

**F2: Smart Dashboard**
- Tổng quan thu-chi-tiết kiệm tháng
- Daily spending limit (tự động tính)
- Biểu đồ chi tiêu theo category
- So sánh tháng này vs tháng trước

**F3: Savings Goals**
- Tạo mục tiêu tiết kiệm (quỹ khẩn cấp, du lịch, mua đồ...)
- Progress bar và milestone celebrations
- Auto-save rules (ví dụ: mỗi lần không mua trà sữa → +25K vào goal)

**F4: Gamification Engine**
- Daily streak ghi chi tiêu
- Badges/achievements (7-day streak, first 1M saved, budget master...)
- Monthly challenges (No Spend Day, 50/30/20 challenge...)
- Share achievements lên Instagram/TikTok

**F5: Financial Tips**
- Daily bite-sized tips (60 giây đọc)
- Personalized dựa trên spending pattern
- Format: cards, short video, infographic

#### 7.2 Features — v2.0 (Post-MVP)
- Liên kết ngân hàng VN (auto-import transactions)
- Social features: savings challenges với bạn bè, leaderboard
- AI financial advisor chatbot
- Investment education & referral
- Subscription tracker
- Cash flow forecast cho freelancers

#### 7.3 Technology
- Mobile: React Native (iOS + Android)
- Backend: Node.js + PostgreSQL
- AI/ML: Python microservices cho categorization & insights
- Cloud: AWS (ap-southeast-1 region cho latency thấp tại VN)

#### 7.4 Assumptions
1. Gen Z sẵn sàng ghi chép chi tiêu nếu UX đủ nhanh và vui (cần validate)
2. Gamification tăng retention đáng kể so với app truyền thống (cần A/B test)
3. 5-8% users sẵn sàng trả 49K/tháng cho Premium (cần validate pricing)
4. AI categorization đạt accuracy ≥ 85% cho chi tiêu VN (cần train model)

### 8. Release Plan

| Phase | Timeline | Scope |
|-------|----------|-------|
| Alpha | T+0 → T+3 tháng | Quick Log + Dashboard + Basic Goals (internal testing) |
| Beta | T+3 → T+5 tháng | + Gamification + Tips (500 beta users) |
| v1.0 Launch | T+5 → T+6 tháng | Full MVP, public launch |
| v1.1 | T+6 → T+9 tháng | Bank linking, social features |
| v2.0 | T+9 → T+12 tháng | AI advisor, investment education |

---

## 8. User Stories

### Epic 1: Quick Log

**Story 1.1: Ghi chi tiêu nhanh**
- **Description**: As a Gen Z user, I want to log an expense in under 3 seconds, so that I don't skip recording because it takes too long.
- **Acceptance Criteria**:
  1. Mở app → màn hình ghi chi tiêu hiển thị ngay (không qua home screen)
  2. Nhập số tiền bằng numpad tùy chỉnh (có nút nhanh: 10K, 20K, 50K, 100K)
  3. AI tự động gợi ý category dựa trên thời gian và số tiền
  4. Swipe hoặc tap để chọn category khác nếu AI sai
  5. Ghi chú tùy chọn (không bắt buộc)
  6. Tap "Done" → lưu thành công với animation nhẹ

**Story 1.2: Voice input chi tiêu**
- **Description**: As a busy user, I want to say "trà sữa 45 nghìn" and have the app record it automatically, so that I can log expenses hands-free.
- **Acceptance Criteria**:
  1. Tap icon microphone trên màn hình Quick Log
  2. Nói tiếng Việt tự nhiên (ví dụ: "ăn trưa 55 nghìn", "grab 32k")
  3. App parse được số tiền và category từ voice
  4. Hiển thị preview để user confirm trước khi lưu
  5. Hỗ trợ các cách nói phổ biến: "nghìn", "k", "triệu"
  6. Xử lý offline với on-device speech recognition

**Story 1.3: Scan receipt**
- **Description**: As a user who shops at stores, I want to scan my receipt to auto-log the expense, so that I get accurate amounts without manual entry.
- **Acceptance Criteria**:
  1. Tap icon camera trên màn hình Quick Log
  2. Chụp hoặc chọn ảnh receipt từ gallery
  3. OCR extract: tổng tiền, ngày, tên cửa hàng
  4. Auto-fill vào form chi tiêu, user review và confirm
  5. Xử lý được receipt tiếng Việt phổ biến (siêu thị, cửa hàng tiện lợi)
  6. Lưu ảnh receipt gốc đính kèm giao dịch

### Epic 2: Smart Dashboard

**Story 2.1: Tổng quan tài chính tháng**
- **Description**: As a user, I want to see my monthly financial overview at a glance, so that I know where I stand financially.
- **Acceptance Criteria**:
  1. Hiển thị: tổng thu nhập, tổng chi tiêu, số tiết kiệm được
  2. Progress bar: % ngân sách đã dùng trong tháng
  3. Daily spending limit còn lại cho hôm nay
  4. Top 3 categories chi tiêu nhiều nhất
  5. So sánh nhanh với tháng trước (↑↓%)
  6. Pull-to-refresh để cập nhật real-time

**Story 2.2: Daily spending limit**
- **Description**: As a user with a savings goal, I want the app to tell me how much I can spend today, so that I stay on track without manual calculation.
- **Acceptance Criteria**:
  1. Tự động tính: (Thu nhập - Tiết kiệm mục tiêu - Chi phí cố định) ÷ Số ngày còn lại
  2. Hiển thị prominently trên dashboard
  3. Màu xanh khi còn nhiều, vàng khi gần hết, đỏ khi vượt
  4. Cập nhật real-time sau mỗi giao dịch
  5. Notification khi chi tiêu vượt 80% limit trong ngày
  6. Cho phép user tùy chỉnh % tiết kiệm mục tiêu

### Epic 3: Savings Goals

**Story 3.1: Tạo mục tiêu tiết kiệm**
- **Description**: As a user, I want to create a savings goal with a target amount and deadline, so that I have clear motivation to save.
- **Acceptance Criteria**:
  1. Nhập: tên mục tiêu, số tiền target, deadline
  2. Chọn icon/emoji cho mục tiêu
  3. App tính số tiền cần tiết kiệm mỗi tháng/tuần
  4. Hiển thị progress bar với % hoàn thành
  5. Hỗ trợ nhiều mục tiêu đồng thời (tối đa 5 ở bản free)
  6. Celebration animation khi đạt milestone (25%, 50%, 75%, 100%)

### Epic 4: Gamification

**Story 4.1: Daily streak**
- **Description**: As a user, I want to maintain a daily logging streak, so that I build a consistent habit of tracking expenses.
- **Acceptance Criteria**:
  1. Streak tăng +1 khi ghi ≥ 1 giao dịch trong ngày
  2. Hiển thị streak count và fire emoji trên dashboard
  3. Streak reset về 0 nếu miss 1 ngày
  4. "Freeze" card: 1 lần/tháng được miss mà không mất streak (Premium)
  5. Milestone badges: 7 ngày, 30 ngày, 100 ngày, 365 ngày
  6. Push notification nhắc nhở lúc 9PM nếu chưa ghi trong ngày

---

## 9. Customer Journey Map

### Persona: Linh (24 tuổi, Marketing Executive)

| Giai đoạn | Touchpoint | Hành động | Cảm xúc | Pain Point | Cơ hội |
|-----------|------------|-----------|---------|------------|--------|
| **Awareness** | TikTok, Instagram | Xem video KOL tài chính review MoneyZ | Tò mò 🤔 | "Lại một app ghi chi tiêu nữa à?" | Content thể hiện sự khác biệt (gamification demo) |
| **Consideration** | App Store, review sites | Đọc review, xem screenshots, so sánh với Money Lover | Quan tâm nhưng hoài nghi 😐 | "Liệu mình có dùng lâu dài không?" | Social proof: "200K Gen Z đang dùng", rating 4.7★ |
| **Acquisition** | App Store download | Tải app, mở lần đầu | Kỳ vọng 😊 | Nếu onboarding dài → bỏ | Onboarding ≤ 3 bước, cho dùng ngay |
| **Onboarding** | In-app | Setup: thu nhập, mục tiêu tiết kiệm, categories | Hơi phiền nhưng hiểu cần thiết 😅 | Form dài, hỏi nhiều thông tin | Progressive onboarding: hỏi ít, learn từ behavior |
| **Aha Moment** | In-app (ngày 2-3) | Ghi 5+ giao dịch, thấy dashboard hiển thị "Hôm nay bạn còn 120K để chi" | Wow, hữu ích thật 😮 | Nếu AI categorize sai nhiều → mất tin tưởng | Đảm bảo AI accuracy ≥ 85%, cho sửa dễ dàng |
| **Engagement** | In-app (tuần 1-4) | Ghi chi tiêu hàng ngày, check streak, đọc tips | Vui, có động lực 😄 | Streak bị reset → frustrated | Streak freeze, encouraging messages khi miss |
| **Retention** | In-app + notifications | Đạt savings milestone, nhận weekly report | Tự hào, motivated 🎉 | Hết nội dung mới, app trở nên nhàm | Monthly challenges mới, seasonal events |
| **Advocacy** | Instagram, word of mouth | Share badge "Tiết kiệm 5 triệu đầu tiên" lên story | Tự hào, muốn khoe 🌟 | Share template xấu → không muốn share | Thiết kế share cards đẹp, on-brand cho Gen Z |

### Các khoảnh khắc quan trọng

- **Aha Moment**: Khi user thấy daily spending limit lần đầu và nhận ra "à, mình chỉ nên chi 150K hôm nay"
- **Moment of Truth**: Cuối tuần đầu tiên — user có quay lại ghi tiếp không?
- **Churn Trigger**: Streak bị reset sau 10+ ngày → cảm giác mất hết progress

### Cải thiện ưu tiên

1. **Quick win**: Onboarding ≤ 3 bước, cho ghi giao dịch đầu tiên trong 30 giây
2. **Quick win**: Share cards đẹp, sẵn template cho Instagram story
3. **Đầu tư lớn**: AI categorization accuracy — quyết định trust của user

---

## 10. North Star Metric

### Phân loại Business Game
MoneyZ thuộc **Productivity Game** — giúp người dùng quản lý tài chính hiệu quả hơn.

### North Star Metric

> **Weekly Active Loggers (WAL)** — Số người dùng ghi ≥ 1 giao dịch trong 7 ngày qua

**Tại sao WAL?**

| Tiêu chí | Đánh giá |
|----------|----------|
| Dễ hiểu | ✅ Ai cũng hiểu "người dùng ghi chi tiêu hàng tuần" |
| Customer-centric | ✅ Phản ánh giá trị thực: user đang dùng app để quản lý tiền |
| Sustainable value | ✅ Ghi chép hàng tuần = thói quen đã hình thành |
| Vision alignment | ✅ "Giúp Gen Z VN quản lý tài chính" = họ phải thực sự dùng app |
| Quantitative | ✅ Đo được chính xác từ database |
| Actionable | ✅ Teams có thể cải thiện qua UX, notifications, gamification |
| Leading indicator | ✅ WAL tăng → retention tăng → revenue tăng |

### Input Metrics (Chỉ số đầu vào)

| Input Metric | Mô tả | Tác động lên WAL |
|-------------|--------|-------------------|
| **Activation Rate** | % new users ghi ≥ 3 giao dịch trong tuần đầu | User activated → likely trở thành WAL |
| **Avg. Transactions/Week** | Số giao dịch trung bình/user/tuần | Nhiều giao dịch hơn → engagement sâu hơn |
| **Streak Retention** | % users duy trì streak ≥ 7 ngày | Streak = habit loop → WAL ổn định |
| **Goal Completion Rate** | % savings goals đạt milestone | Đạt mục tiêu → motivation tiếp tục dùng |
| **D7 Retention** | % users quay lại sau 7 ngày | Trực tiếp đo lường WAL potential |

### Metrics Constellation

```
                    ┌─────────────────────┐
                    │  Weekly Active       │
                    │  Loggers (WAL)       │  ← North Star
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                     │
   ┌──────┴──────┐    ┌───────┴───────┐    ┌───────┴───────┐
   │ Activation  │    │ Streak        │    │ Goal          │
   │ Rate        │    │ Retention     │    │ Completion    │
   └─────────────┘    └───────────────┘    └───────────────┘
          │                    │                     │
   ┌──────┴──────┐    ┌───────┴───────┐    ┌───────┴───────┐
   │ Avg Txn/    │    │ D7            │    │ Premium       │
   │ Week        │    │ Retention     │    │ Conversion    │
   └─────────────┘    └───────────────┘    └───────────────┘
```

---

## 11. GTM Strategy

### Chiến lược tổng quan
**Approach**: Product-Led Growth (PLG) kết hợp Community-Led Growth
**Thị trường đầu tiên**: HCM + Hà Nội (Gen Z đi làm, 22-27 tuổi)

### Phase 1: Pre-Launch (T-2 → T0)

**Xây dựng cộng đồng trước khi launch**

| Kênh | Hoạt động | Mục tiêu |
|------|-----------|----------|
| TikTok | Series "Tiền đi đâu hết?" — content tài chính Gen Z | 500K views, 10K followers |
| Instagram | Infographic tips tài chính, behind-the-scenes build app | 5K followers |
| Waitlist | Landing page "Đăng ký sớm nhận Premium 3 tháng miễn phí" | 5K signups |
| KOL seeding | Gửi beta cho 20 micro-KOL tài chính/lifestyle | 20 authentic reviews |

### Phase 2: Launch (T0 → T+1 tháng)

**Messaging chính**: "Quản lý tiền trong 3 giây. Tiết kiệm như chơi game."

| Kênh | Hoạt động | Budget |
|------|-----------|--------|
| TikTok Ads | Video ads 15-30s, UGC style | 30% budget |
| KOL Campaign | 5 macro + 20 micro KOLs review app | 25% budget |
| App Store Optimization | Keywords: quản lý chi tiêu, tiết kiệm, tài chính cá nhân | 5% budget |
| PR | Bài viết trên Vietcetera, GenK, Cafebiz | 10% budget |
| Referral Program | "Mời bạn, cả hai nhận 1 tháng Premium free" | 15% budget |
| University Campaign | Poster, workshop tài chính tại 10 trường ĐH lớn | 15% budget |

### Phase 3: Growth (T+1 → T+6 tháng)

| Kênh | Hoạt động |
|------|-----------|
| Viral loops | Share savings achievements → bạn bè tải app |
| Content marketing | Blog SEO: "Cách tiết kiệm cho Gen Z", "Quản lý lương đầu tiên" |
| Partnerships | Hợp tác với ngân hàng số (Timo, Cake), ví điện tử (MoMo, ZaloPay) |
| Community | Facebook Group "MoneyZ Community" — chia sẻ tips, challenges |
| Seasonal campaigns | Tết savings challenge, Back-to-school budget, 11.11 spending tracker |

### KPI Targets

| Metric | T+1 tháng | T+3 tháng | T+6 tháng | T+12 tháng |
|--------|-----------|-----------|-----------|------------|
| Downloads | 20K | 80K | 200K | 500K |
| MAU | 10K | 50K | 120K | 300K |
| WAL (North Star) | 5K | 30K | 75K | 200K |
| Premium conversion | 3% | 5% | 6% | 8% |
| CAC | 25K VNĐ | 20K VNĐ | 15K VNĐ | 12K VNĐ |
| NPS | 40 | 45 | 50 | 55 |

### Rủi ro và giảm thiểu

| Rủi ro | Xác suất | Giảm thiểu |
|--------|----------|------------|
| User bỏ sau tuần đầu | Cao | Gamification mạnh, streak system, push notifications thông minh |
| AI categorization kém | Trung bình | Train model với data VN, cho user sửa và learn |
| Cạnh tranh từ Money Lover | Trung bình | Differentiate bằng UX Gen Z + social features |
| Chi phí UA cao | Trung bình | Focus organic/viral growth, referral program |
| Privacy concerns | Thấp | Transparent data policy, on-device processing khi có thể |

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

> Tài liệu này là living document — cần được cập nhật liên tục dựa trên data thực tế sau khi launch.
