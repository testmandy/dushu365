# -*- coding: utf-8 -*-
# @Time    : 2023/4/19 10:49
# @Author  : Mandy
# -*- coding: utf-8 -*-
import random

import xlsxwriter as xw

import conftest
from common.excel import Excel

read_filename = conftest.data_dir + '/book_data.xls'
write_filename = conftest.data_dir + '/results_data.xls'


# def get_sheet_count():
#     """根据问题名称获取问卷列表"""
#     ex = Excel(read_filename)
#     count = ex.get_nsheets()
#     return count


def xw_to_results(data_list, sheet_name):  # xlsxwriter库储存数据到excel
    """将结果写入统计表"""
    workbook = xw.Workbook(write_filename)  # 创建工作簿
    index = 0
    worksheet1 = workbook.add_worksheet(str(index + 1) + sheet_name)  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['id', '书本id', '书名', '主讲', '标签', '总结', '推荐语', '封面', '宣传页', '音频url', '视频url']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data_list)):
        # insertData = [data_list[j]["id"], data_list[j]["info"]]
        str_list = data_list[j].splitlines()
        print(str_list)
        bookId = str_list[0]
        bookName = str_list[1]
        speakerName = str_list[2]
        customTag = str_list[3]
        summary = str_list[4]
        intro = str_list[5]
        mediaImageUrl = str_list[6]
        cover = str_list[7]
        audioUrl = str_list[8]
        videoUrl = str_list[9]
        insertData = [i-1, bookId, bookName, speakerName, customTag, summary, intro, mediaImageUrl, cover, audioUrl, videoUrl]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        i += 1
    index += 1

    workbook.close()


def write_results(data_list, sheet_name):
    """将结果写入结果表"""
    xw_to_results(data_list, sheet_name)
