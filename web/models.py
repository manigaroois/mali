import datetime

from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

class Server(models.Model):
    title = models.CharField(_("عنوان"), max_length=255)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class AbrServer(models.Model):
    title = models.CharField(_("عنوان"), max_length=255)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Expense(models.Model):
    title = models.CharField(_("عنوان"), max_length=255)
    product = models.TextField(_("محصول"))
    user_name = models.CharField(_("نام کاربری خریدار"), max_length=255)
    amount = models.BigIntegerField(_("قیمت"))
    time = models.DateTimeField(_("زمان"))
    server = models.ForeignKey(AbrServer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Income(models.Model):
    title = models.CharField(_("عنوان"), max_length=255)
    product = models.TextField(_("محصول"))
    user_name = models.CharField(_("نام کاربری خریدار"), max_length=255)
    amount = models.BigIntegerField(_("قیمت"))
    time = models.DateTimeField(_("زمان"))
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
