from django.db import models

# Create your models here.
class playerlist(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='id')
    player=models.CharField(max_length=9999,verbose_name="玩家名")
    mail=models.EmailField(verbose_name="邮箱")
    ifok=models.NullBooleanField(verbose_name="处理结果",default=None,null=True)
    time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name='申请列表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.player

class paperlist(models.Model):
    id=models.AutoField(primary_key=True,verbose_name='id')
    title=models.CharField(verbose_name="标题",max_length=100)
    pags=models.TextField(verbose_name="内容")
    ifok=models.BooleanField(verbose_name="是否显示",default=False,null=False)
    time=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    class Meta:
        verbose_name='公告列表'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title

