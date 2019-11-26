import json
import logging
from unittest import TestCase
from requests import Response

import app


def assert_utils(self,response,htttpCode,success,code,message):
    """
    @type self:TestCase
    @type response:Response
    """
    jsonData=response.json()#type:dict
    self.assertEqual(htttpCode,response.status_code)
    self.assertEqual(success,jsonData.get("success"))
    self.assertEqual(code,jsonData.get("code"))
    self.assertIn(message,jsonData.get("message"))

def read_login_data():
    login_data=app.BASEDIR+"/data/login.json"
    with open(login_data,mode='r',encoding='utf-8')as f:
        jsonData=json.load(f)
        logging.info("read_login_data:{}".format(jsonData))
        result_list=[]
        for data in jsonData:
            mobile=data.get("mobile")
            password=data.get("password")
            http_code=data.get("http_code")
            success=data.get("success")
            code=data.get("code")
            message=data.get("message")
            result_list.append((mobile,password,http_code,success,code,message))
        logging.info("result_list: {}".format(result_list))
    return result_list