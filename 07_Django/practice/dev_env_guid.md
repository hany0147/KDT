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

## 6. 앱 생성 및 등록
### 6-1 앱 생성
- application: 독립적으로 작동하는 기능 단위 모듈 / 각기 특정 기능을 담당하며 다른 앱과 함께 프로젝트 구성함
```bash
$ python manage.py startapp 앱 이름
# 앱 이름은 복수형을 권장
```
### 6-2 앱 등록
- 프로젝트 폴더 안, `settings.py` 파일 안에 등록
- 반드시 앱을 생성하고 등록해야 함
  - 반대로 할 경우 생성 불가능
- INSTALLED_APPS 객체 안에 (1)생성 앱 (2) 설치 앱 (3) 기본 앱 순으로 기재 추천
```python
INSTALLED_APPS = [
  '앱 이름',
  ...,
  ]
```

## 7. MTV의 이해
- Model: DB
  - models.py
- Template: 보여지는 것
  - 미리 생성되어 있지 않음
    - django는 백엔드 프레임워크이기 때문에 JSON으로 프론트앤드와 대화하기 때문에 Template을 무조건 생성할 필요가 없기 때문에
  - 폴더는 무조건 `templates`로 생성하는 게 국룰
- View: 작동(controller)
  - views.py

## 8. 요청과 응답 
### 원리
- 요청 -> urls.py -> views.py -> templates or models.py -> views.py -> 응답

### 8-1 URLs
```python
urlpatterns = [
  path('admin/', admin.site.urls),
  path('앱 이름/', views.index),
  # 앱 자체가 __init__.py에 의해 패키지가 되기 때문에 from~import~로 함수 모듈을 추출할 수 있다
]
```
- 요청이 오면, views 모듈의 index 뷰 함 수를 호출한다는 의미
### 8-2 View
```python
def index(request):
  return render(request, '앱 이름/index.html')
  # 무조건 request로 인자를 입력하는 게 국룰
  # app 폴더/templates 까지는 django가 자동으로 경로를 확보해주기 때문에 그 이후부터 경로를 입력하면 된다.
```
- 특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환하는 index 뷰 함수 정의
- render 함수
  ```python
  render(request, template_name, context)
  ```
  - request: 응답을 생성하는 데 사용되는 요청 객체
  - template_name: 템플릿 이름의 **경로**
  - context: 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)

### 8-3 Template
- 앱 폴더 내에 `templates` 폴더 생성하고 그 안에 템플릿 페이지 작성(ex: index.html)

## 9.모델 마이그레이션
### 9-1 모델 클래스 생성
```python
# app_name/models.py
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
    # 필드 이름(변수명) / 데이터 타입(모델 필드 클래스) / 제약 조건(모델 필드 클래스의 키워드 인자)
    # 하나하나가 클래스 변수명
    # id는 django가 알아서 셋팅해줌
    # textfield 메서드는 길이 제한이 없음 / charfield는 길이 제한을 걸어야 함
```

### 9-2 모델 설계도 생성
```bash
$ python manage.py makemigrations
```
- 만약 추가 생성인 경우 default 값을 추가하거나 null값을 허용하는 옵션을 택해야 migration 파일이 생성됨
- 해당 앱의 migrations 폴더에 들어가면 새로 생성된 설계도를 확인 할 수 있다.

### 9-3 모델 DB 반영
```bash
$ python manage.py migrate
```
- 해당 명령문을 입력하지 않으면 설계도에 지나지 않음
- DB 반영까지 완료하고 db.splite3에서 테이블 생성됐는지 확인 필요

## 10. 관리자 관련
### 10-1 관리자 페이지 등록
- admin.py에 들어가서 모델을 관리자 페이지에 등록해야 한다.
```python
from .models import model_name
# 매번 models 모듈을 앞에 입력하기 번거로우므로 from에 .models를 입력한다.
admin.site.register(model_name)
# 암기 꿀팁: 관리자 사이트에 등록한다 모델을
```
### 10-2 관리자 계정 생성
```bash
$ python manage.py createsuperuser
```
- email은 선택사항
- 비밀번호는 보안 떄문에 입력되는 게 보이지 않는다.

### 10-3 관리자 페이지 확인
- 서버를 열고 /admin/ 경로로 들어가 로그인하고, 모델에 자료를 입력하고 db에서 데이터가 생성되는지 확인할 수 있다.