from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

# Create your models here.
class Kouho(models.Model):
    name = models.CharField(max_length=20,verbose_name="氏名")
    age = models.PositiveSmallIntegerField(verbose_name="年齢")
    kao=models.ImageField(upload_to="uploads/",verbose_name="顔写真")
    tou = models.CharField(max_length=20,verbose_name="所属政党")
    career = models.TextField(verbose_name="経歴")
    manifesto_class = models.CharField(max_length=20,verbose_name="選挙公約分類")
    flag = models.CharField(max_length=20,default='unchecked',verbose_name="フラグ")
    manifesto = models.TextField(verbose_name="選挙公約")
    instagram=models.URLField(verbose_name="instergram")
    twitter=models.URLField(verbose_name="twitter")
    facebook=models.URLField(verbose_name="facebook")


    def __str__(self):
        return self.name

class Seitou(models.Model):
    seitou_name=models.CharField(max_length=20,verbose_name="政党名")
    body=models.TextField(verbose_name="政党説明")


class Chat(models.Model):
    chat_name=models.CharField(max_length=20,verbose_name="名前")
    chat_content=models.TextField(verbose_name="テキスト")
    posted_at=models.DateTimeField(default=timezone.now)

class User(models.Model):
    username=models.CharField(max_length=20,verbose_name="ニックネーム")
    mail=models.EmailField(max_length=120,verbose_name="メールアドレス")