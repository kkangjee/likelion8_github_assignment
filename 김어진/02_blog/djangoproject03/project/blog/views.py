from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects 
    #model로 부터 전달받은 object list: query set
    #기능들을 표시해 주는 방법 : method
    #query set을 활용하게 해주는 것이 method
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

#new.html 을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

#입력받은 내용을 db에 넣어주는 함수
def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    #.save : 쿼리셋 메시지 중 하나로 blog에 넣은 모든 객체 db에 저장하는 메소드
    blog.save() 
    #blog.id는 int형인데 url은 항상 문자열이므로 str로 형 변환
    #redirect(url) : 위의 모든 함수를 수행 후에 url로 넘겨라
    return redirect('/blog/'+str(blog.id))


    #redirect와 render의 차이점
    #redirect : 상위 모든 코드 수행 후에 redirect 내의 인자 url이 띄워짐(외부 url도 상관 없음)
    #render : 파이썬 함수 내에서 생성한 내용을 html 상에서 data를 담아 처리하고 싶을 때 사용

