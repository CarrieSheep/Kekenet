__author__ = 'carrie'
from urllib import urlopen,urlretrieve
a = r'agdg' + str(1)
print a

a = r'/home/carrie/downloads/story/picture/' + str(1) + r'.png'
urlretrieve('http://pic.kekenet.com//2014/0617/51821402998609.png',a)

c = urlretrieve('http://pic.kekenet.com/2013/0830/83321377852882.JPG', '/home/carrie/66171411122.jpg')
# print c
c = urlretrieve('http://pic.kekenet.com//2014/0520/45641400576355.png','/home/carrie/66171411112.png')
c = urlretrieve('http://pic.kekenet.com//2014/0627/99731403860110.jpeg','/home/carrie/661714111177.jpg')
