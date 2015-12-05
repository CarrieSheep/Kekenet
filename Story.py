__author__ = 'carrie'

#coding = utf-8
import re
import chardet
from urllib import urlopen

class CrawlerStoryUrl :

    def getPageUrl(self):
        Http = []
        for i in range(1,36):
            http ='http://en.dict.cn/news/topic/strange/pn%s' % i
            print http
            Http.append(http)
        return Http

 # 获取海词英语网奇闻轶事1-46页的网址所对应的源代码
    def getText(self):
        total_url = self.getHttp()
        Text = []
        for total_url in total_url:
            # print total_url
            text = urlopen(total_url).read()
            c = chardet.detect(text)
            code = c['encoding']
            # print code   # 查询网页的编码方式，code 为utf-8
            text = str(text).decode(code, 'ignore').encode('utf-8')
            # print text
            Text.append(text)
        return Text

    # 获取1-46页每篇奇闻轶事的网址
    def getTotalUrl(self):
        text = self.getText()
        Url = []
        for text in text:
            pattern1_url = re.compile('<h2.*?class="ainfo">')
            url_list = re.findall(pattern1_url, text)
            pattern2_url = re.compile('/news/view/\d*')
            url_list = str(url_list)
            url_list = re.findall(pattern2_url, url_list)
            for url_list in url_list:
                url_list = 'http://en.dict.cn'+url_list
                # print url_list
                Url.append(url_list)
        # print Url
        return Url

