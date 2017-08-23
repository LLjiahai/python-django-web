import re
'''
python的正则表达式可以通过re模块来访问，这是在查找函数中使用非常频繁的一个组件。re.search返回一个匹配对象
随后可以用这个对象的group或者groups方法获取匹配的模式

python re模块的match（），search（）

re模块的match（）匹配是从字符串的开始位置匹配，只有从0位置匹配成功才有返回，否则返回none
search（）匹配字符串中有无符合模式要求的子串

例如：
re.match('world','hello world'),会返回none
re.search(‘world’，‘hello world’).span()返回（6，10）

group和groups是两个不同的函数。

一般，m.group(N) 返回第N组括号匹配的字符。
而m.group() == m.group(0) == 所有匹配的字符，与括号无关，这个是API规定的。

m.groups() 返回所有括号匹配的字符，以tuple格式。
m.groups() == (m.group(0), m.group(1), ...)
'''

m = re.search(r'foo', 'seafood')
print(m)
print(m.group()) #获取到匹配的字符串

