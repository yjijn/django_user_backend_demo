from django.conf.urls import url, include
from rest_framework import routers

from user.views import *


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^login', UserLoginView.as_view(), name='login'),
    url(r'^logout', UserLogoutView.as_view(), name='logout'),
    url(r'pwd', UserPasswordView.as_view(), name='changePwd'),
    url(r'', UserView.as_view(), name='user')
]