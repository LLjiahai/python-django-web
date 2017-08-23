'''
定义修饰器函数
'''
def log(func):
    def wrappedFunc(*args, **kw):
        print("********%s() called" % func.__name__)
        return func(*args, **kw)
    return wrappedFunc

@log
def foo():
    print('inside foo()')

foo()

'''
说明：我们需要增强foo（）函数的功能
观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
我们要借助Python的@语法，把decorator置于函数的定义处。
调用
'''
'''
# 延伸
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
'''