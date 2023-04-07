# Django - Understanding Django and framework

## 1. Framework
- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
- 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공

### Why use?
- 기본적인 규조와 규칙을 제공하기 떄문에 필수적인 개발에만 집중 할 수 있음
- 여러 라이브러리를 제공해 개발 속도를 빠르게 함
- 유지보수와 확장에 용이해 SW의 품질을 높임

## 2. Django
- 파이썬 기반의 대표적인 웹 프레임워크
- Spotify, Instagram, Dropbox, Delivery Hero 등 대규모 서비스에서도 안정적인 서비스 제공

## 3. 클라이언트와 서버
### 웹의 동작 방식
- 클라이언트 - 서버 구조
- 클라이언트 -> 서버 (리퀘스트)
- 서버 -> 클라이언트 (응답)

#### Client
- 서비스를 요청하는 주체(웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)

#### Server
- 클라이언트의 요청에 응답하는 주체(웹 페이지, 앱을 저장하는 컴퓨터)

## 4. django 프로젝트 및 가상환경
### django 프로젝트 생성전 루틴

> 서버 종료 할 떄: `ctrl + c`

```bash
# 1. 가상환경(venv) 생성
$ python -m venv venv

# 2. 가상환경 활성화
$ source venv/Scripts/activate

# 3. django 설치
$ pip install django==3.2.18
## 버전을 명시하지 않으면 4.0버전이 설치되니 주의

# 4. 의존성 파일 생성(패키지 설치마다 진행)
$ pip freeze > requirements.txt
```

> 가상환경에 들어가는 개념이 아니라 `on/off` 개념임 / 어디서든 가상환경일 수 있음
> 끄고 싶다면 `deactivate` 혹은 베쉬 자체를 끄기

### django 프로젝트 생성
```bash
$ django-admin startproject projectname .
# .은 현재 위치를 의미
```
> 필수 암기 명령어

### django 서버 실행
```bash
$ python manage.py runserver
# manage.py와 동일한 경로에서 명령어 진행
```
### 페어 입장
- 의존성 문서로 가상환경 버전들 설치하는 명령어
```bash
$ pip install -r requirements.txt 
```
- 서로 가상환경 자체를 공유하지 않는다. 받은 문서로 알아서 가상환경들을 조성해야 함.

## 99. 참고
### django 프로젝트 생성 루틴 정리
1. 가상환경 생성
2. 가상환경 활성화
3. django 설치
4. 의존성 파일 생성(패키지 설치시마다 진행)
> (5, 6) git 관련 설정시에 진행
5. .gitignore 파일 생성
6. git 저장소 생성
7. django 프로젝트 생성

### 가상환경을 사용하는 이유
- 의존성 관리: 라이브러리 및 패키지를 각 프로젝트마다 독립적으로 사용 가능
- 팀 프로젝트 협업: 모든 팀원이 동일한 환경과 의존성 위에서 작업하여 버전간 충돌을 방지

### LTS(Long-Term Support)
- 프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 떄 사용
- 기업이나 대규모 프로젝트에서 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요

### gitignore 설정 서비스
- <https://www.toptal.com/developers/gitignore/>

