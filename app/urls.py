from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),  # 首页
    url(r'^market/$', views.market, name='marketbase'), # 闪购超市
    url(r'^market/(?P<childid>\d+)/(?P<sortid>\d+)/$', views.market, name='market'), # 闪购超市

    url(r'^cart/$', views.cart, name='cart'),
    url(r'^mine/$', views.mine, name='mine'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]