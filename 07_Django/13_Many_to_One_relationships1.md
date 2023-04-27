# Django - Many to one relationships 01
## 1. 개요
- 관계형 데이터베이스의 N:1 관계
- 외래키(Foreign Key)를 어디에 둘 것인가?

## 2. Comment & Article
### 2-1 모델 관계 설정
- Many to one relationships: 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
  - Comment(N) - Article(1)
#### ForeignKey()
- django에서 N:1 관계 설정 모델 필드
```python
article = models.ForeignKey(ModelClass, on_delete=models.CASCADE)
```
- 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

### 2-2 관계 모델 참조
#### 역참조
- 나를 참조하는 테이블(나를 외래키로 지정한)을 참조하는 것
  - N:1 관계에서 1이 N을 참조하는 상황
```bash
article.comment_set.all()
# 모델 인스턴스.related manager.QuerySetAPI
```
- related manager: N:1 혹은 M:N 관계에서 역참조 시에 사용하는 manager
  - 참조하는 모델명_set

### 2-3 댓글 기능 구현
