# balance_6

## 1. 앱 만들기
0. crud - setting
1. accounts
2. posts

## 2. accounts
### 1. 회원가입
- forms.py -> fields : username, email, password
### 2. 로그인
### 3. 로그아웃

## 3. posts
### 0. 인덱스 페이지
### 1. 밸런스 게임 생성(create)
0. 모델
- forms.py -> fields : title, select1_content, select2_content
- 관계
    - auth_user_model - select1_user (n:n)
    - auth_user_model - select2_user (n:n)
    - auth_user_model - post_user (1:n)
- models.py -> fields : title, select1_user(ManyToMany), select1_content, select2_user(ManyToMany), select2_content, user(foreign-key)

1. url / views
2. template
### 2. 밸런스 페이지 조회(detail)
1. url / views
2. template
### 3. 밸런스 선택(answer)
1. url / views 
    - 선택지를 한 번 선택하면 취소하거나 다른 선택지를 선택할 수 없다.
    - 각 선택지 버튼에는 선택을 한 유저의 수를 출력한다.
2. template
3. 비동기 구현
### 4. 이미지 삽입
    - 이미지킷
### 5. 댓글 기능 구현
    - 생성
    - 삭제
### 6. 좋아요 기능 구현
    - 로직
    - 비동기
### 7. 팔로우 기능 구현
    - 유저 모델 수정
    - 프로필 페이지
    - 로직
    - 비동기

## 3. 기타
### 1. 디자인 구현
0. 글씨체(공통)
    - 다 같이 논의해서 넣는 걸로
1. 폼 수정(이수정) [forms.py] 
    - 로그인 폼
    - 회원가입 폼
    - 게시글 생성 폼
    - 댓글 폼
2. nav 바(랭크(10위) - 협업, 만들기(create)) [nav.html]
    - 브랜드(홈 버튼 꾸미기 ^^)(장하늬)
3. 페이지네이터 구현(장민지) [index]
4. 디테일 창 꾸미기(최은비) [detail]
5. 푸터 꾸미기(장하늬) [footer.html]

### 2. 기능 수정 및 추가
1. 게시글 삭제 / 수정
2. 프로필 페이지에서 본인이 선택 인자들이 무엇인지 조회기능 추가(~님은 ~~을 좋아합니다.)
3. 댓글 수정
4. 팔로우 한 걸 모달이나 collapse로 보여주기 ㅎ히히(프론트엔드 + 백엔드 협업)
5. 디테일에서 본인이 선택한 선택지가 무엇인지 테두리에 노란색으로 표시(체크박스 띄우기 / 협업)
6. 비율 기능 구현

### 99. 기타
- 본인이 선택한 선택지에 따라 화면 변경
- 댓글 수정
