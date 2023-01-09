# 모듈(Module)
- 모듈(module): 다양한 기능을 하나의 파일로
- 패키지(package): 다양한 파일을 하나의 폴더로
- 라이브러리(library): 다양한 패키지를 하나의 묶음으로
- 관리자(pip): 이것을 관리하는 관리자

## 모듈과 패키지
### 모듈
- 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것.
- `파이썬 표준 라이브러리`를 통해 기능들 확인하면 됨.
```python
import random
의사 난수 생성 모듈
import datetime
날짜아 시간을 조작하는 객체 제공
import os
OS를 조작하기 위한 인터페이스 제공
from pprint import pprint
pprint(): 예쁘게 정보를 나열해줌
```

### 패키지
- 패키지: 특정 기능과 관련된 여러 모듈의 집합
```python bash
$ pip install Somepackage
$ pip uninstall Somepackage
$ pip list
```