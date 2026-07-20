import re
import os
import sys

# Windows 콘솔 인코딩 대응
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def check_incident_report(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    results = {}

    # 1. Ticket ID 존재 여부 (예: EDU-TKT-2026-0003, Ticket ID 등)
    ticket_pattern = r"(EDU-TKT-\d{4}-\d{4}|Ticket\s*ID|티켓)"
    results["Ticket ID 존재 여부"] = bool(re.search(ticket_pattern, content, re.IGNORECASE))

    # 2. 발생 시간 존재 여부 (예: 2026-07-03, 03:05:00 등)
    time_pattern = r"(\d{4}-\d{2}-\d{2}|\d{2}:\d{2}(:\d{2})?)"
    results["발생 시간 존재 여부"] = bool(re.search(time_pattern, content))

    # 3. 장비명 존재 여부 (예: SAMPLE_TOR_SW_01 등)
    device_pattern = r"(SAMPLE_[A-Z0-9_]+|DEMO_[A-Z0-9_]+|EDU_[A-Z0-9_]+|장비명|SAMPLE_TOR_SW_01)"
    results["장비명 존재 여부"] = bool(re.search(device_pattern, content))

    # 4. 조치 내용 존재 여부 (예: 교체, 세척, Maintenance, swapped, cleaned 등)
    action_pattern = r"(교체|세척|Maintenance|swapped|cleaned|조치|보수)"
    results["조치 내용 존재 여부"] = bool(re.search(action_pattern, content, re.IGNORECASE))

    # 5. 결과 상태 존재 여부 (예: Link Up, healthy, 정상, 0 CRC error 등)
    status_pattern = r"(Link Up|healthy|정상|복구|0 CRC|Line protocol status is UP)"
    results["결과 상태 존재 여부"] = bool(re.search(status_pattern, content, re.IGNORECASE))

    # 6. Root Cause 단정 표현 존재 여부 (예: "원인은 ~이다", "원인 확정", "최종 원인은" 등)
    assertive_cause_pattern = r"(원인은 [가-힣a-zA-Z0-9_]+이다|원인을 확정|최종 원인은 [가-힣a-zA-Z0-9_]+이다|확정적 원인)"
    has_assertive_cause = bool(re.search(assertive_cause_pattern, content))
    results["Root Cause 단정 표현 존재 여부"] = has_assertive_cause

    # 7. 교육용 샘플 데이터 문구 존재 여부 (예: 교육용, 샘플 데이터, 가상 데이터 등)
    edu_pattern = r"(교육용|샘플 데이터|가상|sample data)"
    results["교육용 샘플 데이터 문구 존재 여부"] = bool(re.search(edu_pattern, content, re.IGNORECASE))

    print("=" * 60)
    print("Incident Report (dco_incident_report.md) 검증 결과")
    print("=" * 60)

    for item, status in results.items():
        if item == "Root Cause 단정 표현 존재 여부":
            status_str = "[WARNING] 단정 표현 발견됨 (수정 필요)" if status else "[PASS] 미발견 (가설/가능성 형태로 적절함)"
        else:
            status_str = "[PASS] 존재함" if status else "[FAIL] 미존재"
        
        print(f"- {item:<30}: {status_str}")

    print("=" * 60)

if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "11_incident_report/dco_incident_report.md"
    check_incident_report(target_file)

