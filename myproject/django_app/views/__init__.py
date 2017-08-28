'''
把单文件配置改成包配置
每个view都需要写不然在该app下的urlpatterns的url中找不到匹配
'''
from django_app.views.Calc_view import ADD, Old_add2_Redirect
from django_app.views.Index_view import Home