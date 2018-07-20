"""restaurant的url设置"""

from django.conf.urls import url
from . import views

app_name = 'restaurant'

urlpatterns = [
    # 餐馆主页
    url(r'^$', views.index, name='index'),

    # 菜单主页
    url(r'^menu/$', views.menu, name='menu'),

    # 单个菜品的详细信息
    url(r'^menu/(?P<dish_id>\d+)/$', views.dish_detail, name='dish'),

    # 单个菜品的点菜界面
    url(r'menu/(?P<dish_id>\d+)/order/$', views.order_dish, name='dish_ordering'),

    # 显示账单
    url(r'bill/$', views.get_bill, name='bill'),
]