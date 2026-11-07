# 1주차

- 참여자: 2021245017 공지혁 (개인 진행)
- 팀 번호: 16
- GitHub ID: kjhmoon
- 목표: 환경 세팅, Git 실습, 배경지식 정리

## 실행법

새 폴더에 저장소를 clone한 후, 저장소 최상위 폴더에서 실행합니다.
Python 3.10 이상이 필요하며 추가 패키지는 없습니다.

```powershell
python week1/src/check_environment.py
```

Python 버전과 1주차 필수 파일/디렉터리의 존재를 확인합니다.
실행 위치가 저장소 최상위가 아니면 필수 파일을 찾지 못할 수 있습니다.
이 스크립트는 GitHub 업로드 여부, 보고서 완성도, Arduino 설치 여부를 검사하지 않습니다.

## 하이퍼파라미터

현재 포함된 환경 확인 스크립트에는 하이퍼파라미터가 없습니다.
GPS 처리 및 필터 코드는 이후 과제 안내에 따라 추가합니다.

## 보고서

`reports/`에 Git 실습 결과와 배경지식 6문항의 보고서를 작성해야 합니다.
보고서 이름은 `team16_week1.pdf` 등 안내에 맞는 이름을 사용합니다.
보고서 그림은 `reports/figures/`에 저장합니다.

## Git 실습 확인 기록

- 저장소: https://github.com/kjhmoon/RobotAlgorithm-GPS-Localization-team16
- 브랜치: `main`
- 초기 업로드 커밋: `27b94b5b8c97559c1c3a687849b7703e2a86d415`
- 커밋 작성자: 공지혁 (`163113764+kjhmoon@users.noreply.github.com`)
- GitHub 웹페이지에서 필수 폴더, 자기소개, `team.md`가 표시되는 것을 확인했습니다.
- 별도의 새 폴더에 clone한 뒤 아래 두 명령을 실행했습니다.

```powershell
python src/check_environment.py
python week1/src/check_environment.py
```

두 명령 모두 Python 3.13.15에서 Python 버전 조건과 1주차 파일 구조 검사를 통과했습니다.
이 기록은 Git 실습 확인 내용이며, 배경지식 6문항을 포함한 최종 보고서는 별도로 작성해야 합니다.
