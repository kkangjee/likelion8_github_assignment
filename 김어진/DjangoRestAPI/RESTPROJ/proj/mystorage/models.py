from django.db import models
from django.conf import settings
class Essay(models.Model):
    #models에 있는 foreign key를 기반으로 만들어지며
    #settings에 있는 author user model기반으로 정의
    author=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    body=models.TextField()

class Album(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length=100)

class Files(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.FileField(blank=False, null=False, upload_to="files")
    desc = models.CharField(max_length=100)

