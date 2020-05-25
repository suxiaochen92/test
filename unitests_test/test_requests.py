import requests
import unittest
import time
from excel import Excel
from config import *

excel=Excel(name,sheet)
on=excel.on()

class Test_Cases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requests=requests.Session()
        res=cls.requests.post(host+on[1][2],headers=eval(on[1][4]),json=eval(on[1][5]))
        cls.token=res.json()['data']['token']
    @classmethod
    def tearDownClass(cls):
        pass
    def test_01(self):
        res=requests.get(host+on[0][2]+"?"+on[0][5],headers=eval(on[0][4]))
        self.assertEqual(res.json()['status'],int(on[0][6]))
        self.assertEqual(200,res.status_code)
    def test_02(self):
        res=requests.post(host+on[1][2],headers=eval(on[1][4]),json=eval(on[1][5]))
        self.assertEqual(res.json()['status'],int(on[1][6]))
        self.assertEqual(res.status_code,200)
        global token
        token=res.json()['data']['token']
        global cookies
        cookies=res.cookies
    def test_03(self):
        headers=eval(on[2][4])
        headers.update(token=self.token)
        # res=self.requests.post(host+on[2][2],headers=headers,json=eval(on[2][5]))
        # headers.update(token=token)
        res=requests.post(host+on[2][2],headers=headers,json=eval(on[2][5]),cookies=cookies)
        self.assertEqual(res.json()['status'],int(on[2][6]))
        self.assertEqual(res.status_code,200)
# if __name__=='__main__':
#     unittest.main()