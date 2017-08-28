name = 'lijiahai'
something = 'learning python'
#字符串的格式化方法
print('{0} is {1}'.format(name, something))
print('{} is {}'.format(name, something))

#使用^定义代表字符串，并用*来前后修饰字符串
print('{0:*^9}'.format('hello'))

#end=''指定结尾字符不换行
print('a', end='')
print('b')

#运算符
print('la'*3, 3**2)