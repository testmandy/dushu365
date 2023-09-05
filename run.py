# -*- coding: utf-8 -*-
# @Time    : 2023/2/21 14:21
# @Author  : Mandy
import sys

from common.book_write import write_results
from common.course_write import write_course
from common.get_url import TestUrl
from common.method import Request

req = Request()
URL = TestUrl()
headers = {'Content-Type': 'application/json; charset=utf-8'}
token = "20230905B7luzZCz7b0WdfooiGn"


def get_token():
    """common_get_member_info"""
    data = {"code": "001e42ll2am32b4docol2FOgrd2e42lR", "appId": "wxeaf7bf1de621b0c2",
            "platformType": "miniWx_saveInfo"}
    r = req.post(url=URL.get_url('common_get_member_info'), data=data)
    t = r['data']['token']
    return t


def get_ff_book_list(pageSize):
    data = {
        "appId": "2002",
        "pageNo": 1,
        "pageSize": pageSize,
        "tagId": 10048,
        "key": "allBook",
        "newFlag": "true",
        "token": token
    }
    res = req.post(url=URL.get_url('ff_book_list'), data=data, headers=headers)
    result_list = []
    for i in res['data']:
        bookId = i['bookId']
        bookName = "《%s》" % i['bookName']
        speakerName = i['speakerName']
        try:
            customTag = i['customTag']
            new_customTag = customTag.splitlines()
            customTag = "".join(new_customTag)
        except:
            customTag = "暂无标签"

        try:
            summary = i['summary']
            new_summary = summary.splitlines()
            summary = "".join(new_summary)
        except:
            summary = "暂无总结"

        try:
            intro = i['intro']
            new_intro = intro.splitlines()
            intro = "".join(new_intro)
            # for line in intro:
            #     print(line)
        except:
            intro = "暂无推荐语"

        book_info = get_book_info(bookId)
        result = '%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (bookId, bookName, speakerName, customTag, summary, intro, book_info)
        result_list.append(result)
    write_results(result_list, "非凡精读馆")


def get_ll_book_list(pageTotal):
    result_list = []
    for page in range(1, pageTotal):
        data = {
            "pageNo": page,
            "appId": "2002",
            "token": token
        }
        res = req.post(url=URL.get_url('ll_book_list'), data=data, headers=headers)
        for i in res['data']:
            bookId = i['bookId']
            bookName = "《%s》" % i['title']
            speakerName = "李蕾"
            try:
                customTag = i['customTag']
                new_customTag = customTag.splitlines()
                customTag = "".join(new_customTag)
            except:
                customTag = "暂无标签"

            try:
                summary = i['subtitle']
                new_summary = summary.splitlines()
                summary = "".join(new_summary)
            except:
                summary = "暂无总结"

            try:
                intro = i['intro']
                new_intro = intro.splitlines()
                intro = "".join(new_intro)
            except:
                intro = "暂无推荐语"

            book_info = get_book_info(bookId)
            result = '%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (
                bookId, bookName, speakerName, customTag, summary, intro, book_info)
            result_list.append(result)
    write_results(result_list, "李蕾读经典")


def get_fd_book_list(pageSize):
    data = {
        "order": 1,
        "categoryId": 0,
        "pageSize": pageSize,
        "token": token,
        "appId": "2002",
        "page": 1,
        "bookReadStatus": -1
    }
    res = req.post(url=URL.get_url('fd_book_list1'), data=data, headers=headers)
    print(res)
    result_list = []
    for i in res['books']:
        bookId = i['bookId']
        bookName = "《%s》" % i['title']
        speakerName = '樊登'
        try:
            customTag = i['customTag']
            new_customTag = customTag.splitlines()
            customTag = "".join(new_customTag)
        except:
            customTag = "暂无标签"

        try:
            summary = i['summary']
            new_summary = summary.splitlines()
            summary = "".join(new_summary)
        except:
            summary = "暂无总结"

        try:
            intro = i['intro']
            new_intro = intro.splitlines()
            intro = "".join(new_intro)
            # for line in intro:
            #     print(line)
        except:
            intro = "暂无推荐语"

        book_info = get_book_info(bookId)
        result = '%s\n%s\n%s\n%s\n%s\n%s\n%s\n' % (bookId, bookName, speakerName, customTag, summary, intro, book_info)
        result_list.append(result)
    write_results(result_list, "樊登讲书")


def get_book_info(bookId):
    data = {
        "bookId": bookId,
        "token": token,
        "appId": "2002"
    }
    res = req.post(url=URL.get_url('fd_book_detail'), data=data, headers=headers)
    audioUrl = res['data']['audioInfo']['audioUrl']
    mediaImageUrl = res['data']['audioInfo']['mediaImageUrl']

    try:
        try:
            try:
                cover = res['data']['videoInfo']['cover']
            except:
                cover = res['data']['videoInfo']['mediaImageUrl']
        except:
            cover = res['data']['videoInfo']['videoCoverUrl']
    except:
        cover = "暂无封面"
    # mediaImageUrl2 = res['data']['videoInfo']['mediaImageUrl']
    # videoCoverUrl = res['data']['videoInfo']['videoCoverUrl']
    try:
        videoUrl = res['data']['videoInfo']['videoUrl']
    except:
        videoUrl = "暂无视频"
    info = '书籍封面：%s\n宣传封面：%s\n音频url：%s\n视频url：%s\n' % (mediaImageUrl, cover, audioUrl, videoUrl)
    # print('-------------------书本信息-------------------\n', info)
    return info


def get_course_list(courseId, pageSize):
    data = {
        "courseId": courseId,
        "token": token,
        "page": {
            "pageNo": "1",
            "pageSize": pageSize
        },
        "appId": "2002"
    }
    res = req.post(url=URL.get_url('course_list'), data=data, headers=headers)
    album_list = []
    id_list = []
    i = 0
    for album in res['data']:
        programId = res['data'][i]['id']
        albumId = res['data'][i]['albumId']
        albumName = res['data'][i]['albumName']
        audioUrl = res['data'][i]['audioUrl']
        title = res['data'][i]['title']
        album_list.append(album)
        id_list.append(programId)
        i += 1
        info = '课程ID：%s\n书名：%s\n音频url：%s\n标题：%s\n' % (programId, albumName, audioUrl, title)
        # print('-------------------书本信息-------------------\n', info)
        # print('\n', info)
    # print(id_list)
    return id_list


def get_course_info(courseId):
    program_id_list = get_course_list(courseId, pageSize=300)
    print(program_id_list)
    course_info_list = []
    for programId in program_id_list:
        data = {
            "appId": "2002",
            "programId": programId,
            "albumId": courseId,
            "fragmentType": "3",
            "token": token
        }
        res = req.post(url=URL.get_url('course_info'), data=data, headers=headers)
        albumAuthorName = res['data']['albumAuthorName']
        albumId = res['data']['albumId']
        programId = res['data']['programId']
        categoryName = res['data']['categoryName']
        albumName = res['data']['albumName']

        mediaUrls = res['data']['mediaUrls']
        title = res['data']['title']
        # info = '课程ID：%s\n节目ID：%s\n分类：%s\n课程名：%s\n节目名：%s\n视频url：%s' % \
        #        (albumId, programId, categoryName, albumName, title, mediaUrls)
        info = '\n%s\n%s\n%s\n%s\n%s' % \
               (programId, categoryName, albumName, title, mediaUrls)
        # print('-------------------书本信息-------------------\n', info)
        course_info_list.append(info)
    return course_info_list
    # write_course(result_list, "樊登精品课程")


def get_buy_records(pageNo, sheet_name, filename):
    data = {
        "appId": "2002",
        "pageSize": 1,
        "pageNo": pageNo,
        "token": token,
        "type": 0
    }
    res = req.post(url=URL.get_url('buy_records'), data=data, headers=headers)
    print(res)
    album_list = res['data']['list']
    course_id_list = []
    result_list = []
    i = 0
    for album in album_list:
        course_id = album['id']
        i+=1
        course_id_list.append(course_id)
        author = album['author']
        title = album['title']
        subTitle = album['subTitle']
        info = '%s\n%s\n%s\n%s' % \
               (course_id, author, title, subTitle)
        course_info = get_course_info(course_id)
        course_info2 = [info + str(i) for i in course_info]
        result_list.append(course_info2)
    print(result_list)
    write_course(result_list[0], sheet_name, filename)
    # return result_list
    # albumId = res['data']['albumId']
    # programId = res['data']['programId']
    # categoryName = res['data']['categoryName']
    # albumName = res['data']['albumName']


if __name__ == '__main__':
    # get_ff_book_list(20)
    get_fd_book_list(20)
    # get_ll_book_list(20)
    # get_course_list(400002103)
    # get_course_info(400002103)
    # get_book_info(400069651)
    # get_buy_records(1, "樊登读孟子", '/course_data13.xls')
    # get_buy_records(2, "樊登讲大学", '/course_data1.xls')
    # get_buy_records(3, "李蕾", '/course_data2.xls')
    # get_buy_records(4, "面试", '/course_data3.xls')
    # get_buy_records(5, "罗家德", '/course_data4.xls')
    # get_buy_records(6, "曾仕强-易经", '/course_data5.xls')
    # get_buy_records(7, "韩鹏杰", '/course_data6.xls')
    # get_buy_records(8, "王峰", '/course_data7.xls')
    # get_buy_records(9, "论语", '/course_data8.xls')
    # get_buy_records(10, "新父母", '/course_data9.xls')
    # get_buy_records(11, "李欣", '/course_data10.xls')
    # get_buy_records(12, "姜鹏", '/course_data11.xls')
    # get_buy_records(13, "曾仕强-易经", '/course_data12.xls')

