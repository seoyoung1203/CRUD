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

- modeling ('models.py')

```python
Class Post(models.Model):
    title = modles.CharField(max_length=100)
    content = models.TextField()
```
- migration
```shell
# 번역본 생성
python manage.py makemigrartions
```

```shell
# DB에 반영
python manage.py migrate
```

- create super user
```shell
python manage.py createsuperuser
```

- admin 페이지에 모델 등록('admin.py')
```python
from django.contrib import admin
from.models import Post

admin.site.register(Post)
```

### Read

- 전체 데이터 가져오기
```shell
def index(request):
    posts = Post.objects.all()
```


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

### create

1. 사용자에게 빈 종이 제공
2. 빈 종이에 내용을 입력
3. 입력된 내용을 create로 전송
4. 전송된 데이터 중에서 필요한 정보를 뽑아내고
5. DB에 저장

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

### Delete

1. 

### 코드 참고사항
- f ''>> 문자열 안에 변수를 넣기 위함
- return render(request, 'create.html') >> html 페이지를 보여주는 것이 목적