from django.db import models

# Create your models here.


from enum import Enum
class NoteTypeChoice(Enum):
    1 = "video"
    2 = "image"

class NoteDetail(models.Model):
    note_id = models.CharField(max_length="35", verbose_name="多媒体id")
    type = models.IntegerField(choices=[(tag.name, tag.value) for tag in NoteTypeChoice])
    title = models.CharField(max_length="100", verbose_name = "标题")
    desc = models.CharField(max_length="200", verbose_name= "描述")
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
    image_list = models.CharField(verbose_name="图集地址")
    tag_list = models.CharField(verbose_name="话题")
    last_modify_ts = models.IntegerField()
    note_url = models.URLField(verbose_name="多媒体地址")
    source_keyword = models.CharField(verbose_name="关键词")
    xsec_token = models.CharField()

    def __str__(self):
        return self.desc

