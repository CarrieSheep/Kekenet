#coding = utf-8
__author__ = 'carrie'

import re
import chardet
from urllib import urlopen,urlretrieve

class PatInterview():

    def getPageUrl(self):
        page_list = []
        # page_list.append('http://www.kekenet.com/Article/yule/fangtanlu/')
        for i in range(4, 5):
            http = 'http://www.kekenet.com/Article/yule/fangtanlu/List_' + str(i) + '.shtml'
            # print http
            page_list.append(http)
        print 1, page_list
        return page_list

    def getUrlAndTitle(self):
        story_list = []
        title_list = []
        page_list = self.getPageUrl()
        for page in page_list:
            text = urlopen(page).read()
            text = str(text).replace('\r\n', '')
            a = re.compile(r'http://www.kekenet.com/Article/2.*?</a>')
            b = re.compile(r'http://www.kekenet.com/Article/2.*?shtml')
            list_url = re.findall(b, text)
            list_title = re.findall(a,text)
            # print len(list_title)
            for title in list_title:
                title = title.replace('&#8226;','')
                title = re.findall(r'>(.*?)<', title)
                # print title
                if title != []:
                    title_list.append(title[0])
                    print title[0]
                else:
                    print ''
            for story in list_url:
                story_list.append(story)
                # print story
        print 2, title_list
        print 3, story_list
        dict = {'title':title_list,'url':story_list}
        return dict

    def getInterviewSC(self):
        story_list = self.getUrlAndTitle()
        sc_list = []
        for story in story_list:
            text = urlopen(story).read()
            text = str(text).replace('\r\n', '')
            sc_list.append(text)
        print 4, sc_list
        return sc_list

    def getContent(self):
        sc_list = self.getInterviewSC()
        content_list = []
        for sc in sc_list:
            a = re.compile('<div class="qh_.*?</div>')
            article = re.findall(a, sc)
            content = ''
            if article != []:
                for item in article:
                    item = re.sub(r'<.*?>', '', item).replace('&#39;', "'")
                    content = content + item + '\r\n'
                content_list.append(content)
            else:
                content_list.append('')
            print 5, content
        return content_list

if __name__ == '__main__':
    a = PatInterview()
    a.getContent()