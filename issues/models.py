from django.db import models

# Create your models here.

class Issues(models.Model):
    issue = models.CharField(max_length=100,verbose_name='问题')
    reason = models.CharField(max_length=100,verbose_name='原因')
    solution = models.TextField(verbose_name='解决方案')
