#coding=utf-8
__author__ = 'carrie'
import re
from urllib import urlretrieve
# from urllib import urlopen,urlretrieve
# a = r'agdg' + str(1)
# print a
#
# a = r'/home/carrie/downloads/story/picture/' + str(1) + r'.png'
# urlretrieve('http://pic.kekenet.com//2014/0617/51821402998609.png',a)
#
# c = urlretrieve('http://pic.kekenet.com/2013/0830/83321377852882.JPG', '/home/carrie/66171411122.jpg')
# # print c
# c = urlretrieve('http://pic.kekenet.com//2014/0520/45641400576355.png','/home/carrie/66171411112.png')
# c = urlretrieve('http://pic.kekenet.com//2014/0627/99731403860110.jpeg','/home/carrie/661714111177.jpg')

# page_list = []
# page_list.append('http://www.kekenet.com/menu/13407/')
# for i in range(34,34):
#     http = 'http://www.kekenet.com/menu/13407/List_%s' % i + '.shtml'
#     # print http
#     page_list.append(http)
# print 1, page_list
# 检测正则中(.*?)与.*?的不同
# a = '>agsrh<'
# b = re.compile(r'>(.*?)<')
# title = re.search(b, a)
# print 1,title.group()
# title = re.search(r'>.*?<', a)
# print 2,title.group()

# a = '<a http://www.kekenet.com/menu/201409/329668.shtml \a>'
# print type(a),a
# b = re.findall(r'<a.*?\a>',a)
# c = re.findall(r'<a(.*?)\a>',a)
# print b
# print c

#检测lrc文件
# a = 'http://www.kekenet.com/Sound/Article/fangtanlu/20111117.mp3.lrc'
g = 'http://www.kekenet.com/Sound/2015/11/15_3459987kpP.lrc'
urlretrieve(g,'/home/carrie/downloads/story/picture/g.lrc')


# 检测for循环中列表删除元素后长度是否变化
# list = ['asd','ad',123,'bgs']
# print 1, len(list)
# list.pop(2)
# print 2, len(list),list
# for i in range (0,len(list)):
#     print 3, list[i]

#检测re.spilt的效果
# str  = 'asd' + '\r\n' +'dfdg' + '\r\n'
# print str
# title = re.split('\r\n',str)
# print title

#字典的用法
# dict = {'a':['a','b'],'b':[1, 2, 3]}
# print dict['a']







