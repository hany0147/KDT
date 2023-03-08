# Web - Fundamentals of Grid system

## 1. 개요
### Bootstrap Grid system
- 웹 페이지의 레이아웃을 조정하는 데 사용되는 **12개의 컬럼**으로 구성된 시스템
- 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시 할 수 있도록 도움

## 2. Grid system 클래스와 기본 구조
### 핵심 클래스
```html
<div class="container">
  <div class="row">
    <div class="col-4"></div>
    <div class="col-4"></div>
    <div class="col-4"></div>
  </div>
</div>
```
- 1개의 row안에 12칸의 컬럼 영역이 구성
- 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨