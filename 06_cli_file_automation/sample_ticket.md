# [EDU] 교육용 샘플 티켓: CRC 에러 및 링크 다운 이벤트

> [!IMPORTANT]
> **교육용 가상 데이터 안내**
> 본 문서는 실제 AWS 내부 절차, 실제 장비, 실제 티켓, 실제 고객 정보를 포함하지 않습니다. 
> 모든 예시는 `SAMPLE`, `EDU` 접두어가 붙은 교육용 가상 데이터이며, 학습 목적으로만 활용됩니다.

---

## 1. 티켓 기본 정보

| 항목 | 상세 정보 |
| --- | --- |
| **티켓 ID** | `EDU-TKT-2026-008912` (Sample Only) |
| **발생 시간 (UTC)** | `2026-07-07 05:42:11` |
| **샘플 장비명** | `SAMPLE_TOR_SW_01` (가상 Top of Rack Switch) |
| **이벤트 유형** | `Link Down (Interface Ethernet 1/1)` |
| **심각도 (Severity)** | `Severity 3 - Medium` (Sample Category) |

---

## 2. 모니터링 관찰 내용 (Simulated Logs)

아래의 로그 정보는 실습을 위해 구성된 가상의 모니터링 출력입니다.

```log
2026-07-07T05:38:15Z SAMPLE_TOR_SW_01 daemon.info: Port Ethernet 1/1: CRC error count increased (Current: 1452, Delta: +120)
2026-07-07T05:40:15Z SAMPLE_TOR_SW_01 daemon.info: Port Ethernet 1/1: CRC error count increased (Current: 2840, Delta: +1388)
2026-07-07T05:42:11Z SAMPLE_TOR_SW_01 daemon.crit: Port Ethernet 1/1: Link state changed to DOWN
```

### 상세 분석 사항 (Observations)
- **CRC 에러 누적**: `Ethernet 1/1` 인터페이스에서 물리적 혹은 논리적 오류 전송으로 인한 CRC 에러가 2분 간격으로 급격히 증가함.
- **링크 상태 전환**: 에러 누적 직후 링크 상태가 `DOWN`으로 전환되어 통신이 중단됨.

---

## 3. 후속 조치 및 에스컬레이션 (Escalation)

- **Escalation 필요 여부**: **YES (예)**
  - 1차 로그상 원인 단정이 불가하므로, 현장 랙의 케이블 접촉 상태 또는 패치 패널 상태 점검을 위한 인필드(In-Field) 엔지니어 협조 요청 필요.
- **협업 참조**: `06_cli_file_automation/rack_checklist.md` 문서를 기반으로 교차 검증 요망.

---

## 4. 보안 주의사항 (Security Guidelines)

- **주의 1**: 본 샘플 티켓 내에는 가상의 호스트명(`SAMPLE_TOR_SW_01`)만 존재하며, 실제 IP 주소나 스위치 시리얼 번호는 절대 기재하지 않습니다.
- **주의 2**: 스위치 내부 설정 값이나 실제 라우팅 테이블 정보는 보안 통제 대상이므로 노출하지 않습니다.
