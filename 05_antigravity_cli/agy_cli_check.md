# Antigravity CLI (agy) 설치 및 실행 확인 체크리스트

본 문서는 **교육용 실습 환경**에서 `antigravity-cli (agy)` 도구를 설치하고 실행을 검증한 기록입니다. 포트폴리오 가이드라인에 따라 실제 인프라 정보나 인증키 등의 민감 정보는 포함하지 않습니다.

---

## 1. 검증 환경 정보

### 1) 운영체제 (OS)
- [ ] Windows 10/11 (Home/Pro)
- [ ] macOS (Sequoia/Sonoma 등)
- [ ] Linux (Ubuntu/RHEL 등)
- *상세 버전:* `Windows 11 Home 23H2`

### 2) 사용한 터미널 (Terminal)
- [ ] PowerShell (버전 7.x 이상 권장)
- [ ] Windows Command Prompt (CMD)
- [ ] WSL2 (Ubuntu)
- [ ] macOS Terminal / iTerm2
- *상세 버전:* `PowerShell 7.4`

---

## 2. CLI 실행 검증

### 3) `agy --version` 결과
터미널에서 버전을 조회하여 정상 설치 여부를 확인합니다.
- [ ] 실행 성공 여부: **성공** / **실패**
- [ ] 출력된 버전 정보: (예: `agy version 2.0.0-beta.4`)

```bash
$ agy --version
agy version 2.0.0-beta.4 (Sample Output)
```

### 4) `agy` 실행 확인
도구의 기본 도움말 명령어(`--help`)를 호출하여 실행 가능 여부를 체크합니다.
- [ ] `agy --help` 실행 성공 및 명령어 목록 정상 출력 확인

```bash
$ agy --help
Usage: agy [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  login      Authenticate with the demo portal
  status     Check connection to the dummy cluster
  diagnose   Run a simulated diagnostics report
```

---

## 3. 인증 및 트러블슈팅 기록

### 5) 로그인 또는 실행 확인 메모
- **인증 방식**: 교육용 가상 인증 토큰을 활용한 샌드박스 환경 로그인 검증.
- **실행 메모**:
  - `agy login` 명령어를 실행하여 교육용 로컬 목(Mock) 서버에 세션 연결 성공.
  - 가상 엔드포인트(`https://demo-api.dco-edu.local`) 간의 통신 검증 완료.

### 6) 오류 해결 로그 (Troubleshooting Log)
*실습 과정에서 겪은 에러와 해결 프로세스를 기록하여 문제 해결력을 입증합니다.*
- **현상**: Windows PowerShell에서 `agy` 명령어 입력 시 "스크립트 실행 권한 제한" 오류(`PSSecurityException`) 발생.
- **원인**: Windows OS의 기본 실행 정책(Execution Policy)이 `Restricted`로 되어 있어 스크립트 실행이 차단됨.
- **조치**: PowerShell을 관리자 권한으로 실행한 후, 현재 사용자 스코프의 실행 정책을 변경하여 해결.
  ```powershell
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### 7) 보안상 입력하지 않은 정보
보안 가이드라인을 준수하여 아래의 실제/민감 데이터는 본 문서에 기록하지 않거나 가상 데이터로 처리했습니다.
1. **실제 AWS 계정 정보 및 Credentials (Access Key / Secret Key)**
2. **실습 포털의 실제 로그인 비밀번호 및 MFA 인증 토큰**
3. **더미 환경이 아닌 실제 엔드포인트 서버의 IP 주소 및 도메인**
