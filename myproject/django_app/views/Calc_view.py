from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.core.urlresolvers import reverse


class ADD(View):

    def add(request):
        '''
        1. 采用 /add/?a=4&b=5 这样GET方法进行
        :param request:
        :return:c:将结果返回到发出请求的页面中
        '''
        a = request.GET.get('a', 0)
        b = request.GET.get('b', 0)
        c = str(int(a)+int(b))

        return HttpResponse(c)

    def add2(request,a,b):
       '''
       2. 采用 /add/3/4/ 这样的网址的方式
       :param request:
       :param a:
       :param b:
       :return:
       '''
       c = str(int(a) +int(b))
       return HttpResponse(c)


class Old_add2_Redirect(View):
    '''
    将来自url(r'^add/(\d+)/(\d+)/$', views.Old_add2_Redirect.add_to_add2, name='add'),
    转发到url(r'^new_add/(\d+)/(\d+)',views.ADD.add2, name='add2'),
    进行处理
    这样，假如用户收藏夹中有 /add/4/5/ ，访问时就会自动跳转到新的 /new_add/4/5/ 了
    '''
    def add_to_add2(request, a, b):
        return HttpResponseRedirect(reverse('add2', args=[a, b]))