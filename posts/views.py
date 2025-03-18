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
