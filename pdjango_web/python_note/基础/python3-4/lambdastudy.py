from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

'''
使用匿名函数作为修饰器来验证用户的权限
'''
print('开始')
@user_passes_test(lambda u: u.is_allowed_to_vote)
def vote(request):
    '''投票逻辑处理'''
    print('验证通过正在投票')