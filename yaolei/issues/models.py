from django.db import models
from material.models import Meterials

# Create your models here.

class Issues(models.Model):
    issueType = models.CharField(max_length=10,verbose_name='问题类型')
    issue = models.CharField(max_length=100,verbose_name='问题')
    reason = models.CharField(max_length=100,verbose_name='原因')
    solution = models.TextField(verbose_name='解决方案')
    # meterial = models.ForeignKey(Meterials, related_name='issue', verbose_name='物料', blank=True,on_delete=models.CASCADE)

class MeterialIssues(models.Model):
    pubtime = models.DateTimeField(verbose_name='时间',auto_now_add=True)
    issue = models.ForeignKey(Issues,related_name='issuesmeter',verbose_name='问题以及问题类型',on_delete=models.CASCADE,default='')
    meterial = models.ForeignKey(Meterials,related_name='meterialsmete',verbose_name='物料',blank=True,on_delete=models.CASCADE)
    histcode = models.CharField(max_length=10,verbose_name='层柱析编号')
    # issuetype = models.CharField(max_length=100,verbose_name='问题类型')
    # issuesolution = models.TextField(verbose_name='解决方案')



