# GIT 1일차

## CLI
`Command Line Interface`의 약자로, `명령어 기반`의 인터페이스이다.
> <->`GUI`(Graphic User Interface)

### 명령어
- `ls`: 목록 확인
- `mkdir`: 디렉토리 생성
- `cd`: 디렉토리로 이동
> cd ..: 상위폴더로 이동
- `touch`: 파일 생성
- `rm` 폴더: 파일 삭제
- `rm -r` 폴더명: 폴더 삭제
- `pwd`: 현재의 디렉토리 출력

## GIT
분산 버전 관리 시스템
> 중앙집중 버전 관리 시스템과 달리 로컬에서 버전을 관리할 수 있다.

  - 버전: 컴퓨터 SW의 특정 상태(=`커밋`)

### GIT 명령어
  - 저장소 생성: `git init`
  - 변경된 파일 모으기: `git add <파일명>`
  - 버전으로 남기기: `git commit -m '메세지'`
  - 상태 확인: `git status`
  > working directory와 staging area의 정보를 확인 할 수 있다.
  - 버전 확인: `git log`

  - 기타: `git log -1`(최근 1개의 기록 확인), `git log --oneline`(한줄로 기록 확인), `git log -2 --oneline`(최근 2개의 기록을 한 줄로 확인)

