# 개발 환경 설정 가이드
## 0. 깃 환경 조성
### 0-1 .gitignore 만들기
- [gitignore 코드 생성 사이트](https://www.toptal.com/developers/gitignore/)
- python, window, mac, django, VScode 키워드 입력하기

> 주의: **`git add .`전**에 만들자!

### 0-2 git 생성
```bash
$ git init
```

## 1. 가상환경 생성 및 활성화
### 1-1 가상환경 생성
```bash
$ python -v venv venv
# 맨 뒤에 자유롭게 이름 설정 가능하나 venv가 국룰이므로 무조건 venv를 써라. 왜냐하면 .gitignore에서도 /venv 라는 요소가 포함되기 때문
```
### 1-2 가상환경 활성화
```bash
# 1. python bash 환경
$ source venv/Scripts/activate

# 2. VS code 환경
## 2-1 ctrl + shift + p를 누른다.
## 2-2 interpreter를 검색한다.
## 2-3 python 가상 환경을 클릭한다.
```
> 비활성화 방법: deactivate 입력 또는 bash 창을 끈다.

## 2. django 설치
### 2-1 가상 환경 들어 왔는지 선 확인
- bash 터미널에 (venv)가 붙어 있다면 가상환경에 들어 온 것이다.
- 또는 `pip list` 명령어 입력하여 가상환경 인지 확인하라

### 2-2 django 설치
```bash
$ pip install django==3.2.18
``` 
- django만 입력하면 4.x 버전으로 설치되기 떄문에 주의 해야한다.
- LTS는 현재 3.2X 버전이다.

## 3. 의존성 파일 생성
```bash
$ pip freeze > requirements.txt
```
- requirements 또한 국룰!

- 페어 조원의 입장이라면 하단의 입력어를 통해 가상 환경을 일치시켜야 한다.
```bash
$ pip install -r requirements.txt
```
## 4. django 프로젝트 생성
```bash
$ django-admin startproject 프로젝트 이름 .
# '.'은 현재 위치를 의미하므로 프로젝트 이름 뒤에 한 칸 띄고 꼭 입력해야 함
```

## 5. django 서버 실행
### 5-1 서버 실행 명령어 입력
```bash
$ python manage.py runserver
# manage.py와 동일한 경로상에서 명령어 진행해야 함.
# manage.py 뒤에 다양한 명령어가 들어 갈 수 있음
```
### 5-2 url 클릭
- 터미널에 입력된 링크 접속
- 🚀 확인되면 성공!