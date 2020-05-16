### **vscode에서  장고 설치하는 법**
<br/><br/>

## *가상 환경 실행 방법
<br/>
1. python --version

-python 버젼 확인을 통해 제대로 파이썬이 깔려있는지 확인한다.
<br/><br/><br/>

2. 가상환경 생성

-python -m venv <가상환경 이름>

ex)python -m venv myvenv
<br/><br/>

3. 가상환경 구동

git bash 사용 : source myvenv/Scripts/activate

cmd 사용 : myvenv\Scripts\activate

(저는 bash root 파일에 문제가 생겨서 결국 고치는건 포기하고 vscode 터미널 디폴트로 cmd를 쓰고 있습니다😢)

<br/><br/>

4. 가상환경 빠져나오기(활성화 종료)

deactivate
<br/><br/>

 

## *설치 및 삭제
장고 설치(가상환경 켜놓고 실행)

pip install django
<br/><br/>
 

장고 삭제

pip unintall django
<br/><br/>

## *서버 켜고 끄기
서버 켜기
-python manage.py runserver   

<br/>

서버 끄기

-ctrl-c   

<br/><br/><br/>

 

## <django 기본 흐름>
<br/>

1. 프로젝트 만들기<br/>

django-admin startproject <프로젝트 이름>

 ex) django-admin startproject djangoproject01
<br/><br/>
 

2. 프로젝트의 작은 부분인 app만들기

python manage.py startapp < app이름 >

ex)python manage.py startapp myapp
<br/><br/>


+)app : 프로젝트를 이루는 작은 단위  

<br/><br/>

3. app을 하나 만들고 프로젝트 폴더 내의 setting.py안에 들어가서 새 app이 만들어졌다고 알려줘야됨(프로젝트와 app 연결 )


-wordcount라는 app 생성 시 위와 같이 setting.py의 installed_apps의 가장 아랫줄에 경로를 추가해주도록 한다.
<br/><br/>
 

4. template 폴더 생성

-app안에서는 user에게 보여질 화면 html을 만들어 준다.
<br/><br/>
 

5. views.py

-user에게 보여질 화면 html이 언제, 어떻게 처리될 지 알려주는 '함수'작성
<br/><br/>

 

6. url.py

-내가 만든 html이 어떤 url을 입력 했을 때 뜨게 할 지 결정
<br/><br/>

 

7. python manage.py runserver

-서버를 돌리면 html 파일 나타남
<br/><br/>

 

8. ctrl+c

-서버 끄기
<br/><br/><br/>

 

 

## Django 구동 원리
<br/>

MTV 패턴 
<br/>

Model-데이터 담당

Template-화면 보여주기 담당

View-처리 담당  
<br/><br/>
 

MVC 패턴

-MTV가 차용한 방식으로 좀 더 일반적인 패턴 

<br/><br/> 

Model-DB담당

View-사용자에게 보여지는 부분 담당

Controller-중간 관리 담당