# GPS와 칼만필터·파티클필터로 캠퍼스에서 내 위치 찾기

2026년도 가을학기 로봇 알고리즘(SWE4007) 프로젝트

- 참여자: 2021245017 공지혁
- 진행 형태: 개인
- 팀 번호: 16
- GitHub ID: kjhmoon
- 저장소 이름: `RobotAlgorithm-GPS-Localization-team16`
- 현재 단계: 기본 파일 업로드 및 clone 검증 완료, 1주차 보고서 작성 준비

## 실행

Python 3.10 이상에서 저장소 최상위 폴더를 기준으로 실행합니다.
현재 환경 확인 스크립트는 Python 표준 라이브러리만 사용합니다.

```powershell
python src/check_environment.py
python week1/src/check_environment.py
```

## 폴더 사용법

- `src/`: 작업 중인 프로젝트 코드
- `week1/src/`: 1주차 제출 시점의 코드 복사본 (zip 파일 사용 금지)
- `week1/README.md`: 1주차 코드 실행법과 하이퍼파라미터
- `week1/reports/`: 1주차 보고서와 `figures/`의 그림
- `week2/` ~ `week4/`: 이후 주차용 구조만 준비한 상태

주차 제출 전에 작업 코드를 해당 주차의 `src/`에 복사하고,
해당 주차의 README와 보고서를 실제 결과에 맞게 갱신합니다.

## 1주차 진행 상황

- [x] 개인 제출에 사용할 팀 번호 확인: 16
- [x] GitHub ID를 `team.md`에 기입: kjhmoon
- [x] 지정 이름의 GitHub 저장소 생성 및 본인 계정으로 commit/push
- [x] GitHub 웹페이지에서 업로드 확인
- [x] 새 폴더에 clone 후 파일과 실행 확인
- [ ] Arduino IDE 2.x 설치/버전 확인
- [ ] 아래 배경지식 6문항의 보고서 작성
- [ ] Git 과정의 실제 결과와 확인 자료를 보고서에 포함
- [ ] 보고서 이름을 `team16_week1.pdf` 등으로 지정

## 보고서에 답할 문항

1. 경로 계획 문제에 샘플링이 필요한 이유와 수업에서 학습한 해당 방법
2. 칼만 필터(KF)의 개념과 필요한 상황
3. 파티클 필터의 개념과 필요한 상황
4. 안내문의 “Important sample”의 의미와 파티클 필터에서의 필요성
   (문맥상 importance sampling을 가리키는 것으로 보이며, 작성 시 용어 확인)
5. Localization 문제를 푸는 이유와 대응하는 현실 문제
6. Occupancy grid map의 개념과 센서 측정으로 만드는 방법

GitHub 업로드와 새 폴더 clone 후 실행 검증은 완료했습니다.
Arduino IDE 확인과 최종 보고서 작성은 아직 남아 있습니다.
