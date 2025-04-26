from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import XhsTask
from .serializers import XhsTaskSerializer
from utils.custom_renderer import enveloper
@extend_schema(tags=["任务管理"])
class TaskView(APIView):

    @extend_schema(
        operation_id="task-get",  # 设置右上角的名称，需要唯一性
        summary="任务列表",  # 接口上的备注 
        responses= enveloper(XhsTaskSerializer, True),
        )
    def get(self, request):
        """
        获取所有任务
        """
        task_list = XhsTask.objects.all()
        ser = XhsTaskSerializer(task_list, many=True)
        return Response(ser.data)
    
    @extend_schema(
        operation_id="task-post",  # 设置右上角的名称，需要唯一性
        summary="创建任务",  # 接口上的备注 
        request= XhsTaskSerializer,
        responses= enveloper(XhsTaskSerializer, True),
        ) 
    def post(self, request):
        """
        添加任务
        参数creator_id和note_id至少有一个
        """
        data = request.data
        serializer1  = XhsTaskSerializer(data=data)
        if not serializer1.is_valid():
            return Response(serializer1.errors)
        serializer1.save()
        return Response(serializer1.data)