from django.conf.urls import url
from django_app import views
#
#
app_name = 'django_app'
urlpatterns = {
    url(r'^add/$', views.ADD.add, name='add'),
    # url(r'^add/(\d+)/(\d+)/$', views.Old_add2_Redirect.add_to_add2, name='add'),
    # url(r'^new_add/(\d+)/(\d+)', views.ADD.add2, name='add2'),
    url(r'^add/(\d+)/(\d+)', views.ADD.add2, name='add2'),
    url(r'^$', views.Home.index, name='home'),
    # url(r'^请求路径', views.方法名或者类名, name='别名'),
    # url(r'^api/check_user_type/', views.check_user_type, name='cut'),获取的用方法来处理请求
    # url(r'^api/paycallbackhttp$', views.PayCallback.as_view(), name='pay'),获取的用类来处理请求
}