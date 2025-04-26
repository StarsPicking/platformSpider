from django.db import models

# Create your models here.

from enum import Enum

class NoteTypeChoice(Enum):
    VIDEO = 1
    IMAGE = 2

class NoteDetail(models.Model):
    note_id = models.CharField(max_length=35, verbose_name="多媒体id")
    type = models.IntegerField(choices=[(tag.name, tag.value) for tag in NoteTypeChoice])
    title = models.CharField(max_length=100, verbose_name = "标题")
    desc = models.CharField(max_length=200, verbose_name= "描述")
    video_url= models.URLField(verbose_name="视频地址")
    time = models.DateTimeField(verbose_name="发布时间")
    last_update_time = models.DateTimeField(verbose_name="最后更新时间")
    user_id = models.CharField(max_length=25, verbose_name="用户id")
    nickname = models.CharField(max_length=20, verbose_name="昵称")
    avatar = models.URLField(verbose_name="头像地址")
    liked_count = models.IntegerField(verbose_name="点赞数")
    comment_count = models.IntegerField(verbose_name="评论数")
    share_count = models.IntegerField(verbose_name="分享数")
    ip_location= models.IntegerField(verbose_name="地域")
    image_list = models.CharField(max_length=500 ,verbose_name="图集地址")
    tag_list = models.CharField(max_length=100,verbose_name="话题")
    last_modify_ts = models.IntegerField()
    note_url = models.URLField(verbose_name="多媒体地址")
    source_keyword = models.CharField(max_length=200, verbose_name="关键词")
    xsec_token = models.CharField(max_length=45)
    def __str__(self):
        return self.desc
    class Meta:
        managed = True
        verbose_name = "笔记"
        verbose_name_plural = verbose_name

class SourceChoice(Enum):
    FROMID = 1  # 通过笔记列表爬取
    FROMCREATOR = 2 # 通过创作者id爬取




class XhsCreator(models.Model):
    creator_id = models.CharField(max_length=35, verbose_name="创作者id")
    nickname = models.CharField(max_length=20, verbose_name="昵称")
    avatar = models.URLField(max_length=200, verbose_name="头像")
    inserttime = models.DateTimeField(auto_now_add=True, verbose_name="插入时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    def __str__(self):
        return self.creator_id + self.nickname
    
    class Meta:
        managed = True
        verbose_name = "创作者"
        verbose_name_plural=verbose_name


class XhsTask(models.Model):
    creator_id = models.CharField(max_length=35, null=True,verbose_name="创作者id")
    note_ids = models.CharField(max_length=500, null=True, verbose_name="笔记数组")
    inserttime = models.DateTimeField(auto_now_add=True, verbose_name="插入时间")
    updatetime = models.DateTimeField(auto_now=True, verbose_name="更新时间")


    class Meta:
        managed = True
        verbose_name = "任务"
        verbose_name_plural=verbose_name