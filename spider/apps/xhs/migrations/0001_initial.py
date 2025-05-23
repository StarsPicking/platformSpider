# Generated by Django 5.2 on 2025-04-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoteDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_id', models.CharField(max_length=35, verbose_name='多媒体id')),
                ('type', models.IntegerField(choices=[('VIDEO', 1), ('IMAGE', 2)])),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('video_url', models.URLField(verbose_name='视频地址')),
                ('time', models.DateTimeField(verbose_name='发布时间')),
                ('last_update_time', models.DateTimeField(verbose_name='最后更新时间')),
                ('user_id', models.CharField(max_length=25, verbose_name='用户id')),
                ('nickname', models.CharField(max_length=20, verbose_name='昵称')),
                ('avatar', models.URLField(verbose_name='头像地址')),
                ('liked_count', models.IntegerField(verbose_name='点赞数')),
                ('comment_count', models.IntegerField(verbose_name='评论数')),
                ('share_count', models.IntegerField(verbose_name='分享数')),
                ('ip_location', models.IntegerField(verbose_name='地域')),
                ('image_list', models.CharField(max_length=500, verbose_name='图集地址')),
                ('tag_list', models.CharField(max_length=100, verbose_name='话题')),
                ('last_modify_ts', models.IntegerField()),
                ('note_url', models.URLField(verbose_name='多媒体地址')),
                ('source_keyword', models.CharField(max_length=200, verbose_name='关键词')),
                ('xsec_token', models.CharField(max_length=45)),
            ],
        ),
    ]
