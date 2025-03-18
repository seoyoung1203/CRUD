from django.shortcuts import render, redirect
from.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post':post,
    }

    return render(request, 'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    # 정보 뽑기
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 빈칸 만들기 (셸 만들기)
    post = Post()
    # 값 넣기
    post.title = title
    # 컬럼 이름   데이터
    post.content = content
    # 데이터 베이스에 저장
    post.save()

    # return render(request, 'create.html') >> html 페이지를 보여주는 것이 목적
    # return redirect('/index/')
    return redirect(f'/posts/{post.id}/')
    # f ''>> 문자열 안에 변수를 넣기 위함


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/posts/')


def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'edit.html', context)

def update(request, id):
    # 기존정보 가져오기
    post = Post.objects.get(id=id)

    # 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 기존 정보를 새로운 정보로 바꾸기
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
