# Django - Form
## 1. 개요
- HTML form: 사용자로부터 form 요소를 통해 데이터를 받고 있으나 비정상적 혹은 악의적인 요청을 확인하지 않고 모두 수용 중
  - 데이터 형식에 맞는지에 관한 '유효성 검증' 필요
### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
  - 입력 값, 형식, 중복, 범위, 보안 등 많은 걸 고려해야 하므로 이런 과정과 기능을 제공해주는 도구가 필요
  - 장고가 도구를 제공함

## 2. Django Form
- 사용자 입력 데이터를 수직하고, 처리 및 유효성 검증을 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공

### Form class 선언
```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=80)
    content = forms.CharField()
```
- .as_p

## 3. Widgets
- HTML 'input' element의 표현을 담당
- 위젯은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것
```python
# forms 클래스에서 위젯 추가
content = forms.CharField(widget=forms.Textarea)
```

## 4. Django ModelForm
### Form
- 사용자 입력 데이터를 DB에 저장하지 않을 때(ex. 로그인)

### ModelForm
- 사용자 입력 데이터를 DB에 저장해야 할 때(ex. 회원가입)
