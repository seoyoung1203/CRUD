앱 생성

```shell
djang
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
python manage.py makemigrartions
```

```shell
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

## Read

- 전체 데이터 가져오기
def index(request):
    posts = Post.objects.all()


- 하나씩 뽑아오기
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

## create

1. 사용자에게 빈 종이 제공
2. 빈 종이에 내용을 입력
3. 입력된 내용을 create로 전송
4. 전송된 데이터 중에서 필요한 정보를 뽑아내고
5. DB에 저장

## Update


## Delete

1. 