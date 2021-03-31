# 校验权限中间件，用于业务服务后端，非本项目使用

import requests as webRequest
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from rest_framework import status
import json, re

from user_backend_demo.settings import USER_SERVER  # 用户服务url


class LoginMiddleware(MiddlewareMixin):
    @staticmethod
    def _resourceAuthen(request, userInfo):  # 资源鉴权
        '''
        资源权限鉴权
        :param request:  请求体
        :param userInfo:  用户基本及权限信息
        :return:
        '''
        # 权限字典
        resourceAuthenDic = {  # pathStart: resourceAlias
            '/audit': 'audit', '/industry': 'industry', '/company': 'company', '/target/': 'target', '/report': 'report',
            '/socialReport/list': 'report', '/yearReport/list': 'report', '/yearReport/data': 'yearReportData',
            '/socialReport/data': 'socialReportData', '/targetData': 'targetData', '/publicSentiment': 'publicSentiment',
            '/csrScore': 'csrScore'
        }
        for pathStart, resourceAlias in resourceAuthenDic.items():
            if request.path.startswith(pathStart):
                for resource in userInfo.get('resourcePermission', {}):
                    if resource.get('alias', '') == resourceAlias:
                        return resourceAlias
        # 没有资源权限，报错
        raise Exception('用户({})没有访问{}的权限'.format(userInfo.get('username', ''), request.path))

    @staticmethod
    def _actionAuthen(request, resourceAlias, userInfo):  # 操作鉴权
        '''
        操作鉴权
        :param request: 请求体
        :param resourceAlias: 操作资源别称
        :param userInfo: 用户基本及权限信息
        :return:
        '''
        actionPressionList = []  # 操作权限列表
        for row in userInfo.get('actionPermission'):
            if row.get('resourceAlias', '') == resourceAlias:
                actionPressionList.append(row.get('actionAlias'))

        actionList = ['download', 'upload', 'export', 'audit']  # 能通过url判断的行为类型
        # 操作行为确定
        action = ''  # 默认为查询权限
        for act in actionList:
            if act in request.path:
                action = act
                break
        if action == '' and request.method in ('POST', 'PUT'):  # 编辑行为校验
            action = 'edit'
        elif action == '' and request.method == 'DELETE':  # 删除行为校验
            action = 'delete'
        # 行为权限校验
        if action and action not in actionPressionList:  # 操作但没有权限
            raise Exception('用户({})没有{}的{}权限'.format(userInfo.get('username', ''), resourceAlias, action))

    def process_request(self, request):
        try:
            requestPath = re.sub('^/api', '', request.path)  # 去除代理路径
            if not re.search('^/data/', requestPath) and 'common' not in requestPath:  # 文件白名单不校验
                webSession = webRequest.session()
                webSession.user = request.user
                result = webSession.get(USER_SERVER + '/user/login', headers=request.headers)
                if result.status_code == 200:
                    userInfo = json.loads(result.text).get('data', {})
                    resourceAlias = self._resourceAuthen(request, userInfo)
                    self._actionAuthen(request, resourceAlias, userInfo)
                else:
                    print(result.text)
                    raise Exception(json.loads(result.text).get('msg', '校验失败'))
        except Exception as e:
            return JsonResponse(
                {
                    'data': [],
                    'total': 0,
                    'msg': '用户验证失败：' + str(e),
                    'code': 401
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
