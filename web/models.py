from django.db import models
from django.utils.translation import ugettext_lazy as _

class Expense(models.Model):
    titel = models.CharField()
