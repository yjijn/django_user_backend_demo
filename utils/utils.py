import logging
from rest_framework.response import Response
from rest_framework import status


# 正常输入
def normalResopnse(request, data, total, status=status.HTTP_200_OK):
    result = outPut(data, total=total)
    writeLog('info', request, result)
    return Response(result, status=status)

# 异常数据
def errorResponse(request, error, status):
    result = outPut([], msg=str(error))
    writeLog('error', request, error)
    return Response(result, status=status)


#  接口输出数据函数
def outPut(data, msg='', total=0):
    return {
        'data': data,
        'total': total,
        'msg': msg
    }

# 日志方法
def writeLog(level, request, response):
    '''

    :param level: info,error
    :param requst: requst object
    :param response: response or error
    :return:
    '''
    logger = logging.getLogger('log')
    if level == 'info':
        logger.info('IP:{},{} {} request {}'.format(request.META['REMOTE_ADDR'], request.path, request.method,
                                                   request.GET))
        logger.info('{} {} response:{}'.format(request.path, request.method, response))
    elif level == 'error':
        logger.error('IP:{},{} {} request {}'.format(request.META['REMOTE_ADDR'], request.path, request.method,
                                                     request.GET))
        logger.error('{} {} ERROR:{}'.format(request.path, request.method, response))
