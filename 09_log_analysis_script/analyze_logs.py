# -*- coding: utf-8 -*-
"""
DCO 교육용 샘플 로그 분석 스크립트
작성자: Python 코드 작성 도우미 (인턴십 교육용)
"""
import os

# 입력 파일명과 출력 파일 경로를 설정합니다.
INPUT_FILE = "sample_dco_log.txt"
OUTPUT_DIR = r"C:\Users\admin_23\Desktop\AWS-DCO-GenAI-Portfolio\09_log_analysis_script"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "incident_summary.md")

def analyze_logs():
    # 1. 분석을 위해 필요한 변수들을 준비합니다 (초기화)
    total_lines = 0                     # 전체 로그 줄 수
    severity_counts = {}                # 심각도별 개수 저장용 딕셔너리
    event_counts = {}                   # 이벤트 종류별 개수 저장용 딕셔너리
    warning_critical_logs = []          # WARNING 또는 CRITICAL 로그 목록 리스트
    major_events = []                   # 주요 키워드 관련 이벤트 리스트

    # 입력 파일이 존재하는지 확인합니다.
    if not os.path.exists(INPUT_FILE):
        print(f"오류: 입력 로그 파일 '{INPUT_FILE}'을 찾을 수 없습니다.")
        return

    # 2. 로그 파일을 읽어와 한 줄씩 분석합니다.
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            total_lines += 1

            # 로그 형식: YYYY-MM-DD HH:MM:SS | DEVICE | SEVERITY | EVENT | MESSAGE
            parts = [part.strip() for part in line.split("|")]
            if len(parts) < 5:
                continue

            timestamp = parts[0]
            device = parts[1]
            severity = parts[2]
            event = parts[3]
            message = parts[4]

            # (1) 심각도별(SEVERITY) 개수 세기
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
            if severity in ["WARNING", "CRITICAL"]:
                warning_critical_logs.append({
                    "timestamp": timestamp,
                    "device": device,
                    "severity": severity,
                    "event": event,
                    "message": message
                })

            # (4) CRC_ERROR, LINK_DOWN, TICKET_ESCALATED가 포함된 주요 이벤트 요약 대상 식별
            event_upper = event.upper()
            msg_upper = message.upper()

            is_crc = ("CRC" in event_upper or "CRC" in msg_upper)
            is_link_down = ("LINK DOWN" in event_upper or "LINK_DOWN" in event_upper or "LINK" in event_upper and "DOWN" in event_upper)
            is_ticket_escalated = ("ESCALATED" in event_upper or "ESCALATED" in msg_upper)

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
                    "event": event,
                    "message": message
                })

    # 3. 분석한 결과를 지정된 마크다운 파일로 저장합니다.
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write("# 📋 DCO 교육용 샘플 로그 분석 보고서\n\n")
        out.write("이 보고서는 AWS DCO 인턴십 직무 이해를 돕기 위해 ...\n")