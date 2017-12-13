"""mytest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.admin import site

from asset.views import *
from .views import *
from wol.views import  *

# from mytestapp.views import home

urlpatterns = [
    url(r'^admins/', site.urls),

	url(r'^admin/$', admin, name='index'),
	url(r'^account/', include('account.urls')),

	# 远程开机模块
	url(r'^$', Index),
	url(r'^wol/$', PowerOn, name='PowerOn'),
	#asset主机记录信息
	url(r'^asset/$', server_list, name='server_list'),
	url(r'^asset/(?P<id>\d+)/$',ServerManage, name="server_edit"),
	url(r'^asset/delete/$', ServerManage,name='server_delete'),
	url(r'^hostlist/',host_list, name='host_list'),


	
]
