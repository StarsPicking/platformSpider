from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NoteDetail, XhsCreator, XhsTask

admin.site.register(NoteDetail)
admin.site.register(XhsCreator)
admin.site.register(XhsTask)

admin.site.site_header='自媒体发布管理后台'
admin.site.site_title='自媒体发布管理后台'