# utils/exceptions.py
from rest_framework.views import exception_handler
from rest_framework.response import Response
from django.conf import DEBUG  
from rest_framework import status
from utils.logger import logger

# 自定义异常处理
# 创建文件exception.py 在这里我们需要处理发生错误时响应的内容 因为DRF的报错种类比较多，所以当我取detail的内容或错误的最后一条信息为msg 这里将错误信息处理成返回
def common_exception_handler(exc, context):
    # 将错误写入日志
    logger.error('view是：%s ，错误是%s' % (context['view'].__class__.__name__, str(exc)))
    response: Response = exception_handler(exc, context)
    if response is None:
        # 处理drf未处理的异常

        if DEBUG:
            raise err
        res = {"msg": "服务器错误:{err}", "code": 500}
        return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
    else:
        # drf已经处理的异常
        msg = response.reason_phrase
        if "detail" in response.data:
            msg = response.data["detail"]
        else:
            for k, v in response.data.items():
                msg = v 
                if isinstance(v, list):
                    msg = v[0]
        res = {}
        res.update(response.data)
        res["msg"] = msg
        res["code"] = response.status_code
        return Response(res, status=response.status_code, exception=True)
