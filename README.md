# CRUD

## 0. setting
- 가상환경 생성
- 가상환경 활성화
- .gitignore 설정(python, window, macOS, Django)

## 1. Django
- pip install django
- 프로젝트 생성
```shell
django-admin startproject crud .
```
- 앱 생성, 등록
```shell
django-admin startapp posts
```

## 2. CRUD 

Create
Read
Update
Delete

 #### 첫번째
- modeling ('models.py') 틀 잡기(규격 설정)

```python
Class Post(models.Model):
    title = modles.CharField(max_length=100)
    content = models.TextField()
```
- migration
```shell
# 번역본 생성 >> html에 내가 작성한 페이지 
python manage.py makemigrartions
```

```shell
# DB에 반영(내용 채워넣기. 기능 만들기)
python manage.py migrate
```

- create super user (데이터가 없기 때문에 출력될 값을 만들기 위해 슈퍼유저를 생성 > 값을 만들어냄)
```shell
python manage.py createsuperuser
```

- admin 페이지에 모델 등록('admin.py')
```python
from django.contrib import admin
from.models import Post

- 빈 model을 admin에 등록
admin.site.register(Post)
```

### Read

- 전체 데이터 가져오기(모든 접근 가능한)
```shell
def index(request):
    posts = Post.objects.all() 모든 애들을 가지고 와서 posts라는 변수에 저장

  
    context = {
        'posts': posts
    }
    >> posts 데이터를 html에 보내준다 
```
----------
#### index.html
    p tag >> html의 str 문법 > 한 뭉탱이씩 만들어줌
    hr tag >> 구분줄


- 하나씩 뽑아오기
```shell
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>index</h1>
    {% for post in posts %}
        <p>{{post.title}}</p>
        <p>{{post.content}}</p>
    {% endfor %}
</body>
</html>
```

#### detail 만들기 작업
```shell
<body>
    <h1>detail</h1>
    <h2>{{post.title}}</h2>
    <p>{{post.content}}</p>
```
>> id 글 하나의 상세페이지만 보여주면 되기 때문에 

a tag >> 하이퍼링크(클릭하면 이동)



### create

1. 사용자에게 빈 종이 제공
2. 빈 종이에 내용을 입력
3. 입력된 내용을 create로 전송
4. 전송된 데이터 중에서 필요한 정보를 뽑아내고
5. DB에 저장

#### new 만들기 작업

```shell
def new(request):
    # 공간만 만들어주는 것이기 때문에 바로 return
    return render(request, 'new.html')
```
```shell
<body>
    <form action="/posts/create/">
        <input type="text" name="title">
        <input type="text" name="content">
        <input type="submit">
    </form>
```
-> 사용자 입력을 받을 수 있는 입력 필드 생성

### Update
```shell
 # 기존정보 가져오기
    post = Post.objects.get(id=id)

    # 새로운 정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 기존 정보를 새로운 정보로 바꾸기
    post.title = title
    post.content = content
    post.save()
```
#### edit

### Delete

1. 

### 코드 참고사항
- f ''>> 문자열 안에 변수를 넣기 위함
- return render(request, 'create.html') >> html 페이지를 보여주는 것이 목적

<form action="/posts/{{post.id}}/update/"> # 내가 입력한 값 받을 곳
# 아무거나 숫자 들어오는게 아니기 때문에 post.id 사용
    <input type="text" value="{{post.title}}" name="title">
    # 이전에 쓴 값을 확인할 수 있도록 value 값 사용
    <input type="text" value="{{post.content}}" name="content">
    <input type="submit">
   </form>