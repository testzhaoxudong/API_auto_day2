import os
import unittest

# 定义一个函数来组织测试用例
def add_testcase_to_suite_by_discover():
    # 获取测试用例所在的目录
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testcase_path = os.path.join(base_path, "testcase")
    # 调用unittest框架下的defaultTestLoader下的discover方法来加载测试用例
    suite = unittest.defaultTestLoader.discover(testcase_path, pattern="test*.py")
    # 返回测试套件
    return suite
