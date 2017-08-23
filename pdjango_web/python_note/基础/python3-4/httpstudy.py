import http.client  #python2中是httplib python3中是http.client


def check_web_server(host, port, path):
    h = http.client.HTTPConnection(host,port)
    h.request('GET', path)
    resp = h.getresponse()
    print('HTTPResponse:')
    print('     status = ', resp.status)
    print('     reason = ', resp.reason)
    print('HTTP Header:')
    for hdr in resp.getheaders():
        print('     %s: %s' %hdr)

check_web_server('www.python.org',80,'/')
'''
当该函数的参数在一个三元组里面的时候
'''
host_info = {'host': 'www.python.org', 'port': 80, 'path': '/'}
check_web_server(host_info[0],host_info[1],host_info[2])

'''
当参数为很多的时候，我们可以构造一个字典，这样可以达到扩展的效果
'''
host_info_dict = {'host': 'www.python.org', 'port': 80, 'path': '/'}
'''
这样告诉函数打开字典的时候，每个键是参数的名字，同时对应的值是函数调用的参数。
'''
check_web_server(**host_info_dict)