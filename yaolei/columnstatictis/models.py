from django.db import models
from material.models import Meterials

# Create your models here.

class Columnstatictis(models.Model):
    resin = models.ForeignKey(Meterials,related_name='materisesin',on_delete=models.CASCADE,verbose_name='填料')
    packingitem = models.CharField(max_length=20,verbose_name='装柱项目',blank=True)
    histcode = models.CharField(max_length=20,verbose_name='层析柱编号',blank=True)
    resincode = models.CharField(max_length=20,verbose_name='填料编号',blank=True)
    lowestspeed = models.CharField(max_length=20,verbose_name='最低装柱流速',blank=True)
    hightspeed = models.CharField(max_length=20,verbose_name='最高装柱流速',blank=True)
    pressure = models.CharField(max_length=20,verbose_name='装柱压力',blank=True)
    yieldspeed = models.CharField(max_length=20,verbose_name='生产流速',blank=True)
    columnheight = models.CharField(max_length=20,verbose_name='柱高',blank=True)
    columndimeter = models.CharField(max_length=20,verbose_name='层析柱直径',blank=True)
    symmetry = models.CharField(max_length=20,verbose_name='对称性',blank=True)
    hetp = models.CharField(max_length=20,verbose_name='HETP',blank=True)
    comment = models.CharField(max_length=30,verbose_name='备注',blank=True)

