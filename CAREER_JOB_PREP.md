# 💼 생성형 AI 취업 준비 프로젝트 (DCO / IT 인프라 운영 지원)

> **[안내] 본 문서는 AWS DCO(Data Center Operations) 인턴 및 데이터센터 IT 인프라 운영 지원 직무 진출을 위한 생성형 AI 기반 채용공고 분석, 경험-역량 매칭, STAR 경험 카드 작성 및 AI 모의 면접 대비 통합 가이드 문서입니다.**

---

## 🎯 1단계: 관심 직무 선택

- **선택 직무**: **AWS DCO (Data Center Operations) 인턴 / 데이터센터 IT 인프라 운영 지원**
- **직무 개요**: 데이터센터 내부의 서버, 스위치, 랙(Rack), PDU, UPS 등 물리/네트워크 인프라의 상태를 모니터링하고, SOP에 따른 장애 대응, 티켓 관리(Ticket Triage), 현장 자재 교체 지원 및 교체 시점의 인수인계(Shift Handover) 업무를 수행합니다.

---

## 📋 2단계 & 3단계: 채용공고 분석 및 프롬프트

### 💡 채용공고 분석 코칭 프롬프트

```text
당신은 신입 취업준비생을 돕는 직무 분석 코치입니다.

아래 채용공고를 분석해 주세요.

[분석 항목]
1. 직무명
2. 주요 담당 업무
3. 필수 역량
4. 우대 역량
5. 기술 역량
6. 협업 및 태도 역량
7. 포트폴리오로 증명하면 좋은 항목
8. 면접에서 질문받을 가능성이 높은 항목

[작성 조건]
- 채용공고에 직접 제시된 내용과 추론한 내용을 구분하세요.
- 채용공고에 없는 자격이나 기술을 임의로 추가하지 마세요.
- 신입 지원자가 이해할 수 있는 용어로 설명하세요.

[채용공고]
(공개된 데이터센터 운영지원 / DCO 인턴 채용공고 텍스트)
```

### 📊 채용공고 분석표 (DCO 인턴 / 인프라 운영 지원 예시 분석)

| 구분 | 분석 내용 | 공고 원문 근거 | 추가 확인 필요 (추론/보완) |
| --- | --- | --- | --- |
| **주요 업무** | 서버/네트워크 장비 물리 점검, 장애 티켓 수신 및 1차 대응, 랙 자재 교체 지원 | "데이터센터 인프라 현장점검 및 티켓 기반 장애 조치 지원" | Shift 교체 시 Handover 문서 작성 및 현장 작업 SOP 준수 여부 |
| **필수 역량** | 하드웨어 기본 지식(Server, Switch, PDU), 문제 원인 추론 능력, 교대근무 이해 | "컴퓨터 구조/네트워크 기초 이해, 24/7 교대 근무 가능자" | 데이터센터 인프라 이중화(N+1, Dual Feed) 개념 이해도 |
| **우대 역량** | Linux 기초, Python 스크립트 활용 경험, Git 버전 관리, 네트워크 자격증 | "Linux/Python 활용 경험자 우대, CCNA/네트워크 자격 보유자 우대" | 로그 파싱 자동화 스크립트 작성 및 Git 포트폴리오 유무 |
| **기술 역량** | Python 로그 파싱, Linux CLI 기본 조작, 네트워크 인터페이스(Gi0/1 등) 이해 | "기초 스크립팅 및 네트워크 인터페이스 상태 이해" | CRC Error, Link Flap 등 물리 계층(L1/L2) 장애 모니터링 능력 |
| **협업 역량** | Clear 커뮤니케이션, 정확한 보고서 작성, SOP 표준 절차 준수 | "타 팀(Facilities, Cabling)과의 협업 및 정확한 릴레이 보고" | Incident Report 작성 능력 및 Escalation 판단 기준 |
| **포트폴리오 항목** | 장애 로그 파싱 스크립트, SOP 체크리스트, 장애 대응 보고서, Shift Handover Memo | "실무 관련 프로젝트 및 문제 해결 문서화 경험 제출" | Git 커밋 이력 및 AI 도구 검증 프로세스 기록 |
| **예상 면접 질문** | 1. Severe 알람과 Priority의 차이는 무엇인가?<br>2. CRC error 증가 시 첫 조치 단계는?<br>3. 이중화 전원 경고 시 복구 순서는? | "기초 인프라 장애 판단 및 상황별 대응 질문" | 단순 심각도가 아닌 비즈니스 가용성(Blast Radius) 중심의 판단 근거 |

---

## 🔗 4단계: 경험–역량 연결 (매칭표)

### 💡 경험-역량 연결 프롬프트

```text
아래 채용공고의 요구 역량과 내가 수행한 교육용 프로젝트를 연결해 주세요.

[내가 수행한 프로젝트]
- DCO 직무 용어 정리 (PDU, UPS, ToR Switch, N+1 이중화 등)
- 교육용 SOP 체크리스트 작성
- Git·GitHub를 이용한 파일 관리 및 버전 제어
- Antigravity CLI(agy)를 이용한 로컬 파일 및 작업 자동화
- Python 교육용 로그 분석 스크립트 작성 (`analyze_logs.py`)
- CRC error와 Link Down 시나리오 심층 분석 (`crc_Iinkdown_analysis.md`)
- 장애대응보고서 초안 작성 및 자동 검증 스크립트 (`dco_incident_report.md`, `check_incident_report.py`)
- Ticket Triage 및 Shift Handover Memo 작성 (`ticket_priority_matrix.csv`, `shift_handover.md`)

[출력 형식]
요구 역량 | 연결 가능한 프로젝트 | 증거 파일 | 면접에서 설명할 내용

[작성 조건]
1. 실제 데이터센터 근무 경험이 있다고 표현하지 마세요.
2. 교육용 프로젝트와 실제 업무 경험을 구분하세요.
3. 내가 제공하지 않은 성과를 만들지 마세요.
4. 연결이 어려운 역량은 억지로 연결하지 말고 '추가 학습 필요'라고 표시하세요.
```

### 🔗 경험–역량 매칭표

| 채용공고 요구 역량 | 연결되는 수업/프로젝트 경험 | GitHub 증거 자료 (파일 링크) | 현재 수준 | 보완할 점 (Action Item) |
| --- | --- | --- | :---: | --- |
| **문제 해결 & 장애 분석** | 장애 원인 가설 수립 및 물리 계층(CRC Error/Link Down) 분석 | [`crc_Iinkdown_analysis.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/10_incident_analysis/crc_Iinkdown_analysis.md) | 중급 | DOM(광파워 수치) 및 L1 계층 물리 측정 원리 보충 |
| **문서화 & 보고서 작성** | SOP 체크리스트 변환 및 11개 구조 Incident Report 작성 | [`dco_incident_report.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/11_incident_report/dco_incident_report.md) | 중급 | 실제 장애 상황 모의 구두 브리핑 연습 |
| **Python 자동화** | 140줄 DCO 가상 로그 파싱 스크립트 및 검증 프로그램 구현 | [`analyze_logs.py`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/09_log_analysis_script/analyze_logs.py) | 기초/중급 | 에러 예외 처리(Try-Except) 및 딕셔너리 구조화 확장 학습 |
| **Git·GitHub 활용** | 전체 프로젝트 체계적 디렉토리 설계 및 버전 관리 | [`README.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/README.md) | 중급 | 커밋 메시지 컨벤션(Conventional Commits) 지속 적용 |
| **Ticket Triage & 인수인계** | 복수 장애 발생 시 Blast Radius 기준 티켓 우선순위 결정 및 Handover | [`shift_handover.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/12_ticket_triage_handover/shift_handover.md) | 중급 | 랙 전원 계통도(Feed A/B) 관련 시설 지식 학습 |
| **Linux / 시스템 모니터링** | 가상 로그 심각도(ERROR/WARNING/INFO) 분류 파이프라인 | [`incident_summary.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/09_log_analysis_script/incident_summary.md) | 기초 | Linux CLI (dmesg, journalctl, grep) 실습 추가 필요 |
| **대시보드 설계** | Google AI Studio를 활용한 모니터링 대시보드 구조 설계 | *(추후 추가 예정)* | 추가 학습 필요 | AI Studio 대시보드 UI/UX 와이어프레임 제작 진행 |

---

## 💳 5단계: 경험 카드 (STAR 기법 기반 5종)

### 💡 경험 카드 작성 프롬프트

```text
당신은 취업준비생의 경험을 정리하는 코치입니다.
내가 작성한 내용을 바탕으로 경험 카드를 정리해 주세요.

[내 경험]
- 활동 목적:
- 내가 직접 수행한 일:
- 사용한 도구:
- 어려웠던 점:
- 해결하기 위해 한 행동:
- 완성한 결과:
- 배운 점:

[작성 조건]
1. 상황-과제-행동-결과-배운 점(STAR)으로 구분하세요.
2. 제공하지 않은 경험이나 성과를 만들지 마세요.
3. 실제 현장 업무처럼 과장하지 마세요.
4. 교육용 프로젝트라는 점을 유지하세요.
5. 결과 수치가 없다면 임의의 숫자를 만들지 마세요.
6. 지원 직무와 연결되는 역량을 3개 제시하세요.
7. 면접에서 1분 동안 설명할 수 있는 답변으로 정리하세요.
```

---

### 🎴 경험 카드 1: Python 기반 DCO 로그 분석 스크립트 작성

| 항목 | 작성 내용 |
| --- | --- |
| **경험명** | DCO 교육용 샘플 로그 파싱 및 자동 분석 스크립트 개발 |
| **활동 목적** | 140줄의 DCO 가상 로그 데이터에서 심각도별(ERROR/WARNING/INFO) 발생 건수를 자동 집계하고 핵심 장애 이벤트를 빠르게 추출하기 위함 |
| **사용한 도구** | Python 3, VS Code, Git |
| **어려웠던 점** | 파이프(`\|`) 구분자로 정렬된 가상 로그 텍스트를 정확히 정규표현식 및 문자열 분할로 파싱하는 과정에서 인코딩 및 예외 데이터 처리 문제 발생 |
| **해결 행동** | Python의 `re` 모듈과 `split('\|')` 구문을 활용해 날짜, 장비명, 심각도, 이벤트명, 상세 메시지를 딕셔너리로 추출하고 에러 카운터 로직 구축 |
| **완성 결과물** | [`analyze_logs.py`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/09_log_analysis_script/analyze_logs.py), [`incident_summary.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/09_log_analysis_script/incident_summary.md) |
| **배운 점** | 단순 로그 파싱을 넘어 이상 징후를 자동 요약하는 파이프라인의 중요성을 이해하였으며, AI 도구로 코드를 작성한 후에도 실행 검증이 필수적임을 깨달음 |
| **연결 직무 역량** | Python 기초 자동화, 로그 분석 능력, 데이터 구조화 |
| **GitHub 증거 자료**| `09_log_analysis_script/analyze_logs.py` |

---

### 🎴 경험 카드 2: CRC Error & Link Down 장애 분석 및 보고서 자동 검증

| 항목 | 작성 내용 |
| --- | --- |
| **경험명** | 포트 장애 원인 가설 분석 및 Incident Report 자동 검증 스크립트 구축 |
| **활동 목적** | 스위치 포트의 CRC error 급증 및 Link Down 장애에 대한 원인을 분석하고, 표준 보고서 작성 규칙을 자동으로 검증하기 위함 |
| **사용한 도구** | Markdown, Python, Antigravity CLI (`agy`) |
| **어려웠던 점** | AI가 초안 작성 시 근본 원인을 단정 지으려는 "환각(Hallucination)"이 있었고, 윈도우 콘솔(cp949) 환경에서 파이썬 검증 출력 시 유니코드 에러 발생 |
| **해결 행동** | 보고서에 `[사실]`, `[추정]`, `[미확인]` 구분을 명확히 도입하고, Python의 `sys.stdout.reconfigure(encoding='utf-8')` 구문을 추가하여 7가지 항목 자동 검증 프로그램 완성 |
| **완성 결과물** | [`dco_incident_report.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/11_incident_report/dco_incident_report.md), [`check_incident_report.py`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/11_incident_report/check_incident_report.py) |
| **배운 점** | 복구 완료 소식만으로 Root Cause를 단정해서는 안 되며, AI 초안을 검증(Human-in-the-Loop)하는 품질 관리 역량이 중요함을 배움 |
| **연결 직무 역량** | Incident Report 작성, 문제 해결 능력, 코드 기반 품질 검증 |
| **GitHub 증거 자료**| `11_incident_report/dco_incident_report.md` |

---

### 🎴 경험 카드 3: 교육용 SOP 분석 및 현장 랙/장비 점검 체크리스트 변환

| 항목 | 작성 내용 |
| --- | --- |
| **경험명** | 데이터센터 표준 운영 절차서(SOP) 분석 및 점검 체크리스트 제작 |
| **활동 목적** | 복잡한 가상의 DCO SOP 문서를 현장 엔지니어가 빠르게 점검할 수 있는 실행 가능한 체크리스트 서식으로 변환하기 위함 |
| **사용한 도구** | Markdown, VS Code |
| **어려웠던 점** | SOP 내의 장비 점검 순서와 안전 주의사항(ESD 방지, 전원 차단 순서 등)을 누락 없이 조치 단계별로 분류하는 데 어려움이 있었음 |
| **해결 행동** | 사전 준비, 본 작업, 작업 후 검증의 3단계 프로세스로 구분하고, 핵심 확인 항목을 Checkbox 형태로 재구성하여 작업 누락을 방지함 |
| **완성 결과물** | [`sop_checklist.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/03_sop_analysis/sop_checklist.md), [`rack_checklist.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/06_cli_file_automation/rack_checklist.md) |
| **배운 점** | 표준 절차서(SOP) 준수가 데이터센터 운용의 안정성 확보에 직결되며, 문서를 명확한 체크리스트로 바꾸는 문서화 능력을 기름 |
| **연결 직무 역량** | SOP 이해 및 준수, 현장 체크리스트 작성, 문서 구조화 |
| **GitHub 증거 자료**| `03_sop_analysis/sop_checklist.md` |

---

### 🎴 경험 카드 4: Ticket Triage 및 우선순위 기반 Shift Handover Memo 작성

| 항목 | 작성 내용 |
| --- | --- |
| **경험명** | 복수 인시던트 발생 시 서비스 영향도(Blast Radius) 기준 티켓 트리아지 및 인수인계 |
| **활동 목적** | 교대 시점(07:55)에 동시에 발생한 4개 장애 티켓의 우선순위를 결정하고 다음 담당자에게 정확한 Handover Memo를 전달하기 위함 |
| **사용한 도구** | Markdown, CSV, Antigravity CLI (`agy`) |
| **어려웠던 점** | 단순히 `ERROR` 문구나 발생 시각 순서에 쏠리지 않고, 이중화 전원(Feed B) 가동 여부 및 실제 서비스 차단 이력을 종합 판단하는 데 혼선이 있었음 |
| **해결 행동** | `Ticket ID`, `주요 현상`, `서비스 상태`, `영향 범위(Blast Radius)`, `티켓 상태`를 포함한 CSV 매트릭스를 작성하고, 1순위로 실제 Link Down 및 Link Flap이 재발한 포트 장애 티켓을 지정함 |
| **완성 결과물** | [`ticket_priority_matrix.csv`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/12_ticket_triage_handover/ticket_priority_matrix.csv), [`shift_handover.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/12_ticket_triage_handover/shift_handover.md) |
| **배운 점** | Severity는 사건의 심각도이고 Priority는 엔지니어의 처리 순서임을 체득하였으며, 교대 간 커뮤니케이션의 중요성을 인식함 |
| **연결 직무 역량** | Ticket Triage (우선순위 판단), 교대 인수인계 (Handover), 커뮤니케이션 |
| **GitHub 증거 자료**| `12_ticket_triage_handover/shift_handover.md` |

---

### 🎴 경험 카드 5: Git/GitHub 및 Antigravity CLI 활용 버전 관리 및 페어 프로그래밍

| 항목 | 작성 내용 |
| --- | --- |
| **경험명** | Git/GitHub 프로젝트 버전 관리 및 생성형 AI CLI(agy) 협업 학습 |
| **활동 목적** | 전체 교육 과정의 포트폴리오 산출물을 체계적으로 관리하고, AI 도구를 페어 파트너로 활용하여 작업 생산성을 향상시키기 위함 |
| **사용한 도구** | Git, GitHub, Antigravity CLI (`agy`), Windows PowerShell |
| **어려웠던 점** | 대량의 산출물을 디렉토리 규칙에 맞춰 관리하고, AI가 도출한 원본 설명 부족 및 이중화 맥락 오인을 사람이 교정하는 데 시간이 소요됨 |
| **해결 행동** | 차시별 숫자 디렉토리 규칙을 수립하여 Git 커밋 메시지 컨벤션을 적용하였으며, AI 생성 결과에서 발견한 오류를 `README.md`에 투명하게 기록함 |
| **완성 결과물** | [`README.md`](file:///C:/Users/admin_23/Desktop/AWS-DCO-GenAI-Portfolio/README.md) (전체 포트폴리오 및 회고 통합) |
| **배운 점** | 결과물 자체뿐만 아니라 AI를 어떤 목적으로 활용하고 무엇을 직접 검증하여 수정했는가(Human-in-the-Loop)의 과정 기록이 중요함을 배움 |
| **연결 직무 역량** | Git/GitHub 버전 관리, AI 페어 프로그래밍, 학습 회고 및 메타인지 |
| **GitHub 증거 자료**| `README.md` |

---

## 🎙️ 6단계: AI 모의 면접 가이드 및 모의 면접 기록표

### 💡 AI 모의 면접 실행 프롬프트

```text
당신은 신입 IT 인프라/DCO 운영지원 직무의 면접관입니다.

아래 채용공고와 프로젝트 내용을 바탕으로 모의 면접을 진행해 주세요.

[진행 규칙]
1. 한 번에 질문을 하나만 하세요.
2. 내가 답변하기 전에 모범답안을 보여 주지 마세요.
3. 답변 후 다음 항목을 100점 만점으로 평가하세요.
   - 질문에 직접 답했는가
   - 실제 경험이 구체적으로 나타나는가
   - 행동과 결과가 구분되는가
   - 기술 용어가 정확한가
   - 과장하거나 근거 없이 말한 부분이 있는가
4. 답변에서 불명확한 부분을 찾아 꼬리질문을 하세요.
5. 5개의 질문이 끝나면 전체 피드백을 제공하세요.

[나의 경험 범위]
나는 공개 직무 정보와 교육용 샘플 데이터를 이용한 프로젝트를 수행했습니다. 실제 AWS 내부 시스템이나 실제 데이터센터 장비를 운영한 경험은 없습니다.

[지원 직무 / 채용공고 타겟]
AWS DCO 인턴 및 데이터센터 IT 인프라 운영 지원

[프로젝트 내용]
- DCO 용어집 정리 및 SOP 체크리스트 작성
- Python 가상 로그 파싱 스크립트 작성 (analyze_logs.py)
- CRC error/Link Down 심층 분석 및 Incident Report 작성 (dco_incident_report.md)
- Incident Report 품질 자동 검증 스크립트 개발 (check_incident_report.py)
- Ticket Triage & Shift Handover Memo 작성 (shift_handover.md)
- README.md 기반 AI 초안 검증 및 회고 작성
```

---

### 📝 모의 면접 기록표 (예시 및 연습용 서식)

| 질문 | 내 답변의 핵심 | AI 피드백 (점수 & 평가) | 수정 및 보안할 내용 (Action Item) |
| :---: | :--- | :--- | :--- |
| **Q1. Severity와 Priority의 차이를 설명하고, 실제 프로젝트에서 어떤 기준으로 티켓 우선순위를 정했나요?** | Severity는 사건의 기술적 심각도이고, Priority는 엔지니어가 무엇을 먼저 처리할지 정하는 순서입니다. 실습 시 이중화 전원으로 작동 중인 PDU 경고보다 actual outage(Link Down)가 발생하고 Link Flap이 재발한 포트 장애 티켓을 1순위로 결정했습니다. | **92점**: 용어 정의가 명확하고 랙 이중화와 실제 통신 차단 사례를 명확히 비교함. 수치적 Blast Radius(서버 2대 vs 6대)를 좀 더 붙이면 완벽함. | 우선순위 설명 시 영향 서버 수(Blast Radius)의 정량적 기준을 추가 언급하도록 연습. |
| **Q2. CRC Error 알람 발생 후 Link Down으로 이어지는 장애 상황에서 첫 조치 단계와 주의할 점은?** | 5분 내 CRC error 수치를 확인하고, 포트 물리 케이블 및 커넥터 세척/교체를 판단합니다. 단, 수리 완료 후 Link Up이 되었더라도 곧바로 원인이 결정된 것은 아니며 가설로 남겨둬야 합니다. | **88점**: 기술적 흐름을 잘 파악함. 다만 SFP 모듈 수신 광파워(DOM 수치) 확인 등 실측 데이터 파악 단계를 추가 언급하면 좋음. | DOM(Digital Optical Monitoring) 수치 확인 및 현장 랙 작업 로그 대조 단계 언급 보완. |
| **Q3. AI(Antigravity CLI)로 장애 보고서 초안을 작성할 때 발생했던 문제와 이를 해결한 방법은?** | AI가 근본 원인(Root Cause)을 하나로 확정 지으려는 단정적 편향이 있었습니다. 이를 방지하고자 [사실], [추정], [미확인] 태그를 적용하고, Python 정규표현식 검증 스크립트를 만들어 자동 검사했습니다. | **95점**: AI의 한계(Hallucination)와 이를 시스템적으로 검증(Python Script)한 경험이 구체적이며 과장이 없음. | 검증 스크립트의 구체적 검사 항목 7가지를 가볍게 나열할 수 있도록 정돈. |
| **Q4. 교대 인수인계(Shift Handover) 시 가장 중요하게 생각한 요소와 작성 항목은?** | 현재 Open 상태의 티켓뿐만 아니라 '아직 확인되지 않은 정보'와 '다음 담당자가 즉시 실행할 Action Item'을 3줄 요약으로 명확히 구분하여 전달하는 것입니다. | **90점**: 인수인계의 목적인 업무 연속성과 리스크 전달을 잘 설명함. | Monitoring 상태 티켓과 Resolved 티켓의 관리 구분선도 간단히 덧붙이기. |
| **Q5. 데이터센터 현장 근무 경험이 없는데, 본인이 DCO 인턴으로서 빠르게 적응할 수 있는 근주는?** | 실제 근무 경험은 없으나, 가상 샘플 로그 파싱, SOP 체크리스트 작성, Incident Report 검증 스크립트 제작을 통해 데이터센터 운영 흐름과 용어를 체득하였고, AI 도구를 검증하며 일하는 습관을 다졌습니다. | **94점**: 솔직하게 학습 경험임을 인정하면서도 결과물(GitHub 증거)을 바탕으로 신뢰감을 줌. | 비전공자로서의 분석적 사고방식(분자생물학 → IT 인프라 파이프라인 이해)을 접목. |
