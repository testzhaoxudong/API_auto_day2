import os
from BeautifulReport import BeautifulReport
from API_auto_day2.testsuite.testsuite import add_testcase_to_suite_by_discover as suite
from API_auto_day2.common.time_stamp import time_stamp

# 获取测试报告存在的目录
base_path = os.path.dirname(os.path.abspath(__file__))
report_path = os.path.join(base_path,"report")
# 判断一下测试报告所在的目录是否存在，如果不存在，则创建。
if not os.path.exists(report_path):
    os.mkdir(report_path)
# 获取测试套件
test_suite = suite()
# 实例化BeautifulReport对象
BeautifulReport(test_suite).report(filename=f"report_{time_stamp()}", description="接口自动化测试报告", log_path=report_path)