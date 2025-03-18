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


migration
