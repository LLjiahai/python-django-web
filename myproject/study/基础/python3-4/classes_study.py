class BookEntity(object):
    version = 0.1

    def __init__(self,name, phone, author):
        '''
        定义该类的一个构造器
        '''
        self.name = name
        self.phone = phone
        self.author = author

    def update_phone(self, phone):
        '''
        修改属性author_phone
        '''
        self.author_phone = phone

'''创建实例对象'''
book1 = BookEntity('Python', 163, 'Jnet')
'''遍历实例'''
print(book1.__dict__)
print(book1.phone)

'''
修改属性的值
'''
book1.phone = 198
print(book1.phone)


'''
类的继承
'''
class PythonBookEntity(BookEntity):
    def __init__(self, name, id, phone, author, publishdate):
        BookEntity.__init__(self,name,phone,author)
        self.pbook_id = id
        self.pbtime = publishdate

pbe = PythonBookEntity('python+web', 1, 158, 'sos', '20170823')
print(pbe.__dict__)
print(pbe.version)
pbe.phone=185
print(pbe.phone)


'''
内部类/嵌套类
嵌套类也是一个真正的Python类，但他只有在OuterClass实例的内部才可见，即这个内部类归属于外部类
'''
class OuterClass(object):
    class InnerClass:
        pass
