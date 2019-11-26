import logging
import unittest
from aip.loginAPi import LoginApi
from utils import assert_utils


class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.login_api=LoginApi()

    def tearDown(self):
        pass

    def test01_login_success(self):
        response=self.login_api.login("13800000002","123456")
        jsonData=response.json()#type:dict
        logging.info("测试登陆成功返回的数据为：{}".format(jsonData))
        assert_utils(self,response,200,True,10000,"操作成功")
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(True,jsonData.get("success"))
        # self.assertEqual(10000,jsonData.get("code"))
        # self.assertIn("操作成功",jsonData.get("message"))

    def test02_mobile_is_not_exist(self):
        response=self.login_api.login("13800000002","error")
        jsonData=response.json()#type:dict
        logging.info("测试密码错误返回的数据为：{}".format(jsonData))
        assert_utils(self,response,200,False,20001,"用户名或密码错误")
        # self.assertEqual(200,response.status_code)
        # self.assertEqual(False,jsonData.get("success"))
        # self.assertEqual(20001,jsonData.get("code"))
        # self.assertIn("用户名或密码错误",jsonData.get("message"))

    def test03_mobile(self):
        response = self.login_api.login("13640219972", "123456")
        jsonData = response.json()  # type:dict
        logging.info("测试账号不存在返回的数据为：{}".format(jsonData))
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")


    def test04_mobile_is_not(self):
        response = self.login_api.login("", "error")
        jsonData = response.json()  # type:dict
        logging.info("测试账号为空返回的数据为：{}".format(jsonData))
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

    def test05_password_is_not(self):
        response = self.login_api.login("13800000002", "")
        jsonData = response.json()  # type:dict
        logging.info("测试密码为空返回的数据为：{}".format(jsonData))
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")

