# Django - Authentication System
## 1. 개요
### 인증 시스템
- 사용자 인증과 관련된 기능을 모아 놓은 시스템
- 인증과 권한 부여를 함께 제공 및 처리
### Authentication(인증)
- 사용자가 자신이 누구인지 확인하는 것(신원 확인)
### Authorization(권한, 허가)
- 인증된 사용자가 수행할 수 있는 작업을 결정(권한 부여)

## 2. Custom User model
## 3. Login
- Session을 Create하는 과정
## 4. Logout
- Session을 Delete하는 과정

## 5. 회원 가입
- User 객체를 Create 하는 것
### UserCreationForm()
- 회원 가입을 위한 built-in **ModelForm**

## 6. 회원 탈퇴
- User 객체를 Delete 하는 것

## 7. 회원정보 수정
- User 객체를 Update 하는 것
### UserChangeForm()
- 회원 가입을 위한 built-in ModelForm

## 8. 비밀번호 변경
### PasswordChangeForm()
- 비밀번호 변경을 위한 bulit-in Form

## 9. 로그인 사용자에 대한 접근 제한
