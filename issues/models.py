from django.db import models

# Create your models here.

class Issues(models.Model):
    issue = models.CharField(max_length=100,verbose_name='问题')
    reason = models.CharField(max_length=100,verbose_name='原因')
    solution = models.TextField(verbose_name='解决方案')

# class MeterialIssues(models.Model):
#     pubtime = models.DateTimeField(verbose_name='时间',auto_now_add=True)
#     meterial = models.ManyToManyField(Issues,related_name='issue',verbose_name='物料')
#     histcode = models.CharField(max_length=10,verbose_name='层柱析编号')
#     issuetype = models.CharField(max_length=100,verbose_name='问题类型')
#     issuesolution = models.TextField(verbose_name='解决方案')



