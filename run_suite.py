import unittest
import os
import time
from script.TestLogin import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
report_name=os.getcwd()+"/report/report-{}.html".format(time.strftime("%Y%m%d%H%M%S"))
with open(report_name,mode='wb')as f:
    runner=HTMLTestRunner(f,verbosity=1,title="IHRM人力资源",description='v.0.0')

    runner.run(suite)