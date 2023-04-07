# Django - django URLs
## 1. 개요
### URL dispatcher
- 분배기
- URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

## 2. 변수와 URL
### Variable Routing
- URL 일부에 변수를 포함시키는 것
- 변수는 view 함수의 인자로 전달할 수 있음
### 작성법
- `<path_converter:variable_name>`
```python
path('articles/<int:num>/', views.hello)
```
- Path converters: url 변수의 타입을 지정(str, int 등 5가지 타입 지원)
  - str은 기본값이라 생략 할 수 있음 (ex: `<name>`)

## 3. App의 URL
### App URL mapping
- 각 앱에 URL을 정의하는 것
- 프로젝트와 각각의 앱이 URL을 나누어 관리하여 주소 관리를 편하게 하기 위함

### include()
- 다른 URL들을 참조할 수 있도록 돕는 함수
- URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분은 후속처리를 위해 include된 URL로 전달

## 4. URL 이름 지정
### Naming URL patterns
- URL에 이름을 지정하는 것(path 함수의 name 인자를 정의해서 사용)
### 'url' tag
- 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
```python
{% url 'url_name' arg1 arg2 %}
```

## 5. URL Namespace
### app_name 속성 지정
```python
app_name = 'app_name'
{% url 'app_name:url_name' %}
```

> NoReverseMatch 문제다? 무조건 url관련 문제다!

## 99. 참고
### app_name 지정 후 주의사항
- app_name을 지정한 이후에는 url태그에서 반드시 `명찰`을 다는 형태로만 사용할 수 있음
- 그렇지 않으면 `NoReverseMatch`에러 발생

### Trailing Slashes
- django는 URL 끝에 '/'가 없다면 자동으로 붙임-
- 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이 두 주소(foo.com/bar와 foo.com/bar/)를 서로 다른 페이지로 봄
- 그래서 django는 검색 엔진이 혼동하지 않게 하기 위해 사용
  - 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님 