import re
import time
from datetime import datetime
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
'''
将txt文件load到mysql数据库中
load data local infile "D:/data.txt" into table salary fields terminated by ',';
'''

str ='219.155.6.220 - - [22/Aug/2017:10:45:39 +0800] "GET /api/user/bindstatus/ HTTP/1.1" 499 0 "http://wxapp.jtgzfw.com:8080/" "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"'
m = re.search(r'(?<![.\d])(?:\d{1,3}.){3}\d{1,3}(?![.\d])', str).group()
m1 = datetime.strptime(re.findall(r'\[(.*)\]', str)[0][:-6],"%d/%b/%Y:%H:%M:%S").strftime('%Y-%m-%d')
# m1 = re.search(r'Aug', str)
m2 = re.search(r'/phpmyadmin', str)
m3 = re.search(r'http://wxapp.jtgzfw.com', str)
# m1 = '04/12/2017:23:24:24'
# 20170812 1

# time.strptime(m1,'%Y%m%d');/
 #04/Aug/2017:23:24:24 +0800


if m2 is None:
    m2 = 'N'
else:
    m2 = 'Y'
if m3 is None:
    m3 = 'N'
else:
    m3 = 'Y'

print(m, m1,m2, m3)

