# Web - Grid system fro responsive web design
## 1. 개요
### Responsive Web Design
- 디바이스 종류나 화면의 크기에 상관없이, 어디에서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
- 부트스트랩 그리드 시스템의 12개 column과 **6개의 breakpoints**를 사용하여 반응협 웹 디자인을 구현

## 2. Grid system Breakpoints
### Grid system breakpoints
- 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
- 화면 너비에 따라 6개의 분기점 제공: xm, sm, md, lg, xl, xxl
- 각 브레이크포인트마다 설정된 최대 너비 값 **이상으로** 화면이 커지면 그리드 시스템 동작이 변경됨
```html
<div class="col-sm-6"></div>
```
> sm의 사이즈에선 6개의 컬럼을 차지하겠다.

#### offset
- 특정 브레이크포인트에 적용했고, 이후 사이즈에는 적용하지 않으려면 리셋해주어야 한다.


## 99. 참고
### Grid cards
- row-cols 클래스를 사용하여 행당 표시할 열(카드) 수를 손쉽게 제어 할 수 있음
- 12개의 컬럼에서 카드를 몇 개 표시할 지 개수의 의미를 지님
  - 컬럼 칸 수를 의미하는 게 아님
- 행(row)에서 컨트롤함
```html
<div class="row row-cols-1 row-cols-md-2">
```