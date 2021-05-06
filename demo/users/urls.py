# 从 urls 模块中导入 re_path
from django.conf.urls import re_path
# 从当前目录导入我们的视图模块 views
from . import views

app_name = "haha"

# urlpatterns 是被 django 自动识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要使用 url 函数来构造
    # url (路径, 视图)
    re_path(r'^index/$', views.index),
    re_path(r'^haha/$', views.haha),
    re_path(r'^hello/$', views.show_index),
    re_path(r'^req/$', views.req, name="heihei"),

]
