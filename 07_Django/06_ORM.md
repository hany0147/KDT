# Django - ORM
## 1. 개요
### ORM
- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

## 2. QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
- API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

### 구문
`Article.objects.all()`
- Article(Model class)
- objects(Manager)
- all()(Queryset API)

### Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청

### QuerySet
- DB에게서 전달 받은 객체 목록(데이터 모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
- 단, DB가 단일한 객체를 반환 할 때는 모델(Class)의 **인스턴스**로 반환됨

## 3. ORM CREATE
### django shell
- django 환경 안에서 실행되는 python shell
- 입력하는 QuerySetAPI 구문이 django 프로젝트에 영향을 미침

> .pk = .id

#### save()
- 객체를 데이터베이스에 저장하는 메서드

## 4. ORM READ
### 전체 데이터 조회
- all() 메서드
```bash
>>> Article.objects.all()
```
### 단일 데이터 조회 & 특정 조건 데이터 조회
```bash
>>> Article.objects.get(pk=1)
>>> Article.objects.filter(content='django!')
```
- get() 메서드: pk를 찾을 때 적합(데이터 단일 조회만 가능하기에)
- filter() 메서드: pk 외의 것을 조회할 떄(get 메서드와 달리 데이터가 없어도 에러가 뜨지 않고 빈 쿼리 셋을 반환함)

## 5. ORM UPDATE
- 원한느 값을 조회하고, 다시 변수를 재할당하면 수정이다.

## 6. ORM DELETE
- 인스턴스.delete()
- 삭제된 객체가 반환되는 게 특징

## 99. 참고

### 쿼리셋 API 관련 문서
<https://docs.djangoproject.com/en/3.2/topics/db/queries/>

### Field lookups
> __startswith = Like(SQL)
- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 filter(), exclude(), get()에 대한 키워드 인자로 지정됨
<https://docs.djangoproject.com/en/3.2/ref/models/querysets/>

### 어떻게 SQL문으로 번역되는지 확인하려면?
- print 안에 조회 명령어에 .query를 뒤에 붙이면 나옴