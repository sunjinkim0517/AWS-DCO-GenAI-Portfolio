# 📋 DCO 교육용 샘플 로그 분석 보고서

이 보고서는 AWS DCO 인턴십 직무 이해를 돕기 위해 교육용 샘플 로그를 분석하여 작성된 인시던트 요약본입니다.
*(실제 AWS 내부 시스템 로그가 아니며 가상 시스템 데이터입니다.)*

## 1. 전체 로그 분석 요약
- **총 로그 줄 수**: 140 줄

## 2. 심각도별 로그 분포
| 심각도 (Severity) | 개수 (Count) | 비율 (Percentage) |
| --- | --- | --- |
| **ERROR** | 2개 | 1.4% |
| **INFO** | 135개 | 96.4% |
| **WARNING** | 3개 | 2.1% |

## 3. 주요 이벤트별 로그 발생 건수
| 이벤트명 (Event) | 발생 건수 |
| --- | --- |
| Normal heartbeat | 125개 |
| Ticket opened | 3개 |
| Ticket escalated | 3개 |
| Maintenance completed | 3개 |
| Fan Alert | 1개 |
| Temperature warning | 1개 |
| SSD failure warning | 1개 |
| CRC error 증가 | 1개 |
| Link Down | 1개 |
| Link Up | 1개 |

## 4. WARNING 및 CRITICAL 로그 상세 리스트
| 발생 시간 | 장비명 (Device) | 등급 | 이벤트 | 상세 메시지 |
| --- | --- | --- | --- | --- |
| 2026-07-03 01:05:00 | `DEMO_CORE_SW_02` | **WARNING** | Fan Alert | Fan module 2 RPM dropped to 15% (Below threshold 20%). IP: 198.51.100.2 |
| 2026-07-03 02:05:00 | `EDU_SRV_R04_N12` | **WARNING** | Temperature warning | Chassis temperature reached 42C (Threshold: 40C). IP: 192.0.2.12 |
| 2026-07-03 03:05:00 | `SAMPLE_TOR_SW_01` | **WARNING** | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |

## 5. 핵심 인시던트 주요 이벤트 요약
이 섹션은 하드웨어 결함이나 장애 전파와 관련된 핵심 키워드(**CRC_ERROR, LINK_DOWN, TICKET_ESCALATED**) 관련 요약입니다.

| 구분 (Category) | 발생 시간 | 장비명 (Device) | 이벤트 | 상세 내용 |
| --- | --- | --- | --- | --- |
| `TICKET_ESCALATED` | 2026-07-03 01:10:00 | `DEMO_CORE_SW_02` | Ticket escalated | Ticket EDU-TKT-2026-0001 escalated to Local Infrastructure Team. |
| `TICKET_ESCALATED` | 2026-07-03 02:15:00 | `EDU_SRV_R04_N12` | Ticket escalated | Ticket EDU-TKT-2026-0002 escalated to DCO Hardware Support. |
| `CRC_ERROR` | 2026-07-03 03:05:00 | `SAMPLE_TOR_SW_01` | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| `LINK_DOWN` | 2026-07-03 03:06:00 | `SAMPLE_TOR_SW_01` | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |
| `TICKET_ESCALATED` | 2026-07-03 03:12:00 | `SAMPLE_TOR_SW_01` | Ticket escalated | Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team. |
| `CRC_ERROR` | 2026-07-03 03:30:00 | `SAMPLE_TOR_SW_01` | Normal heartbeat | System status is healthy. Interface Gi0/1 running with 0 CRC errors. IP: 192.0.2.1 |

---
*분석 완료 시간: 2026-07-19 (DCO 인턴십 교육용 자동 분석 보고서)*
