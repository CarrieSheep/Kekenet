__author__ = 'carrie'
#coding=utf-8
import re
import chardet
from urllib import urlopen,urlretrieve


#获取"小故事背诵"网页链接
page_list = []
page_list.append('http://www.kekenet.com/menu/13407/')
for i in range(1,37):
    http = 'http://www.kekenet.com/menu/13407/List_%s' % i + '.shtml'
    # print http
    page_list.append(http)
#
#
# # 获取 每个故事 链接
story_list = []
for page in page_list:
    text = urlopen(page).read()
    c = chardet.detect(text)
    code = c['encoding']
    text = str(text).decode(code, 'ignore').encode('utf-8').replace('\r\n', '')#把文本转换成字符串,并将换行符删去
    # print text
    # a = re.compile(u'<ul id="menu-list">(.*?)<div class="page th">')
    # text = a.search(text)
    # text = text.group()
    # print type(text)
    # print text
    b = re.compile(r'http://www.kekenet.com/menu/2.*?shtml')
    list = re.findall(b, text)
    # print list
    for story in list:
        story_list.append(story)
        text = urlopen(story).read()
        text = str(text).replace('\r\n', '')
        pic_download = re.findall(r'http://pic.kekenet.*?jpg',text)
        print pic_download
# print len(story_list)


# c = urlretrieve('http://pic.kekenet.com/2014/0919/66171411117722.jpg','/home/carrie/66171411117722.jpg')
# print c


# 获取 每篇文章的标题,内容,音频,图片
# text = urlopen('http://www.kekenet.com/menu/201409/329668.shtml').read()
# c = chardet.detect(text)
# code = c['encoding']
# print code
# 以上三行解码错误且
# text = str(text).replace('\r\n', '')
# print text

# #爬取文章  内容和标题
# a = re.compile(r'<div class="qh_.*?</div>')
# article = re.findall(a, text)
# essay = ''
# title = ''
# count = 0
# for item in article:
#     item = re.sub(r'<.*?>', '', item).replace('&#39;', "'")
#     # print item
#     if count < 2:
#         title = title + item + '  '
#         count += 1
#     essay = essay + '\r\n' + item
# print title
# print essay

# 爬取文章  音频
# for i in story_list:
#     mp3_dowmload = i.replace('menu','mp3')
#     # print mp3_dowmload
#     text = urlopen(mp3_dowmload).read()
#     a = re.findall(r'http://xia.*?mp3', text)
#     print a

# 爬取文章  图片

# for i in story_list:
#     pic_download = re.findall(r'http://pic.kekenet.*?jpg',text)
#     print pic_download




