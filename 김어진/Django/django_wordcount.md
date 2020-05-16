# WORDCOUNT
<br/><br/><br/>

## Home.html
1. about 페이지와 링크로 연결

2. 사용자들로부터 입력을 받음

3. 결과 제출 버튼
<br/><br/>
 

## About.html
1.home 페이지와 링크로 연결

2,.about에 관련된 내용 적혀 있음
<br/><br/>
 

## Result.html
1.home 에서 입력 받은 데이터를 처리한 함수를 받아 “결과는 이러하다”를 출력
<br/><br/>


## View.py에 정의되어야 하는 함수
1. home을 띄우는 함수

2.about을 띄우는 함수

3.result에 전달할 함수(home에서 입력 받은 데이터를 처리하는 함수)->글자를 세주는 함수
<br/><br/>

 
 ******************

## 만들 URL
1.home 을 띄우는 url=뒤에 아무것도 안 붙는 url(e.g. mutsawordcount.com)

2.about을 띄우는 url=/about(e.g. mutsawordcount.com/about)

3.result를 띄우는 url=/result(e.g. mutsawordcount.coun/result)
<br/><br/>

## 템플릿 언어       
-html안에 쓰는 장고 제공 언어

-html안에 파이썬 변수/문법을 쓰고 싶을 때 사용  
<br/><br/>


## 템플릿 변수

-해당 파이썬 변수를 html파일에 담아 화면에 출력하라
<br/><br/>

## 템플릿 필터
{{value | length}} : value의 길이 반환

{{value | lower}} : value를 소문자로 출력
<br/><br/>

## 템플릿 태그
-html 상에서 파이썬 문법 사용, url 생성 등의 기능 제공

Ex) {%tag%}…태그내용…{%endtag%}}

>>html 태그처럼 장고의 템플릿 태그도 끝나는 태그가 있어야한다.
<br/><br/>

******************

<br/><br/>
 e.g. for 문

파이썬 파일

'Aclass=["민수", "영희","철수"]'
<br/>


HTML

"number of students={{class | length}}
{%for students in class%}
    {{students}}
{%endfor%}""
<br/><br/>
 

 1. number of students={{class | length}}

class라는 템플릿 변수에 length라는 템플릿 필터를 씌워 class라는 변수의 길이를 반환하라

-number of students는 3 반환
<br/><br/>

 

2.{%for students in class%}

python code상의 for문을 html상으로 나타낸 것

-class 전체를 순회 하면서 한 번 씩 students에 변수를 담아라
<br/><br/>
 

3.{{students}}

템플릿 변수 부분에서는 students 변수를 출력해라.
<br/><br/>

 

4.{%endfor%}

-장고의 템플릿 태그를 닫아 for문 종료
<br/>
<br/> 

 

e.g. URL생성

{%url ‘url_name’%}