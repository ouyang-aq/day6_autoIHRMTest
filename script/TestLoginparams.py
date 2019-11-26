
import logging
import unittest

from parameterized import parameterized

from aip.loginAPi import LoginApi
from utils import assert_utils, read_login_data


class TestLogin(unittest.TestCase):
    def setUp(self):
        pass

    @classmethod
    def setUpClass(cls):
        cls.login_api=LoginApi()

    def tearDown(self):
        pass

    @parameterized.expand(read_login_data)
    def test01_login_success(self,mobile, password, http_code, success, code, message):
        response=self.login_api.login(mobile, password)
        jsonData=response.json()#type:dict
        logging.info("测试登陆成功返回的数据为：{}".format(jsonData))
        assert_utils(self,response, http_code, success, code, message)

