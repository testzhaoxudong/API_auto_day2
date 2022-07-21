import xlrd
import os
import json

# 定义一个函数，用来读取excel表格中的测试用例数据
def get_lesson_data(sheetname):
    # 定义一个空列表
    lessonDataList = []
    # 需要获取excel表格的路径
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testcase_path = os.path.join(base_path, "excel_testcase_data", "测试用例.xlsx")
    # 打开excel文件读取数据
    WorkBook = xlrd.open_workbook(testcase_path)
    # 通过sheet页的名称来读取某个sheet页的数据
    WorkSheet = WorkBook.sheet_by_name(sheetname)
    # 获取excel表格中的有效数据的 行数
    maxrows = WorkSheet.nrows
    # 循环所有的 行数，然后获取 单元格的数据
    for row in range(1, maxrows):
        # 获取到的是请求参数 列的数据
        reqInfo = WorkSheet.cell(row, 8).value   # 行 和 列 都是从 0 开始计算
        # 获取到的是返回结果列的数据，并且把获取到返回结果列的数据转换为字典
        resInfo = json.loads(WorkSheet.cell(row, 10).value)
        # 获取excel表格中的测试编号
        test_num = WorkSheet.cell(row, 0).value
        # 获取excel表格中的用例标题
        testcse_title = WorkSheet.cell(row, 2).value
        # 把获取到的请求参数  和 返回结果 列的数据 append到空列表中
        lessonDataList.append([reqInfo, resInfo, test_num, testcse_title])
    # 返回获取到的测试用例
    return lessonDataList

if __name__ == '__main__':
    print(get_lesson_data("2-增加课程")[1])



