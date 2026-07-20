# -*- coding: utf-8 -*-
"""
DCO 교육용 샘플 로그 분석 스크립트
작성자: Python 코드 작성 도우미 (인턴십 교육용)
설명: 비전공자 학생도 이해하기 쉽도록 주석을 상세하게 작성한 Python 표준 라이브러리 기반 로그 분석기입니다.
"""

import os

# 입력 파일명과 출력 파일 경로를 설정합니다.
INPUT_FILE = "sample_dco_log.txt"
OUTPUT_DIR = r"C:\Users\admin_23\Desktop\AWS-DCO-GenAI-Portfolio"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "incident_summary.md")

def analyze_logs():
    # 1. 분석을 위해 필요한 변수들을 준비합니다 (초기화)
    total_lines = 0                     # 전체 로그 줄 수
    severity_counts = {}                # 심각도별(INFO, WARNING, ERROR 등) 개수 저장용 딕셔너리
    event_counts = {}                   # 이벤트 종류별 개수 저장용 딕셔너리
    warning_critical_logs = []          # WARNING 또는 CRITICAL 단계의 로그를 담을 리스트
    major_events = []                   # CRC_ERROR, LINK_DOWN, TICKET_ESCALATED 관련 주요 이벤트 저장 리스트

    # 입력 파일이 존재하는지 확인합니다.
    if not os.path.exists(INPUT_FILE):
        print(f"오류: 입력 로그 파일 '{INPUT_FILE}'을 찾을 수 없습니다.")
        print("현재 작업 디렉토리에 파일이 존재하는지 확인해주세요.")
        return

    # 2. 로그 파일을 읽어와 한 줄씩 분석합니다.
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip() # 줄 바꿈 문자(\n)나 불필요한 앞뒤 공백을 제거합니다.
            if not line:
                continue # 빈 줄은 건너뜜

            total_lines += 1

            # 로그 형식: YYYY-MM-DD HH:MM:SS | DEVICE | SEVERITY | EVENT | MESSAGE
            # ' | ' 문자열을 기준으로 각 요소를 나눕니다.
            parts = [part.strip() for part in line.split("|")]
            
            # 올바른 형식의 로그가 맞는지 확인합니다 (5개 영역으로 나뉘어야 함).
            if len(parts) < 5:
                continue

            timestamp = parts[0]
            device = parts[1]
            severity = parts[2]
            event = parts[3]
            message = parts[4]

            # (1) 심각도별(SEVERITY) 개수 세기
            # 딕셔너리에 이미 있는 심각도면 +1, 없으면 새롭게 1로 시작합니다.
            if severity in severity_counts:
                severity_counts[severity] += 1
            else:
                severity_counts[severity] = 1

            # (2) 이벤트(EVENT)별 개수 세기
            if event in event_counts:
                event_counts[event] += 1
            else:
                event_counts[event] = 1

            # (3) WARNING 또는 CRITICAL 로그 목록 수집
            # 심각도가 WARNING이거나 CRITICAL인 경우 리스트에 저장합니다.
            if severity in ["WARNING", "CRITICAL"]:
                warning_critical_logs.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

            # (4) CRC_ERROR, LINK_DOWN, TICKET_ESCALATED가 포함된 주요 이벤트 요약 대상 식별
            # 비전공자 교육용이므로 대소문자 구분 없이 직관적으로 주요 키워드를 검사합니다.
            event_upper = event.upper()
            msg_upper = message.upper()

            # CRC 관련 (CRC_ERROR, CRC error 등)
            is_crc = ("CRC" in event_upper or "CRC" in msg_upper)
            # LINK_DOWN 관련 (LINK DOWN, LINK_DOWN, status down 등)
            is_link_down = ("LINK DOWN" in event_upper or "LINK_DOWN" in event_upper or 
                            "LINK DOWN" in msg_upper or "LINK_DOWN" in msg_upper or
                            ("LINK" in event_upper and "DOWN" in event_upper))
            # TICKET_ESCALATED 관련 (TICKET ESCALATED, TICKET_ESCALATED 등)
            is_ticket_escalated = ("TICKET ESCALATED" in event_upper or "TICKET_ESCALATED" in event_upper or
                                   "TICKET ESCALATED" in msg_upper or "TICKET_ESCALATED" in msg_upper or
                                   "ESCALATED" in event_upper or "ESCALATED" in msg_upper)

            if is_crc or is_link_down or is_ticket_escalated:
                category = "기타 주요 이벤트"
                if is_crc:
                    category = "CRC_ERROR"
                elif is_link_down:
                    category = "LINK_DOWN"
                elif is_ticket_escalated:
                    category = "TICKET_ESCALATED"

                major_events.append({
                    "category": category,
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

    # 3. 분석한 결과를 지정된 마크다운 파일로 저장합니다.
    # 결과를 저장할 폴더가 없다면 생성합니다.
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# 📋 DCO 교육용 샘플 로그 분석 보고서\n\n")
        out.write("이 보고서는 AWS DCO 인턴십 직무 이해를 돕기 위해 교육용 샘플 로그를 분석하여 작성된 인시던트 요약본입니다.\n")
        out.write("*(실제 AWS 내부 시스템 로그가 아니며 가상 시스템 데이터입니다.)*\n\n")

        # 1. 전체 로그 요약
        out.write("## 1. 전체 로그 분석 요약\n")
        out.write(f"- **총 로그 줄 수**: {total_lines} 줄\n\n")

        # 2. 심각도별 개수
        out.write("## 2. 심각도별 로그 분포\n")
        out.write("| 심각도 (Severity) | 개수 (Count) | 비율 (Percentage) |\n")
        out.write("| --- | --- | --- |\n")
        for sev, count in sorted(severity_counts.items()):
            percentage = (count / total_lines) * 100
            out.write(f"| **{sev}** | {count}개 | {percentage:.1f}% |\n")
        out.write("\n")

        # 3. 이벤트별 개수
        out.write("## 3. 주요 이벤트별 로그 발생 건수\n")
        out.write("| 이벤트명 (Event) | 발생 건수 |\n")
        out.write("| --- | --- |\n")
        # 발생 빈도가 높은 순서대로 정렬하여 출력합니다.
        sorted_events = sorted(event_counts.items(), key=lambda x: x[1], reverse=True)
        for evt, count in sorted_events:
            out.write(f"| {evt} | {count}개 |\n")
        out.write("\n")

        # 4. WARNING 또는 CRITICAL 로그 목록
        out.write("## 4. WARNING 및 CRITICAL 로그 상세 리스트\n")
        if not warning_critical_logs:
            out.write("*분석된 로그 중 WARNING 이나 CRITICAL 등급의 로그가 존재하지 않습니다.*\n")
        else:
            out.write("| 발생 시간 | 장비명 (Device) | 등급 | 이벤트 | 상세 메시지 |\n")
            out.write("| --- | --- | --- | --- | --- |\n")
            for item in warning_critical_logs:
                out.write(f"| {item['timestamp']} | `{item['device']}` | **{item['severity']}** | {item['event']} | {item['message']} |\n")
        out.write("\n")

        # 5. CRC_ERROR, LINK_DOWN, TICKET_ESCALATED가 포함된 주요 이벤트 요약
        out.write("## 5. 핵심 인시던트 주요 이벤트 요약\n")
        out.write("이 섹션은 하드웨어 결함이나 장애 전파와 관련된 핵심 키워드(**CRC_ERROR, LINK_DOWN, TICKET_ESCALATED**) 관련 요약입니다.\n\n")
        
        if not major_events:
            out.write("*핵심 키워드가 포함된 주요 인시던트 이벤트가 발견되지 않았습니다.*\n")
        else:
            out.write("| 구분 (Category) | 발생 시간 | 장비명 (Device) | 이벤트 | 상세 내용 |\n")
            out.write("| --- | --- | --- | --- | --- |\n")
            for item in major_events:
                out.write(f"| `{item['category']}` | {item['timestamp']} | `{item['device']}` | {item['event']} | {item['message']} |\n")
        out.write("\n")

        out.write("---\n")
        out.write("*분석 완료 시간: 2026-07-19 (DCO 인턴십 교육용 자동 분석 보고서)*\n")

    print(f"분석 성공! 결과가 다음 경로에 저장되었습니다: {OUTPUT_FILE}")

if __name__ == "__main__":
    analyze_logs()
