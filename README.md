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