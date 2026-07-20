# 🚀 AWS-DCO-GenAI-Portfolio

> **AWS DCO (Data Center Operations) 인턴십 대비 생성형 AI 활용 및 엔지니어링 실습 포트폴리오**
> 
> *본 저장소는 비전공자(분자생물학 전공 → IT Data Center Operations 전환) 출신으로서 데이터센터 인프라 운영 지식을 습득하고, Antigravity CLI(`agy`) 등 생성형 AI 도구를 활용하여 로그 분석, 장애 보고서 작성, 티켓 트리아지(Triage) 및 인수인계(Handover) 실습을 수행한 학습 기록입니다.*

---

## 📌 1. 포트폴리오 핵심 학습 철학 (Human-in-the-Loop)

- **AI는 보조 도구, 판단은 엔지니어의 몫**: AI(Antigravity CLI)가 작성한 초안을 수동적으로 수용하지 않고, 로그 기반의 **확인된 사실(Fact)**과 **추정/가설(Hypothesis)**을 엄격하게 분리하여 직접 검증하고 교정합니다.
- **실무 언어의 체득과 도메인 맥락 이해**: PDU, UPS, N+1 이중화, ToR Switch, Link Flap, DOM 광파워 등 데이터센터 현장 용어를 직접 다루며 SOP 및 Incident 처리 프로세스를 주도적으로 소화합니다.
- **안전한 학습 환경 준수**: 모든 예시 데이터는 `SAMPLE`, `DEMO`, `EDU` 등의 접두어가 붙은 가상의 교육용 데이터로 구성하여 실제 AWS 내부 시스템, 보안 및 고객 정보 유출 위험을 철저히 차단하였습니다.

---

## 📂 2. 폴더 구조 및 차시별 산출물

| 폴더명 | 주요 역할 및 나만의 언어로 정리한 핵심 내용 | 대표 파일 |
| :--- | :--- | :--- |
| [`01_dco_glossary/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/01_dco_glossary) | DCO 용어집: PDU, UPS, N+1 이중화, ToR Switch, CRC Error 등 인프라 핵심 용어를 엔지니어 관점으로 정돈 | `dco_glossary.md` |
| [`02_dco_profile/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/02_dco_profile) | 협업 역량 리포트: 나의 강점(분석적 사고)을 DCO Ticket, SOP, SLA, Escalation 절차와 연계하여 나만의 언어로 서술 | `dco_profile.md` |
| [`03_sop_analysis/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/03_sop_analysis) | SOP 분석: 가상의 표준 운영 절차서(SOP)를 목적·단계별 조치·주의사항으로 해부하고 현장 체크리스트로 재구성 | `sop_checklist.md` |
| [`03_star_interview/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/03_star_interview) | STAR 인터뷰: Amazon Leadership Principles 연계 30초 자기소개 및 문제 해결 사례 정리 | `star_interview.md` |
| [`04_environment_setup/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/04_environment_setup) | 환경 구축 기록: Git/GitHub, Python, CLI 자동화 도구 환경 설정 내역 | `setup_guide.md` |
| [`05_antigravity_cli/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/05_antigravity_cli) | AI CLI 활용: Antigravity CLI(`agy`) 명령 체계 학습 및 템플릿 검증 | `agy_cli_check.md` |
| [`06_cli_file_automation/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/06_cli_file_automation) | 파일 자동화: CLI 스크립트를 통한 랙 상태 점검표 및 티켓 서식 자동 생성 | `rack_checklist.md`, `sample_ticket.md` |
| [`07_log_analysis_script/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/07_log_analysis_script)<br>[`09_log_analysis_script/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/09_log_analysis_script) | 로그 분석 파이프라인: `sample_dco_log.txt` (140줄) 자동 파싱 스크립트 작성 및 이상 징후 요약 | `analyze_logs.py`, `sample_dco_log.txt`, `incident_summary.md` |
| [`10_incident_analysis/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/10_incident_analysis) | 장애 심층 분석: CRC Error 급증 및 Link Down 장애에 대한 원인 가설(케이블 손상, 오염, SFP 접촉) 도출 | `crc_Iinkdown_analysis.md` |
| [`11_incident_report/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/11_incident_report) | 인시던트 보고서 및 자동 검증: 11개 구조 Incident Report 작성, Python 자동 검증 스크립트 및 1분 브리핑 양식 구축 | `dco_incident_report.md`, `check_incident_report.py`, `one_minute_briefing.md` |
| [`12_ticket_triage_handover/`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/12_ticket_triage_handover) | 티켓 트리아지 및 인수인계: 복수 장애 발생 시 서비스 영향도(Blast Radius) 중심 우선순위 매트릭스 및 Handover Memo 작성 | `sample_shift_handover_log.txt`, `ticket_priority_matrix.csv`, `shift_handover.md` |
| [`CAREER_JOB_PREP.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/CAREER_JOB_PREP.md) | 생성형 AI 취업 준비 프로젝트: 채용공고 분석, 경험-역량 매칭, STAR 경험 카드 5종 및 AI 모의 면접 준비 서식 | `CAREER_JOB_PREP.md` |


---

## 🔍 3. AI(Antigravity CLI `agy`) 활용 및 검증 회고 (Human-in-the-Loop)

#### 1) 사용한 도구
- **Antigravity CLI (`agy`)**

#### 2) AI가 생성한 내용 중 발견한 오류 또는 부족한 점
1. **단순 Severity 및 텍스트 상태 추종으로 인한 리스크 미평가**:
   - AI는 로그의 `ERROR` / `WARNING` 심각도 라벨 및 타임스탬프 순서에 의존하는 경향이 있어, 실제 서버 2대 차단(Actual Outage)이 발생했던 `EDU-TKT-2026-0201`(포트 Link Down)과 이중화 전원으로 서비스 중단이 없었던 `EDU-TKT-2026-0202`(PDU 전압 경고)의 **실제 가용성 비즈니스 임팩트 차이**를 정밀하게 가중치 반영하지 못하는 한계가 있었습니다.
2. **복구 후 간헐적 재발(Link Flap)의 위험도 저평가**:
   - `0201` 티켓 포트가 06:48에 `LINK_UP` 되었으나, 이후 07:05에 `LINK_FLAP_DETECTED`가 1회 추가 기록된 **간헐적 장애 재발 상태**를 단순히 "복구됨" 상태로 축약할 위험이 있었습니다.
3. **다음 담당자 Action Item의 구체성 부족**:
   - AI는 "원인 미확인"을 단순히 텍스트상으로 나열하는 데 그치고, 다음 담당자가 현장에서 즉시 확인해야 할 **구체적 실계측 항목**(예: DOM 광파워 모니터링 로그, 시설팀 PDU 입력 전압 측정값 대조 등)을 능동적으로 제시하지 못했습니다.

#### 3) AI 결과에서 원본 자료와 다르거나 설명이 부족했던 부분
1. **이중화(Redundancy) 가동 상태의 맥락 구분 부족**:
   - 원본 로그에는 PDU 경고 시 `Feed B` 잉여 전원 동작 및 SSD 경고 시 `Storage Mirror`가 정상 작동 중임이 명시되어 있었으나, AI 초안에서는 서비스 상태가 장애 상황인 것처럼 오인될 수 있게 경고 위주로 단락화되는 설명의 부족함이 있었습니다.
2. **영향 범위(Blast Radius)의 정량적 비교 미비**:
   - 원본 로그의 "영향 서버 2대(포트 장애)"와 "영향 가능 서버 6대(PDU 전압 지속 경고)" 간의 수치적 영향 범위를 우선순위 판단 근거로 체계적으로 연결해 주는 설명이 부족하여 엔지니어의 직접적인 판단 보완이 필요했습니다.
3. **가설(Hypothesis)과 사실(Fact)의 엄격한 분리 부족**:
   - AI는 조치 로그 문구를 바탕으로 원인을 단정 지으려는 경향을 보였으나, 로그만으로는 파이버 피복 꺾임이나 커넥터 오염 등 **근본 원인(Root Cause)을 확정할 수 없으므로 가설 단계로 명시해야 함**을 엔지니어가 직접 재검토하고 보완했습니다.

---

## 🤖 4. 생성형 AI 활용 원칙 (Generative AI Principles)

- **초안 검토 원칙**: 생성형 AI의 답변은 최종 정답이 아니라 검토가 필요한 초안으로 사용했습니다.
- **원본 로그 비교**: AI가 작성한 장비명, 시간, Ticket ID와 사건 내용을 원본 로그와 1:1로 직접 대조하고 비교했습니다.
- **사실과 추정의 분리**: 로그에서 직접 확인되는 사실(Fact)과 가능한 추정/가설(Hypothesis)을 엄격하게 구분했습니다.
- **근본 원인 확정 금지**: 로그만으로 확인할 수 없는 근본 원인(Root Cause)은 임의로 확정하지 않았습니다.
- **주체적 우선순위 판단**: Ticket 우선순위는 AI가 대신 결정하지 않고, 엔지니어가 비즈니스 영향도와 근거를 비교하여 직접 판단했습니다.
- **보안 가이드라인 준수**: 실제 계정 정보, 실제 장비 정보, 실제 Ticket과 실제 AWS 내부 정보를 AI에 입력하지 않았습니다.
- **교육용 데이터 구성**: 모든 로그, 장비명, Ticket ID와 IP 주소는 공개 학습용 샘플 데이터로 구성했습니다.

---

## 🎯 5. 실제 실습을 통해 배운 점 (Learnings & Takeaways)

1. **생성형 AI의 생산성과 파이프라인 가속화**: 생성형 AI를 활용하면 로그 요약, Python 코드 작성과 Incident Report 초안 작성 시간을 획기적으로 줄일 수 있습니다.
2. **인간 주도 검증(Human-in-the-Loop)의 필수성**: AI가 빠르게 결과를 생성하더라도 원본 자료와 비교하는 검증 과정이 반드시 필요함을 실감했습니다.
3. **로그 분석 시 3가지 요소의 명확한 구분**: 로그 분석에서는 **확인된 사실(Fact)**, **가능한 추정(Hypothesis)**과 **미확인 정보(Missing Info)**를 명확히 구분해야 합니다.
4. **복구(Recovery)와 근본 원인(Root Cause)의 독립성**: 장애가 복구되었다는 사실만으로 정확한 Root Cause가 확인된 것은 아니며, 재발 가능성에 대한 모니터링이 이어져야 함을 배웠습니다.
5. **Severity와 Priority의 체계적 차이**: `Severity`는 사건의 기술적 심각도이고, `Priority`는 "무엇을 먼저 확인할 것인지" 정한 엔지니어링 처리 순서입니다.
6. **다각적 Ticket 우선순위 결정 기준**: Ticket 우선순위는 서비스 영향, 반복·지속 여부, 영향 범위(Blast Radius), 복구 여부와 현재 상태를 함께 종합적으로 고려해야 합니다.
7. **Incident Report와 Handover Memo의 목적**: Incident Report는 사건의 흐름과 조치 결과를 체계적으로 공유하기 위함이며, Handover Memo는 교대 전에 진행 중인 상황과 차기 확인 사항을 다음 담당자에게 명확히 전달하기 위해 작성합니다.
8. **과정(Process) 중심 기록의 기술 가치**: 단순 기술 결과물뿐만 아니라 **AI를 어떤 목적으로 사용하고, 무엇을 직접 검증하고 수정했는지**를 투명하게 기록하는 것이 엔지니어로서의 진정한 역량입니다.

---

## 🔒 6. 보안 및 교육용 데이터 사용 준수 안내

- 저장소 내 모든 시스템명, IP 주소, 티켓 ID는 `SAMPLE_TOR_SW_03`, `EDU-TKT-2026-0201`, `192.0.2.1` 등 가상의 서식으로 변경되어 있습니다.
- 실제 데이터센터 장비 조작 명령어나 비밀번호, API Key 등 보안 민감 파일은 포함되어 있지 않으며 `.gitignore`를 통해 엄격히 관리됩니다.
- 본 저장소는 AWS DCO 직무 이해 및 인프라 운영 논리 체득을 목적으로 한 개인 학습용 포트폴리오입니다.
