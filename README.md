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