# Shift Handover Memo

- **작성자**: DCO 엔지니어 (교육용)
- **교대 시점**: 2026-07-10 07:55

> **[EDUCATIONAL SAMPLE DATA]**
> 본 문서는 실제 AWS 시스템, 장비, 티켓 또는 운영 절차가 아닌 public DCO job-context 학습용 교육용 샘플 데이터를 바탕으로 작성된 인수인계 문서입니다.

---

## 가장 먼저 확인할 Ticket

- **EDU-TKT-2026-0201** (`SAMPLE_TOR_SW_03` Gi0/24 포트 Link Flap 및 Link Down 재발 건)
  - **이유**: 실제로 Link Down이 발생하여 서버 2대의 연결이 일시 차단되었고, Link Up 복구 이후에도 Link Flap이 재발했으나 원인이 미확인된 Open 상태이기 때문입니다.

---

## 현재 Open 상태 Ticket

- **EDU-TKT-2026-0201**: SAMPLE_TOR_SW_03 Gi0/24 포트 Link Flap 재발 (Open)
- **EDU-TKT-2026-0202**: SAMPLE_RACK_PDU_05A 입력 전압 경고 지속 및 시설팀 Escalated (Open)

---

## Monitoring 상태 Ticket

- **EDU-TKT-2026-0203**: EDU_SRV_R02_N08 SSD Slot 2 예측 장애 경고 및 미러링 가동 (Monitoring)

---

## Resolved 상태 Ticket

- **EDU-TKT-2026-0204**: DEMO_CORE_SW_04 Fan 모듈 1 RPM 저하 발생 후 정상 회복 (Resolved)

---

## 현재까지 확인된 사실

- **[사실]** `SAMPLE_TOR_SW_03` Gi0/24 포트에서 10분 내 4회 Link Flap 및 Link Down이 발생하여 샘플 서버 2대가 일시 연결 불가능했으나 현재는 Link Up 상태임. 단, 07:05에 상태 변화가 1회 더 기록됨.
- **[사실]** `SAMPLE_RACK_PDU_05A` Feed A 입력 전압 경고가 06:50부터 지속 중이며, Feed B 이중화 전원 동작으로 서비스 중단은 없으나 랙 연관 6대 서버에 영향 가능성이 있어 시설(Facilities) 팀으로 Escalated됨.
- **[사실]** `EDU_SRV_R02_N08` SSD Slot 2 예측 장애 경고가 발생하였으나, 저장장치 미러가 활성화되어 서비스는 정상 가동 중임.
- **[사실]** `DEMO_CORE_SW_04` Fan 모듈 1 RPM 저하 경고가 발생했으나 섀시 온도는 정상 범위 내 유지되었고 RPM이 정상 복구(07:22)되어 티켓 처리 완료됨.

---

## 아직 확인되지 않은 내용

- **[미확인]** Gi0/24 포트의 반복적 Link Flap 발생 근본 원인 및 광 트랜시버/케이블 신호 측정값.
- **[미확인]** PDU Feed A 입력 전압 경고의 원인 및 시설(Facilities) 팀의 현장 점검 조사 결과.
- **[미확인]** SSD 예측 장애 수리를 위한 교체 작업 점검 일정 및 교체용 자재 수급 상태.

---

## 다음 담당자가 확인할 내용

1. **`EDU-TKT-2026-0201` 점검**: Gi0/24 포트의 신호 감쇄 및 반복 Link Flap 발생 원인 추적 확인.
2. **`EDU-TKT-2026-0202` 점검**: Facilities 팀으로 Escalated된 PDU Feed A 전압 경고 조사 경과 및 이중화 유지 상태 모니터링.
3. **`EDU-TKT-2026-0203` 점검**: SSD 예측 장애 보고 서버의 작업 유지보수 일정 및 디스크 자재 수급 확인.

---

## 3줄 인수인계 요약

1. 최우선 확인 티켓은 Link Up 후에도 Link Flap이 재발하고 원인이 미해결된 `EDU-TKT-2026-0201` (스위치 포트 장애)입니다.
2. PDU Feed A 전압 경고(`EDU-TKT-2026-0202`)는 Feed B 이중화로 서비스 정상이나 6대 서버 연관 랙 전원 경고이므로 시설팀 조치 경과 확인이 필요합니다.
3. SSD 예측 장애(`EDU-TKT-2026-0203`)는 미러링 동작 중으로 모니터링 단계이며, Fan 경고(`EDU-TKT-2026-0204`)는 정상 복구되어 완료되었습니다.

---

## agy 결과와 내 판단 비교

- **agy가 잘 정리한 내용**: 로그상의 시간순 사건, Ticket ID별 1:1 매핑, 현재 Ticket 상태(Open, Monitoring, Resolved) 및 확인된 사실을 빠짐없이 규칙적 문맥으로 정리함.
- **agy 결과에서 빠졌거나 부족했던 내용**: 단순히 로그 메시지 문구만 나열하는 수준을 넘어 장애 영향 서버 수(서버 2대 vs 6대) 및 전원 이중화 구조(Feed B 이중화, SSD 미러링) 간의 서비스 리스크를 반영하여 티켓 간의 우열(우선순위)을 정하는 판단 근거 작성을 사용자가 직접 도출하도록 요구함.
- **내가 정한 우선순위**:
  - 1순위: `EDU-TKT-2026-0201` (Link Down 발생 이력 및 Link Flap 재발 Open)
  - 2순위: `EDU-TKT-2026-0202` (PDU 전압 경고 지속 및 6대 서버 영향 리스크 Open/Escalated)
  - 3순위: `EDU-TKT-2026-0203` (SSD 예측 장애 미러링 동작 Monitoring)
  - 4순위: `EDU-TKT-2026-0204` (Fan RPM 정상 복구 Resolved)
- **그렇게 판단한 이유**: 실제로 연결 끊김(Link Down)이 발생했고 복구 후에도 반복적 상태 변화(Link Flap)가 관찰된 포트 티켓(`0201`)이 서비스 가용성에 직결되므로 최우선 순위로 지정하였습니다. PDU 경고(`0202`) 역시 랙 전원 위협으로 중요하지만 이중화(Feed B) 덕분에 가용성이 유지되고 있어 2순위로 지정하였습니다.
