---
inclusion: always
---

# PM Skills — Quy tắc tạo file PM Flow

## Quy tắc output file

Khi tạo file PM Flow cho dự án:
- File PHẢI đặt ở workspace root (KHÔNG đặt trong `.kiro/`)
- Tên file: `{TenSanPham}-Full-PM-Flow.md` (PascalCase, không dấu, không khoảng trắng)
- Ví dụ: `MoneyZ-Full-PM-Flow.md`, `EduCareerVN-Full-PM-Flow.md`
- Nếu user yêu cầu đặt ở thư mục khác thì theo user

## Quy tắc đặt tên sản phẩm

- Hỏi user tên sản phẩm TRƯỚC khi bắt đầu viết
- Nếu user chưa có tên, brainstorm 3-5 gợi ý dựa trên mô tả sản phẩm
- Tên sản phẩm phải nhất quán xuyên suốt tài liệu

## Quy tắc research

- Khi user cung cấp URL tham khảo (đối thủ, inspiration), PHẢI fetch và research trước khi viết
- Dùng web search để lấy data thị trường mới nhất (market size, growth rate, competitors)
- Cite sources khi dùng số liệu cụ thể

## Full PM Flow — 11 phần bắt buộc

Khi user yêu cầu "full flow" hoặc "full PM flow", tạo tài liệu với đầy đủ 11 phần theo thứ tự:

```
Phase 1: Market Research
  1. Competitor Analysis — 5 đối thủ, ma trận so sánh, cơ hội khác biệt hóa
  2. Market Sizing — TAM/SAM/SOM (top-down + bottom-up)
  3. Market Segments — 3-5 phân khúc với JTBD
  4. User Personas — 3 personas chi tiết

Phase 2: Strategy
  5. Value Proposition — 6 phần theo JTBD + statement
  6. Lean Canvas — 9 ô đầy đủ

Phase 3: Execution
  7. PRD — 8 sections (Summary, Contacts, Background, Objective, Segments, Value Props, Solution, Release)
  8. User Stories — 3-4 Epics, mỗi epic 2-3 stories với acceptance criteria
  9. Customer Journey Map — 7 giai đoạn (Awareness → Advocacy)

Phase 4: Go-to-Market
  10. North Star Metric — Business game, NSM, 5 input metrics, constellation
  11. GTM Strategy — 3 phases (Pre-launch, Launch, Growth), KPI targets, rủi ro
```

## Danh sách PM Skills có sẵn

### Market Research
| Skill | Trigger |
|-------|---------|
| `competitor-analysis` | "Phân tích đối thủ cho [sản phẩm]" |
| `market-sizing` | "Ước tính thị trường cho [sản phẩm]" |
| `market-segments` | "Phân khúc thị trường cho [sản phẩm]" |
| `user-personas` | "Tạo personas cho [sản phẩm]" |
| `ideal-customer-profile` | "Xác định ICP cho [sản phẩm]" |
| `sentiment-analysis` | "Phân tích sentiment cho [data]" |
| `cohort-analysis` | "Phân tích cohort cho [data]" |

### Strategy
| Skill | Trigger |
|-------|---------|
| `value-proposition` | "Tạo value prop cho [sản phẩm]" |
| `lean-canvas` | "Tạo lean canvas cho [sản phẩm]" |
| `business-model` | "Tạo BMC cho [sản phẩm]" |
| `product-strategy` | "Tạo product strategy cho [sản phẩm]" |
| `product-vision` | "Tạo vision cho [sản phẩm]" |
| `north-star-metric` | "Xác định NSM cho [sản phẩm]" |
| `positioning-ideas` | "Brainstorm positioning cho [sản phẩm]" |
| `pricing-strategy` | "Tạo pricing cho [sản phẩm]" |
| `monetization-strategy` | "Brainstorm monetization cho [sản phẩm]" |

### Discovery & Ideation
| Skill | Trigger |
|-------|---------|
| `interview-script` | "Tạo interview script cho [chủ đề]" |
| `brainstorm-ideas-new` | "Brainstorm ideas cho [sản phẩm mới]" |
| `brainstorm-ideas-existing` | "Brainstorm ideas cho [tính năng]" |
| `brainstorm-experiments-new` | "Brainstorm experiments cho [sản phẩm mới]" |
| `brainstorm-experiments-existing` | "Brainstorm experiments cho [tính năng]" |
| `identify-assumptions-new` | "Xác định assumptions cho [sản phẩm mới]" |
| `identify-assumptions-existing` | "Xác định assumptions cho [tính năng]" |
| `prioritize-assumptions` | "Ưu tiên assumptions cho [danh sách]" |
| `opportunity-solution-tree` | "Tạo OST cho [outcome]" |

### Execution
| Skill | Trigger |
|-------|---------|
| `create-prd` | "Tạo PRD cho [tính năng]" |
| `user-stories` | "Viết user stories cho [tính năng]" |
| `job-stories` | "Viết job stories cho [tính năng]" |
| `wwas` | "Tạo WWAs cho [tính năng]" |
| `test-scenarios` | "Tạo test scenarios cho [story]" |
| `customer-journey-map` | "Tạo journey map cho [persona]" |
| `prioritize-features` | "Ưu tiên features cho [danh sách]" |
| `sprint-plan` | "Lập sprint plan cho [sprint]" |
| `brainstorm-okrs` | "Brainstorm OKRs cho [team]" |
| `metrics-dashboard` | "Thiết kế dashboard cho [sản phẩm]" |

### Go-to-Market
| Skill | Trigger |
|-------|---------|
| `gtm-strategy` | "Tạo GTM cho [sản phẩm]" |
| `gtm-motions` | "Xác định GTM motions cho [sản phẩm]" |
| `beachhead-segment` | "Xác định beachhead cho [sản phẩm]" |
| `growth-loops` | "Thiết kế growth loops cho [sản phẩm]" |
| `marketing-ideas` | "Brainstorm marketing cho [sản phẩm]" |
| `competitive-battlecard` | "Tạo battlecard vs [đối thủ]" |
| `release-notes` | "Viết release notes cho [version]" |

### Analysis & Operations
| Skill | Trigger |
|-------|---------|
| `swot-analysis` | "Phân tích SWOT cho [sản phẩm]" |
| `pestle-analysis` | "Phân tích PESTLE cho [thị trường]" |
| `porters-five-forces` | "Phân tích Porter's cho [ngành]" |
| `pre-mortem` | "Chạy pre-mortem cho [kế hoạch]" |
| `stakeholder-map` | "Tạo stakeholder map cho [dự án]" |
| `retro` | "Chạy retro cho [sprint]" |
| `ab-test-analysis` | "Phân tích A/B test cho [experiment]" |

### Utilities
| Skill | Trigger |
|-------|---------|
| `dummy-dataset` | "Tạo dummy data cho [mô tả]" |
| `sql-queries` | "Viết SQL cho [yêu cầu]" |
| `grammar-check` | "Kiểm tra grammar cho [text]" |
| `draft-nda` | "Soạn NDA giữa [A] và [B]" |
| `privacy-policy` | "Soạn privacy policy cho [sản phẩm]" |

## Cách sử dụng

- Gõ yêu cầu bằng tiếng Việt hoặc tiếng Anh, Kiro tự kích hoạt skill phù hợp
- Full flow: "Chạy full PM flow cho [tên sản phẩm] — [mô tả ngắn]"
- Từng phần: "Phân tích đối thủ cho app giao đồ ăn"
