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
    post = Post.objects.get(id=id) # 하나만 불러올 것이기 때문에 단수

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)

def new(request):
    # 공간만 만들어주는 것이기 때문에 바로 return
    return render(request, 'new.html')

def create(request):
    
    # 정보 뽑기
    title = request.GET.get('title')
    content = request.GET.get('content')
   
    # 빈칸 만들기 (셸 만들기)
    post = Post()
   
    # 값 넣기(title로 채우기)
    post.title = title
    
    # 값 넣기(title로 채우기)
    post.content = content
#   컬럼  이름      데이터
    
    # >>> 파이썬으로 존재하는 데이터
    # > 데이터 베이스에 저장
    post.save()

    # return render(request, 'create.html') >> html 페이지를 보여주는 것이 목적
    # return redirect('/index/')
# >>
    # 만든 게시물 확인
    # 이미 만들어진 html에 다시 들어감 >> redirect ()
    return redirect(f'/posts/{post.id}/') 
                            # post.id : 틀 post의 id
    # f ''>> 문자열 안에 변수를 넣기 위함

# Delete

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
# 글을 삭제했으면 볼 수 없기 때문에 목록으로 다시 돌아가기
    return redirect('/posts/')

# 글 수정하러 들어가기 (수정할 게시물 찾기)
def edit(request, id):
    post = Post.objects.get(id=id)

# 바로 못 넣음! context 활용
# 딕셔너리 형태로 context에 데이터를 저장
    context = {
        'post': post,
    }
# html에서 나타내기 위해서 반환 사용
    return render(request, 'edit.html', context)

# Update

def update(request, id):
    # 기존정보 가져오기
    post = Post.objects.get(id=id)

    # 사용자가 적은(request) 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 기존 정보를 새로운 정보로 바꾸기(재할당)
    post.title = title
    post.content = content

    # 새로 들어온 데이터 저장
    post.save()

    # detail URL로 들어가기 > 재출력
    return redirect(f'/posts/{post.id}/')
