from rest_framework.renderers import JSONRenderer

from rest_framework.renderers import JSONRenderer
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
# 导入控制返回的JSON格式的类


MSG = "success"
CODE = 200
class CustomRenderer(JSONRenderer):
    # 设立标准返回信息以及返回码

    # 重构render方法
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # 判断实例的类型，返回的数据可能是列表也可能是字典
        if renderer_context:
            if isinstance(data, dict):
                self.MSG = data.pop('msg', MSG)
                self.CODE = data.pop('code', CODE)
                if 'status' in data.keys():
                    del data['status']
        data = {
            'msg': MSG,
            'code': CODE,
            'data': data
        } 
        return super().render(data, accepted_media_type, renderer_context)



def enveloper(serializer_class, many):
    component_name = 'response{}{}'.format(
        serializer_class.__name__.replace("Serializer", ""),
        "List" if many else "",
    )
    
    @extend_schema_serializer(many=False, component_name=component_name)
    class EnvelopeSerializer(serializers.Serializer):
        msg = serializers.CharField(default=MSG)# some arbitrary envelope field
        code = serializers.CharField(default=CODE)
        data = serializer_class(many=many)  # the enveloping part

    return EnvelopeSerializer

