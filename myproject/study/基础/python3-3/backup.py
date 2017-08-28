#文件备份
import os, time

'''
将需要备份的文件和目录指定到一个列表中
'''
sourcefile =['/Users/xiaohaili/ljh_Home/projects/testbackupfile']

'''
指定备份文件的位置
'''
target_dir ='/Users/xiaohaili/ljh_Home/projects/backup'

'''
将备份的文件打包压缩成zip文件
压缩文件的文件名由当前日期和时间构成
'''
targetfile_name = target_dir + os.sep + time.strftime('%Y%m%d%H%M%s')+ '.zip'

#如果目标目录不存在则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(targetfile_name,' '.join(sourcefile))

print(zip_command)

if os.system(zip_command) == 0:
    print('successful back to %s', targetfile_name)
else:
    print('backup FAILED')