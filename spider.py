#__author__ = 'hmj'
# -*-coding:utf8-*-
import urllib2
import csv
from sgmllib import SGMLParser


def spider_run(dest_url):
    response = urllib2.urlopen(dest_url)
    html = response.read()
    return html


class html_parser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        #活动题目
        self.is_h3 = ""
        self.name = []
        #详细内容
        self.is_div=""
        self.divdesc=[]
        #活动时间
        self.is_time=""
        self.etime=[]
        #活动地点
        self.is_span=""
        self.loc=[]

    def start_h3(self, attrs):
        self.is_h3 = 1

    def end_h3(self):
        self.is_h3 = ""

    def start_div(self, attrs):
        self.is_div = 1

    def end_div(self):
        self.is_div = ""

    def start_time(self, attrs):
        self.is_time = 1

    def end_time(self):
        self.is_time = ""

    def start_span(self, attrs):
        cl_loc = [v for k, v in attrs if k=='class']
        if cl_loc:
            self.is_span = 1

    def end_span(self):
        self.is_span = ""

    def handle_data(self, text):
        if self.is_h3 == 1:
            self.name.append(text)
        if self.is_div==1:
            self.divdesc.append(text)
        if self.is_time==1:
            self.etime.append(text)
        if self.is_span==1:
            self.loc.append(text)
# def csv_write(data):
# 	csvfile=file('d:\\niuniuevents.csv','wb')
# 	writer.writerow(['时间', '名称', '内容','链接'])
#     data = [('2014-6-30', '和孩子做游戏', 'blabla','1234567'),('2014-6-30', '玩乐','abaabaaba', '789456')]


def main():
    dest_url='http://www.childlib.org/ts/events/'
    html=spider_run(dest_url)
    my_parser=html_parser()
    my_parser.feed(html)
    for x in my_parser.name:
        print x.decode('UTF-8').encode('cp936')
    for x in my_parser.divdesc:
        print x.decode('UTF-8').encode('cp936')
    for x in my_parser.etime:
        print x.decode('UTF-8').encode('cp936')
    for x in my_parser.loc:
        print x.decode('UTF-8').encode('cp936')

if __name__ == '__main__':
    main()
