# 📋 [교육용] DCO 네트워크 포트 장애 (CRC Error / Link Down) Incident Report 초안

> **[주의] 본 문서는 실제 AWS 내부 보고서가 아닌 DCO(Data Center Operations) 교육용 샘플 데이터를 바탕으로 작성된 가상의 초안 문서입니다.**

---

## 1. 보고서 제목
- **[교육용 샘플]** SAMPLE_TOR_SW_01 장비 Gi0/1 포트 CRC Error 급증 및 Link Down 장애 대응 Incident Report

## 2. 작성 목적
본 보고서는 AWS DCO (Data Center Operations) 직무 이해 및 로그 분석/인시던트 대응 교육 실습을 목적으로 작성되었습니다. 실제 데이터센터 인시던트 보고서 양식의 구조를 습득하고, 수집된 로그 데이터를 기반으로 **확인된 사실(Fact)**과 **가능한 원인(Hypothesis)**을 객관적으로 분리하여 정리하는 연습을 위한 목적을 가집니다.

## 3. 교육용 사건 개요
- **장애 요약**: 2026년 7월 3일 03:05경, 샘플 스위치 장비(`SAMPLE_TOR_SW_01`)의 `Gi0/1` 인터페이스에서 5분간 CRC Error 수치가 154까지 급증하는 WARNING 이벤트가 발생하였고, 이어 03:06에 포트 상태가 DOWN으로 변경되어 서버 연결이 유실되는 ERROR 장애가 발생하였습니다.
- **조치 요약**: 자동 티켓 생성 및 현장 케이블링 팀(Onsite Cabling Team) 이관 후, LC-LC multi-mode patch cord 케이블 교체 및 포트 커넥터 세척 작업(03:25)을 거쳐 03:26에 Link Up 상태로 복구되었으며 03:30 기준 CRC error가 0으로 안정화되었습니다.
- **데이터 출처**: `sample_dco_log.txt`, `incident_summary.md`, `crc_Iinkdown_analysis.md` (이상 교육용 가상 샘플 데이터)

## 4. 관련 샘플 장비와 Ticket
- **대상 샘플 장비**: `SAMPLE_TOR_SW_01` (IP Address: `192.0.2.1`)
- **영향 인터페이스**: `Gi0/1`
- **발행 Ticket ID**: `EDU-TKT-2026-0003`
- **담당/이관 팀**: `Onsite Cabling Team`
- *(참고: 로그 내 동일 시간대에 존재한 `DEMO_CORE_SW_02`, `EDU_SRV_R04_N12` 관련 기기 이벤트는 본 인시던트 건과 별개의 건임)*

## 5. 시간순 이벤트

| 시간 (Timestamp) | 심각도 (Severity) | 이벤트명 (Event) | 상세 내용 (Log Message) |
|---|---|---|---|
| **03:05:00** | **WARNING** | CRC error 증가 | Interface Gi0/1 CRC error counter increased to 154 within 5 minutes. IP: 192.0.2.1 |
| **03:06:00** | **ERROR** | Link Down | Interface Gi0/1 status changed to DOWN. Connection to server lost. |
| **03:07:00** | **INFO** | Ticket opened | Ticket EDU-TKT-2026-0003 created for Gi0/1 port offline. |
| **03:12:00** | **INFO** | Ticket escalated | Ticket EDU-TKT-2026-0003 escalated to Onsite Cabling Team. |
| **03:25:00** | **INFO** | Maintenance completed | LC-LC multi-mode patch cord cable swapped, port connectors cleaned. |
| **03:26:00** | **INFO** | Link Up | Interface Gi0/1 status changed to UP. Line protocol status is UP. |
| **03:30:00** | **INFO** | Normal heartbeat | System status is healthy. Interface Gi0/1 running with 0 CRC errors. IP: 192.0.2.1 |

## 6. 로그에서 확인된 사실

- **[사실 1]**: `SAMPLE_TOR_SW_01` 장비의 `Gi0/1` 포트에서 03:05:00에 5분 이내 154개의 CRC error가 기록되어 WARNING 알람이 발송되었습니다.
- **[사실 2]**: CRC error 알람 발생 1분 뒤인 03:06:00에 `Gi0/1` 포트가 DOWN 상태로 변경되고 서버와의 연결이 중단되었습니다.
- **[사실 3]**: 03:07:00에 해당 장애 처리를 위한 Ticket(`EDU-TKT-2026-0003`)이 생성되었습니다.
- **[사실 4]**: 03:12:00에 해당 Ticket이 `Onsite Cabling Team`으로 이관(escalated)되었습니다.
- **[사실 5]**: 03:25:00에 LC-LC multi-mode patch cord 케이블 교체 및 포트 커넥터 세척(cleaned) 작업이 완료되었습니다.
- **[사실 6]**: 03:26:00에 `Gi0/1` 포트 status 및 Line protocol status가 UP 상태로 전환(Link Up)되었습니다.
- **[사실 7]**: 03:30:00에 Normal heartbeat와 함께 시스템이 healthy 상태로 기록되었으며, `Gi0/1` 포트의 CRC error 수치가 0으로 유지됨을 확인하였습니다.

## 7. 가능한 원인

> **[주의] 로그 데이터 및 수리 내역을 통해 추정할 수 있는 원인 가설들이며, 단일 원인으로 최종 확정하지 않습니다.**

- **가능성 1: 광 패치 코드 케이블(LC-LC Multi-mode Patch Cord)의 물리적 노화 또는 손상**
  - **[추정 근거]**: `Onsite Cabling Team`의 LC-LC multi-mode patch cord 교체 완료 직후 링크가 복구되고 CRC error가 0으로 해소되었습니다.
  - **[미확인 요소]**: 로그 기록만으로는 교체 전 기존 케이블 피복의 기계적 꺾임이나 파이버 심선의 물리적 단선 상태를 직접 입증할 수 없습니다.
- **가능성 2: Port Connectors 단면의 먼지/이물질 유입에 따른 광 신호 감쇄 (Optical Attenuation)**
  - **[추정 근거]**: 케이블 교체와 동시에 커넥터 청소(cleaned)가 수행된 후 에러가 정지되었습니다.
  - **[미확인 요소]**: 청소 작업 이전 광단자 면에 오염물질이 실제 어느 정도 정착해 있었는지는 로그에 기록되지 않았습니다.
- **가능성 3: 트랜시버 모듈(SFP/GBIC) 접촉 불량 또는 미세 탈착**
  - **[추정 근거]**: 현장 유지보수 작업(Maintenance) 과정에서 케이블 재연결로 인해 광 트랜시버 조작 및 결합 물리 상태가 교정되었을 수 있습니다.
  - **[미확인 요소]**: 광 트랜시버 자체의 기계적 고장이나 진동 발생 여부는 본 로그만으로 판단할 수 없습니다.

## 8. 현재 확인되지 않은 내용

- **[미확인]**: 장애 전후 `Gi0/1` 포트의 실시간 광파워(DOM: Digital Optical Monitoring, Rx/Tx Power) 수치.
- **[미확인]**: 수거된 기존 LC-LC multi-mode patch cord의 물리적 피복 상태 및 광 손실율(Insertion Loss) 실측 데이터.
- **[미확인]**: 장애 발생 시점 전후로 랙(Rack) 주변에서 진행된 타 물리 작업이나 외부 진동 발생 여부.
- **[미확인]**: 연결 상대방 서버 측 NIC(네트워크 인터페이스 카드) 커널 로그 및 링크 이벤트 기록.

## 9. 추가로 필요한 정보

1. **DOM (Digital Optical Monitoring) 수치 데이터**: 송수신 광파워(Tx/Rx Power) 모니터링 로그를 확보하여 물리 신호 감쇄 추이 대조 분석 필요.
2. **현장 랙 작업 이력 (Rack Activity Log)**: 해당 시점 인근 랙에서 다른 물리적 작업이나 케이블 이동 조작이 있었는지 여부 확인.
3. **상대 서버 OS 커널 로그 (dmesg / NIC log)**: 스위치 포트 DOWN 시점 서버 측 인터페이스 드라이버에서 감지된 로그 상태 대조.
4. **회수 자재 감쇄 측정 보고서**: 철거된 패치 코드 케이블의 실제 절연 및 광 투과율 측정 결과 확인.

## 10. Escalation 전달 메모

```text
[교육용 Escalation 전달 메모 예시]

수신: Onsite Cabling Team 및 DCO Infrastructure Operations Team
발신: DCO Monitoring Team (교육용)
관련 티켓: EDU-TKT-2026-0003
대상 장비: SAMPLE_TOR_SW_01 (Port: Gi0/1 / IP: 192.0.2.1)

내용:
2026-07-03 03:05경 발생한 SAMPLE_TOR_SW_01 장비 Gi0/1 포트의 CRC Error(154건) 및 Link Down 장애와 관련하여,
Onsite Cabling Team의 LC-LC multi-mode patch cord 교체 및 커넥터 세척 작업을 통해 03:26 기준 Link Up 및 03:30 기준 CRC error 0으로 정상 복구 완료되었습니다.

현장에서 수거한 기존 패치 코드 자재에 대한 추가 물리 측정 결과 및 이물질 확인 내역이 있을 경우, 
티켓 EDU-TKT-2026-0003의 종결 보고 항목에 업데이트 공유를 요청드립니다.
```

## 11. 최종 요약

- 본 보고서는 가상 데이터 기반의 DCO 교육용 샘플 보고서 초안입니다.
- `SAMPLE_TOR_SW_01` (Gi0/1) 포트에서 물리 계층 문제로 추정되는 CRC Error 급증 및 Link Down 인시던트가 발생하였으며, 자동 생성된 티켓(`EDU-TKT-2026-0003`)을 통해 `Onsite Cabling Team`으로 이관되었습니다.
- 현장 점검 중 LC-LC multi-mode patch cord 케이블 교체 및 커넥터 세척이 완료된 후 인터페이스가 정상 복구(Link Up, CRC Error 0)되었음을 확인했습니다.
- 원인은 패치 코드 physical failure, 커넥터 오염, 트랜시버 물리 접촉 미세 오차 등 복수의 물리 계층 가설로 추정되며, 추후 DOM 측정값 및 회수 자재 분석을 통해 보다 상세한 규명이 가능합니다.

---

## 12. 노션 실습용 1분 브리핑 요약

```text
Ticket: EDU-TKT-2026-0003
발생 시간: 2026-07-03 03:05 (복구 완료: 03:30)
대상 장비: SAMPLE_TOR_SW_01 (인터페이스: Gi0/1 / IP: 192.0.2.1)
주요 현상: Gi0/1 포트에서 5분간 154개의 CRC Error 급증(WARNING) 후, 포트 Link Down(ERROR) 및 서버 연결 유실 발생
현재 상태: Link Up 정상 복구 완료 (System status: Healthy, CRC Error: 0)
수행된 조치: Ticket을 Onsite Cabling Team으로 이관(03:12)하여 LC-LC multi-mode patch cord 케이블 교체 및 port connectors 세척 작업 완료(03:25)
확인되지 않은 내용: 교체 전 케이블 물리적 훼손 상태, 커넥터 세척 전 이물질 오염 정도, 포트 실시간 광파워(DOM) 수치
다음 확인 사항: DOM 광파워 모니터링 로그 확인, 철거된 케이블 물리 감쇄율 실측, 상대 서버 NIC 커널 로그(dmesg) 대조
```

