__author__ = 'carrie'
#coding=utf-8
import re
import chardet
from urllib import urlopen,urlretrieve


#获取"小故事背诵"网页链接
# page_list = []
# page_list.append('http://www.kekenet.com/Article/yule/fangtanlu/')
# for i in range(16,17):
#     http = 'http://www.kekenet.com/Article/yule/fangtanlu/List_' + str(i) + '.shtml'
#     print http
#     page_list.append(http)
# print len(page_list)
# #
# #
# # 获取 每个故事 链接
story_list = []
title_list = []
# for page in page_list:
text = urlopen('http://www.kekenet.com/Article/yule/fangtanlu/List_4.shtml').read()
text = str(text).replace('\r\n', '')
b = re.compile(r'http://www.kekenet.com/Article/2.*?shtml')
a = re.compile(r'http://www.kekenet.com/Article/2.*?</a>')
list = re.findall(b, text)
list1 = re.findall(a,text)
# print list
for story in list:
    story_list.append(story)
    # print story
for title in list1:
    title = title.replace('&#8226;','•')
    title = re.findall(r'>(.*?)<', title)
    title_list.append(title[0])
    print 2,title[0]
# print len(story_list)

# 获取 每篇文章的标题,内容,音频,图片
# text = urlopen('http://www.kekenet.com/Article/201109/153564.shtml').read()
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
# picture_list = []
# j = 0
# for i in story_list:
#     text = urlopen(i).read()
#     text = str(text).replace('\r\n','')
# # print text
#     pic_download = re.search(r'http://pic.kekenet.*?jpg', text)
#     if pic_download != None:
#         pic_download = pic_download.group()
#         if len(pic_download) > 100:
#             a = re.findall(r'http://pic.kekenet.*?jpeg', pic_download)
#             if a == []:
#                 b = re.findall(r'http://pic.kekenet.*?JPG', pic_download)
#                 if b == []:
#                     pic_download =re.findall(r'http://pic.kekenet.*?png',pic_download)[0]
#                 else:
#                     pic_download = b[0]
#             else:
#                 pic_download = a[0]
#     else:
#         pic_download = ''
#     print pic_download
#     if pic_download != '':
#         if re.findall('png',pic_download) == []:
#             a = r'/home/carrie/downloads/story/picture/' + str(j) + r'.jpg'
#             urlretrieve(pic_download,a)
#         else:
#             a = r'/home/carrie/downloads/story/picture/' + str(j) + r'.png'
#             urlretrieve(pic_download,a)
#     j = j + 1
#     picture_list.append(pic_download)

# pic_download = re.search(r'http://pic.kekenet.*?jpg','http://pic.kekenet///.*?jpg').group()
# print type(pic_download)
# a = re.search(r'http://pic.kekenet.*?jpg',
#               r'http://pic.kekenet.com/2013/0726/79521374828259.JPG" /></p><p> </p></div>\t        \t '
#              )
# print a
