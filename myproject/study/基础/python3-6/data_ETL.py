import re



str ='219.155.6.220 - - [22/Aug/2017:10:45:39 +0800] "GET /api/user/bindstatus/ HTTP/1.1" 499 0 "http://wxapp.jtgzfw.com:8080/" "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"'

def etl(line):
    m = re.search(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])', line).group()
    m1 = re.search(r'Aug', line)
    m2 = re.search(r'/phpmyadmin', line)
    m3 = re.search(r'http://wxapp.jtgzfw.com', line)
    '''
    m:ip
    m1:time
    m2:/phpmyadmin
    m3:http://wxapp.jtgzfw.com
    '''
    if m1 is None:
        m1 = 0
    else:
        m1 = '201708'
    if m2 is None:
        m2 = 'N'
    else:
        m2 = '/phpmyadmin'
    if m3 is None:
        m3 = 'N'
    else:
        m3 = 'http://wxapp.jtgzfw.com'
    strList =[m, m1, m2, m3]
    s1 = m+','+m1+','+m2+','+m3
    print(s1)
    mystr =','.join(strList)
    return mystr
    # print(type(m))
    # print(type(m1))
    # print(type(m2))
    # print(type(m3))
    # print(m,m1,m2,m3)

print(etl(str))


