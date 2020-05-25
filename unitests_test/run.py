from db import Db
from config import *
from excel import Excel
from HTMLTestRunner import HTMLTestRunner
import unittest

db=Db(ip,user,password,db,port)
res=db.query('select * from t_user where id=251;')
print(res)

excel=Excel(name,sheet)
on=excel.on()
print(on)

suite=unittest.TestSuite()
mk=unittest.defaultTestLoader.discover('.',pattern='test*.py')
suite.addTests(mk)
with open('./测试报告.html','wb') as f:
    HTMLTestRunner(stream=f,verbosity=2,title='测试报告',description='执行人：苏晓晨').run(suite)