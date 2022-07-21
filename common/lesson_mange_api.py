import requests
from config import *
from common.login_api import login


class Lesson_manage_api():
    # 获取cookie
    user_cookie = login()[0]
    # 定义一个函数，实现新增课程的功能
    def add_lesson_api(self, lesson_data):
        # 获取请求的URL
        url = f"{HOST}{ADD_LESSON_API_PATH}"
        # 获取请求的参数
        payload = {"action": "add_course",
                   "data": lesson_data}
        # 模拟发送请求
        res = requests.post(url, data=payload, cookies=self.user_cookie)
        # 返回响应的主体内容
        return res.json()

    # 定义一个函数，实现删除课程的功能
    def delete_lesson_api(self, lessonId):
        # 获取请求的URL
        url = f"{HOST}{DELETE_LESSON_API_PATH}"
        # 获取请求的参数
        payload = {"action":"delete_course",
                   "id": lessonId}
        # 模拟发送请求
        res = requests.delete(url, data=payload, cookies=self.user_cookie)
        # 返回响应的结果
        return res.json()

    # 定义一个函数，实现列出课程的功能
    def list_lesson_api(self, pageNum, pageSize):
        # 获取请求的URL
        url = f"{HOST}{LIST_LESSON_API_PATH}"
        # 获取请求URL的参数
        params = {"action":"list_course",
                  "pagenum": pageNum,
                  "pagesize": pageSize}
        # 模拟发送请求
        res = requests.get(url, params=params, cookies=self.user_cookie)
        # 返回实际的响应的结果
        return res.json()


    # 定义一个函数用来实现删除系统中所有的课程数据
    def delete_all_lesson_data(self):
        # 获取系统中总共的课程的数量
        total_lesson = self.list_lesson_api(1, 20)["total"]
        # 获取系统中的课程的页数
        if total_lesson % 20 > 0:   # 取模运算，获取余数
            pageNum = total_lesson // 20 + 1   # 表示地板除法，向下取整
        else:
            pageNum = total_lesson // 20
        # 定义一个空列表，用来存放系统中所有的课程的信息
        lesson_list = []
        # 对页数进行循环，然后调用 列出课程接口 来获取系统中的所有的课程信息
        for num in range(1, pageNum + 1):
            # 调用列出接口查询所有的课程信息
            lesson_list.append(self.list_lesson_api(num, 20)["retlist"])
        # 调用删除课程接口删除系统中所有的课程
        for lesson in lesson_list:    # lesson是某一页的所有的课程信息
            for lessonInfo in lesson:     # lessonInfo是某一门的课程信息
                # 调用删除课程接口
                self.delete_lesson_api(lessonInfo["id"])

# 实例化一个对象
LessonManagement = Lesson_manage_api()

if __name__ == '__main__':
    LessonManagement.delete_all_lesson_data()
    print(LessonManagement.list_lesson_api(1,20))


