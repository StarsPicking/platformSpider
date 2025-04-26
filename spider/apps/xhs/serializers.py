from rest_framework import serializers
from .models import XhsTask
import datetime
class XhsTaskSerializer(serializers.ModelSerializer):
    # creator_id = serializers.CharField(required=False)
    # note_ids = serializers.CharField(required=False)
    passed_since_time = serializers.SerializerMethodField()
    class Meta:
        model = XhsTask   # 序列化器和哪个表建立关系
        fields = "__all__"  #序列化全部字段
    def get_passed_since_time(self, obj):
        now = datetime.datetime.now()
        return "距上次更新{days}天".format(days=(now - obj.updatetime).days)

    def validate(self, attrs):
        if not attrs.get("creator_id") and not attrs.get("note_id"):
            raise serializers.ValidationError("At least one of creator or note_id must be provided.")
        return super().validate(attrs)
    
    # def create(self, validated_data):
    #     # 从原始数据中获取 extra_field，而不是 validated_data
    #     extra_field_value = self.initial_data.get('extra_field')
    #     # 根据 extra_field_value 做一些逻辑处理
    #     if extra_field_value:
    #         # 例如你可以在这里执行一些操作，比如处理或记录这个字段的值
    #         print(f"Processing extra_field: {extra_field_value}")
    #     # 创建模型实例
    #     instance = MyModel.objects.create(**validated_data)


        return instance
    def create(self, validated_data):
        isinstance = XhsTask.objects.create(**validated_data)
        return isinstance