# Django - Django Model
## 1. 개요
- Model을 통한 DB 관리(**Model != DB**)
- SQLite: 오픈소스 RDBMS 중 하나이며 django의 기본 DB로 사용됨(DB가 파일로 존재하며 가볍고 호환성이 좋음)

## 2. Model
### django Model
- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
- 테이블 구조를 설계하는 **청사진**
```python
# models.py
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
    # 필드 이름(변수명) / 데이터 타입(모델 필드 클래스) / 제약 조건(모델 필드 클래스의 키워드 인자)
    # 하나하나가 클래스 변수명
    # id는 django가 알아서 셋팅해줌
    # textfield 메서드는 길이 제한이 없음 / charfield는 길이 제한을 걸어야 함
```

## 3. Migrations
- model 클래스의 변경사항(필드 생성, 추가 수정 등)을 DB에 최종 반영하는 방법
- model class => migration 파일(설계도) => db.sqlite3
```bash
$ python manage.py makemigrations
# model class 기반으로 설계도 작성

$ python manage.py migrate
# 만들어진 설계도를 DB에 전달하여 반영
```
### 추가 모델 필드 작성
- 추가 생성이므로 장고에서 기본 값 설정이 필요하다고 터미널에서 언급함
- 설계도를 계속 쌓아가며 기록하는 이유: 변화 시점들을 기록하여, 문제가 생겼을 경우 과거로 롤백하기 위함
- model class에 변경사항이 생겼다면, 반드시 새로운 설계도를 생성하고, 이를 DB에 반영해야 한다.
### 필드 유형
1. CharField(): 길이 제한이 있는 문자열을 넣을 떄 사용(max_length 필수인자)
2. TextField(): 글자 수 많을 떄 사용
3. DateTimeField(): 날짜와 시간 넣을 떄 사용 
    - 선택인자
      - auto_now: 데이터가 저장될 때마다 자동으로 현재 날짜 시간을 저장 (수정날짜에 적합)
      - auto_now_add: 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장(생성날짜에 적합)

## 4. Admin site
### Automatic admin interface
- django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
- 데이터 관련 테스트 및 확인을 하기에 매우 유용

### admin 계정 생성
```bash
$ python manage.py createsuperuser
```
- email은 선택사항
- 비밀번호 생성 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가도록 함

### admin에 모델 클래스 등록
- admin.py에 등록하지 않으면 admin site에서 해당 모델을 확인할 수 없음
```python
# admin.py
from django.contrib import admin
from .models import Article
admin.site.register(Article)
```

- 시간은 UTC로 기본 저장됨

## 99. 참고
### Migrations 기타 명령어
```bash
$ python manage.py showmigrations
# migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
# [X] 표시가 있으면 migrate가 완료됐음을 의미

$ python manage.py sqlmigrate articles 0001
# 해당 migrations 파일이 SQL문으로 어떻게 해석되어 DB에 전달되는지 확인하는 용도
# SQL을 확인하는 용도
```
