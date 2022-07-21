import unittest
from parameterized import parameterized
from API_auto_day2.common.lesson_mange_api import LessonManagement
from API_auto_day2.common.get_lesson_data import get_lesson_data

# 使用unittest框架编写测试用例
class Test_lesson(unittest.TestCase):
    # 初始化，删除系统中增加的课程信息
    @classmethod
    def setUpClass(cls):   # 表示在类执行之前执行
        LessonManagement.delete_all_lesson_data()

    # 善后操作
    @classmethod
    def tearDownClass(cls):    # 表示 在类 执行之后 执行
        LessonManagement.delete_all_lesson_data()

    # 定义一个方法，增加课程信息
    @parameterized.expand(get_lesson_data("2-增加课程"))
    def test_add_lesson(self, data, expected, tesecase_num, testcase_title):
        self._testMethodDoc = testcase_title   # 加上这一行代码以后，把测试用例的标题编写在了 测试报告中的 “用例描述”列
        self._testMethodName = tesecase_num   # 加上这一行代码以后，把测试用例的编号编写在了 测试报告中的 “测试方法”列
        # 实际响应的结果
        actual_result = LessonManagement.add_lesson_api(data)
        # 获取实际的响应结果中的 retcode 的值
        actual_retcode = actual_result["retcode"]
        # 获取预期的响应结果中的 retcode 的值
        expected_retcode = expected["retcode"]
        # 判断reason 是否在预期结果中，如果是 断言预期结果中的retcode 及 reason 和 实际结果中的 retcode 及 reason是否一致
        if "reason" in expected:
            # 获取预期结果中的 reason的值
            expected_reason = expected["reason"]
            # 获取实际的响应结果中的 reason的值
            actual_reason = actual_result["reason"]
            # 断言
            self.assertEqual(expected_retcode, actual_retcode)
            self.assertEqual(expected_reason, actual_reason)
        else:
            self.assertEqual(actual_retcode, expected_retcode, msg=f"实际结果中的retcode的值为：{actual_retcode}") # 加上msg以后会把信息打印到测试报告中