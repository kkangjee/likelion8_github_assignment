from django.shortcuts import render, redirect

# User에 대한 클래스
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    # 회원가입 내용을 작성하고 전송 -> POST 방식으로 전송
    if request.method == 'POST': 
        if request.POST['password1'] == request.POST['password2'] :
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            auth.login(request,user) # 로그인 함수
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password1']
        # authenticate : 데이터베이스에 입력한 내용이 있는지 확인
        user = auth.authenticate(request, username = username, password = password)
        if user is not None :
            auth.login(request, user)
            return redirect('home')
        else :
            return render(requet, 'login.html', {'error' : 'username or password is incorrect.'})
    else :
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')
