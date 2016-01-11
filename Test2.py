#coding=utf-8
__author__ = 'carrie'
import re
from urllib import urlretrieve,urlopen
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
# g = 'http://www.kekenet.com/Sound/2015/11/15_3459987kpP.lrc'
# urlretrieve(g,'/home/carrie/downloads/story/picture/g.lrc')


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

# text = urlopen('http://www.kekenet.com/video/movie/').read()
# text = str(text).replace('\r\n','')
# print len(re.findall(r'<li><a href="/video/.*?</li>',text))
# print len(re.findall(r'<li><a href="/menu/.*?</li>',text))

# text = urlopen('http://www.kekenet.com/menu/13407/').read()
# text = str(text).replace('\r\n','')
# a = re.findall(r'<span id="total">.*?</span>',text)
# print a[0]
# print type(re.sub(r'<.*?>','',a[0]))

# text = urlopen('http://www.kekenet.com/video/201203/174590.shtml').read()
# text = str(text).replace('\r\n','')
# a = re.findall(r'<time.*?time>',text)
# a = re.findall(r':(.*?)</time',a[0])
# print a

# text = urlopen('http://www.kekenet.com/video/201203/174590.shtml').read()
# text = str(text)
# text = re.sub(r'\n','',text)
# print text
# a = re.compile('<div class="qh_.*?</div>')
# article = re.findall(a, text)
# # print article
# content = ''
# if article != []:
#     for item in article:
#         print item
#         item = re.sub(r'<.*?>', '', item).replace('&#39;', "'").replace('&quot;', '"')
#         content = content + item + '\r\n'
# else:
#     content = ''

# text = urlopen('http://www.kekenet.com/video/movie/piano/').read()
# text = str(text)
# text = re.sub(r'\n', '', text)
# a = re.findall(r'<a href="http://www.kekenet.com/video/2.*?_blank">',text)
# for i in a:
#     c = re.findall(r'《.*?target',i)
#     c = re.sub(r'" target', '', c[0])
#     print c

# text = urlopen('http://www.kekenet.com/video/201110/158986.shtml').read()
# text = str(text)
# text = re.sub(r'\n','',text)
# a = re.findall(r'<span id="article_eng">.*?<script>',text)[0]
# a = re.sub(r'<BR></FONT>','@@@@',a)
# a = re.sub(r'<BR><FONT.*?>','@@@@',a)
# a = re.sub(r'</FONT> <BR>','@@@@',a)
# a = re.sub(r'<BR></STRONG></FONT>','@@@@',a)
# a = re.sub(r'<.*?>','',a)
# a = re.split('@@@@',a)
# print a
# for i in a:
#     print i

a = ''
print len(a)