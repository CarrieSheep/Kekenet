__author__ = 'carrie'
#coding = utf-8
import re
import chardet
from urllib import urlopen,urlretrieve

class PatStory():

    # 获取可可英语网小故事背诵达人1-37页的网页链接
    def getPageUrl(self):
        page_list = []
        page_list.append('http://www.kekenet.com/menu/13407/')
        for i in range(1,37):
            http = 'http://www.kekenet.com/menu/13407/List_%s' % i + '.shtml'
        # print http
            page_list.append(http)
        return page_list

    # 获取每个故事的网页链接
    def getStoryUrl(self):
        story_list = []
        page_list = self.getPageUrl()
        for page in page_list:
            text = urlopen(page).read()
            b = re.compile(r'http://www.kekenet.com/menu/2.*?shtml')
            list = re.findall(b, text)
            # print list
            for story in list:
                story_list.append(story)
        return story_list

    # 获取每个故事页面的源代码
    def getStorySC(self):
        sc_list = []
        story_list = self.getStoryUrl()
        for story in story_list:
            text = urlopen(story).read()
            text = str(text).replace('\r\n', '')
            sc_list.append(text)
        return sc_list

    #获取每个故事的内容和标题
    def getContent(self):
        content_list = []
        title_list = []
        sc_list = self.getStorySC()
        for content in sc_list:
            a = re.compile(r'<div class="qh_.*?</div>')
            article = re.findall(a, content)
            essay = ''
            title = ''
            count = 0
            for item in article:
                item = re.sub(r'<.*?>', '', item).replace('&#39;', "'")
                # print item
                if count < 2:
                    title = title + item + '  '
                    count += 1
                essay = essay + '\r\n' + item
            content_list.append(essay)
        return content_list

    #获取每个故事的MP3
    def getMP3(self):
        mp3_list = []
        mp3Url_list = []
        story_list = self.getStoryUrl()
        for story in story_list:
            mp3_dowmload = story.replace('menu','mp3')
            # print mp3_dowmload
            text = urlopen(mp3_dowmload).read()
            a = re.search(r'http://xia.*?mp3', text)
            # print a
            if a == None:
                mp3Url_list.append('')
            else:
                mp3Url_list.append(a.group())
        i = 0
        for mp3 in mp3Url_list:
            if mp3 != []:
                a = r'/home/carrie/downloads/story/mp3/' + i + r'.mp3'
                urlretrieve(mp3,a)
            i += 1

    #获取每个故事的图片
