from django.db import models

# Create your models here.
class serverlist(models.Model):
    '''
        服务器信息记录列表
    '''
    ip= models.CharField(max_length=20,verbose_name="IP地址")
    Cmac = models.CharField(max_length=20, verbose_name="MAC地址")
    Cname = models.CharField(max_length=20, verbose_name="主机名")
    user = models.CharField(max_length=20, verbose_name="用户")
    position = models.CharField(max_length=30, verbose_name="位置")
    server= models.CharField(max_length=20, verbose_name="设备类型")
    OS = models.CharField(max_length=20, verbose_name="操作系统")
    remark = models.TextField(max_length=50, blank=True,verbose_name="备注")

    class Meta:
        verbose_name_plural = u'服务器记录列表'

class userhostlist(models.Model):
    '''
        员工主机信息记录列表
    '''
    ip= models.CharField(max_length=20,verbose_name="IP地址")
    mac = models.CharField(max_length=20, verbose_name="MAC地址")
    hostname= models.CharField(max_length=20, verbose_name="主机名")
    username = models.CharField(max_length=20, verbose_name="用户名")

    class Meta:
         verbose_name_plural="员工电脑信息记录列表"