from django.shortcuts import render
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from utils.utils import errorResponse, normalResopnse
from user_backend_demo.settings import SESSION_COOKIE_AGE
from user.models import AuthUserGroups, AuthGroup
from user.permissions import ACTION_PERMISSION_DIC, RESOURCE_PERMISSION_DIC
# Create your views here.


class CsrfExemptSessionAuthentication(SessionAuthentication):  # CSRF Failed: CSRF token missing or incorrect.解决方案
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


# 用户登录
class UserLoginView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    # 登录
    def post(self, request):
        try:
            userName = request.data.get('userName', "")
            pwd = request.data.get('pwd', '')
            if not userName or not pwd:
                raise Exception('参数缺失')
        except Exception as e:
            return errorResponse(request, str(e), status.HTTP_400_BAD_REQUEST)
        try:
            if request.user.is_authenticated:  # 已登录则session延时并
                request.session.set_expiry(SESSION_COOKIE_AGE)  # 延迟session时效
                return normalResopnse(request, getLoginResponseData(request.user), total=1)
            else:  # 未登录进行登录操作
                user = authenticate(username=userName, password=pwd)
                if user is not None:
                    login(request, user)
                    return normalResopnse(request, getLoginResponseData(user), total=1)
                else:
                    return errorResponse(request, '用户不存在或密码错误', status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return errorResponse(request, str(e), status.HTTP_409_CONFLICT)

    # 是否已登录验证
    def get(self, request):
        user = request.user
        if user is not None:
            if user.is_authenticated:  # 校验是否已登录
                request.session.set_expiry(SESSION_COOKIE_AGE)  # 延迟session时效
                return normalResopnse(request, getLoginResponseData(user), total=1)
            else:
                return errorResponse(request, '用户未登录或登录超时', status.HTTP_401_UNAUTHORIZED)
        else:
            return errorResponse(request, '用户不存在', status.HTTP_401_UNAUTHORIZED)


class UserView(APIView):
    # 创建用户
    def post(self, request):
        try:
            userName = request.data.get('userName', '')
            email = request.data.get('email', '')
            pwd = request.data.get('pwd', '')
            if not userName or not email or not pwd:
                raise Exception('参数缺失')
        except Exception as e:
            return errorResponse(request, str(e), status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create_user(userName, email, pwd)
            user.save()
            return normalResopnse(request, ['success'], total=1, status=status.HTTP_201_CREATED)
        except Exception as e:
            return errorResponse(request, str(e), status.HTTP_409_CONFLICT)

class UserPasswordView(APIView):
    # 修改密码
    def put(self, request):
        try:
            if 'oldPwd' not in request.data or 'newPwd' not in request.data:
                raise Exception("缺少参数")
            oldPwd = request.data['oldPwd']
            newPwd = request.data['newPwd']
            if oldPwd == newPwd:
                raise Exception("新密码与就密码一致无法修改")
        except Exception as e:
            return errorResponse(request, str(e), status.HTTP_400_BAD_REQUEST)
        try:
            if request.user.is_authenticated:
                result = request.user.check_password(oldPwd)
                if not result:
                    raise Exception("旧密码有误")
                request.user.set_password(newPwd)
                request.user.save()
                return normalResopnse(request, ["success"], 1, status.HTTP_202_ACCEPTED)
            else:
                raise Exception("用户未登录")
        except Exception as e:
            return errorResponse(request, str(e), status.HTTP_409_CONFLICT)


# 账号登出
class UserLogoutView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return normalResopnse(request, ['logout'], 1)
        else:
            return errorResponse(request, '用户未登录，登出无效', status.HTTP_409_CONFLICT)


# 共用方法
def getLoginResponseData(user):
    userGroupRes = AuthUserGroups.objects.filter(user_id=user.id).extra(
            select={'new_group_id': "position(group_id in '2,1,3')"}).order_by('new_group_id').first()  # 按权限级别高->低排列
    groupId = userGroupRes.group_id if userGroupRes else 3  # 没有找到的定义为访客
    groupRes = AuthGroup.objects.filter(id=groupId).first()
    return {
        'username': user.username,
        'groupId': groupId,
        'group': groupRes.name if groupRes else '',
        'resourcePermission': RESOURCE_PERMISSION_DIC[groupId],
        'actionPermission': ACTION_PERMISSION_DIC[groupId]
    }
