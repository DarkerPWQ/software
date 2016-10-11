# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import urllib
import urllib2
#import re
import requests
#import glovar
import numpy as np
#from os.path import join
import os
import re
import shutil
from lxml import etree
from Queue import Queue
import mysou_rc
import wave
import json
import webbrowser
import threading
import time
import Image
import ImageFilter
from glob import glob
from os.path import join
from time import ctime,sleep
import mp3play
from pyaudio import PyAudio,paInt16
import urllib,urllib2,pycurl
from Queue import Queue
#import threading

# from PyQt4.QtGui import QMainWindow
# from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_pwq import Ui_MainWindow
from Ui_picdeal import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self,pic_path,parent = None):
        """
        Constructor
        """
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.picflag=0
        self.pic_path=pic_path
        self.format=''
        print self.pic_path
        u=unicode(self.pic_path)
        self.img = Image.open(u)
        self.new_img=self.img
    
    @pyqtSignature("")
    def on_radioButton_clicked(self):
        self.format='.bpm'


    @pyqtSignature("")
    def on_radioButton_2_clicked(self):
        self.format='.gif'


    @pyqtSignature("")
    def on_radioButton_3_clicked(self):
        self.format='.gpeg'

    @pyqtSignature("")
    def on_radioButton_4_clicked(self):
        self.format='.png'

    @pyqtSignature("")
    def on_radioButton_5_clicked(self):
        self.format='.tiff'


    @pyqtSignature("")
    def on_radioButton_6_clicked(self):
        self.format='.wmf'

    @pyqtSignature("")
    def on_pushButton_clicked(self): #黑白处理
        self.picflag=1
        self.new_img = self.img.convert('L')
        self.new_img.show()



    @pyqtSignature("")
    def on_pushButton_2_clicked(self):#模糊滤镜
        self.picflag=2
        self.new_img = self.img.filter(ImageFilter.BLUR)
        self.new_img.show()

    @pyqtSignature("")
    def on_pushButton_3_clicked(self):#浮雕滤镜
        self.picflag=3
        self.new_img =self.img.filter(ImageFilter.EMBOSS)
        self.new_img.show()


    @pyqtSignature("")
    def on_pushButton_4_clicked(self):#左右逆反
        self.picflag=4
        self.new_img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.new_img.show()


    @pyqtSignature("")
    def on_pushButton_6_clicked(self):#平滑处理
        self.picflag=6
        self.new_img = self.img.filter(ImageFilter.SMOOTH)
        self.new_img.show()

    @pyqtSignature("")
    def on_pushButton_7_clicked(self):#轮廓滤镜
        self.picflag=7
        self.new_img = self.img.filter(ImageFilter.CONTOUR)
        self.new_img.show()


    @pyqtSignature("")
    def on_pushButton_8_clicked(self):#边界滤镜
        self.picflag=8
        self.new_img = self.img.filter(ImageFilter.SMOOTH_MORE)
        self.new_img.show()

    @pyqtSignature("")
    def on_pushButton_5_clicked(self):#锐化处理
        self.picflag=5
        self.new_img = self.img.filter(ImageFilter.SHARPEN)
        self.new_img.show()



    @pyqtSignature("")
    def on_pushButton_9_clicked(self):#yulan
        self.new_img.show()
        # if self.picflag==0:
        #     self.new_img=self.img
        #
        # if self.picflag==1:#黑白处理
        #     self.new_img = self.img.convert('L')
        #     self.new_img.show()
        #     print type(self.new_img)
        # elif self.picflag==2:#模糊滤镜
        #     self.new_img = self.img.filter(ImageFilter.BLUR)
        #     self.new_img.show()
        #     print type(self.new_img)
        # elif self.picflag==3:#浮雕滤镜
        #     self.new_img =self.img.filter(ImageFilter.EMBOSS)
        #     self.new_img.show()
        #     print type(self.new_img)
        # elif self.picflag==4:#左右逆反
        #     self.new_img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        #     self.new_img.show()
        #     print type(self.new_img)
        # elif self.picflag==5:#锐化处理
        #     self.new_img = self.img.filter(ImageFilter.SHARPEN)
        #     self.new_img.show()
        #     print type(self.new_img)
        # elif self.picflag==6:#平滑处理
        #     self.new_img = self.img.filter(ImageFilter.SMOOTH)
        #     self.new_img.show()
        #     print type(self.new_img)
        # elif self.picflag==7:#轮廓
        #     self.new_img = self.img.filter(ImageFilter.CONTOUR)
        #     self.new_img.show()
        #     print type(self.new_img)
        # elif self.picflag==8:#细化处理
        #     self.new_img = self.img.filter(ImageFilter.SMOOTH_MORE)
        #     self.new_img.show()
        #     print type(self.new_img)
        # # else:
        # #     my_button = QMessageBox.warning(self,u'警告', u'请选择图片处理方式',u'选择' )
        # #self.picflag=0
    @pyqtSignature("")
    def on_toolButton_clicked(self):
        my_list = QStringList()
        my_list.append('45')
        my_list.append('90')
        my_list.append('180')
        my_list.append('270')
        my_list,ok = QInputDialog.getItem(self,u'下拉框',u'请选择旋转角度',my_list)
        print my_list
        #注意刚出来的类型
        if my_list =='45':
            self.new_img = self.new_img.rotate(45) #旋转45
        elif my_list=='90':
            self.new_img = self.new_img.transpose(Image.ROTATE_90)
        elif my_list=='180':
            self.new_img = self.new_img.transpose(Image.ROTATE_180)
        elif my_lis=='270':
            self.new_img = self.new_img.transpose(Image.ROTATE_270)




    @pyqtSignature("")
    def on_pushButton_10_clicked(self): #保存
        if self.format:#是否设置保存格式
            my_file = QtGui.QFileDialog.getSaveFileName(self, u'文件另存为', 'save',self.format )
            print my_file
            save_path = unicode(my_file).replace('/','\\')
            print self.new_img

            self.new_img.save(save_path)
            my_button = QMessageBox.information(self,u'提示', u'保存成功',u'是的' )
        else:
            my_button = QMessageBox.warning(self,u'警告', u'请选择图片保存方式',u'选择' )
    @pyqtSignature("")
    def on_pushButton_11_clicked(self):
        x=self.lineEdit.text()
        y=self.lineEdit_2.text()
        if x and y:
            (x_o,y_o) = self.new_img.size
            y = y_o * int(x) / x_o
            print x_o
            print y_o
            print x
            print y
            self.new_img = self.new_img.resize((int(x), int(y)))#自定义图像大小
        self.new_img.show()
        #my_button = QMessageBox.warning(self,u'提示', u'请先填写像素值',u'是的' )
    @pyqtSignature("")
    def on_pushButton_12_clicked(self):
        my_button = QMessageBox.information(self,u'提示', u'为了图像质量根据PX保证原图像的尺寸比例',u'去调整' )



class YDCD:
    def __init__(self,word, flag):
        baseURL="http://dict.youdao.com/search?q="+str(word)+"&keyfrom=dict.index"
        self.baseURL = baseURL
        self.flag=flag
        
    def getPage(self):
        try:

            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接有道失败,错误原因",e.reason
                return None
    def getcontents(self):
        page=self.getPage()
        selector=etree.HTML(page)

        if not self.flag:
            content=selector.xpath('//div[@class="trans-container"]/ul/li/text()')
            if content:
                for i in content:
                    if i.replace('\n','').replace('\t','').replace(' ',''):
                        print i.replace('\n','').replace('\t','').replace(' ','')
            else:
                pass


        else:
            content=selector.xpath('//p[@class="wordGroup"]')
            if content:
                for n in content:
                    a =n.xpath('span/a/text()')
                    b = ' '.join(a)
                    print b
            else:
                print '查询失败'




class MainWindow(QMainWindow, Ui_MainWindow,threading.Thread):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        QMainWindow.__init__(self, parent)
        threading.Thread.__init__(self)
        self.setupUi(self)
        self.flag=1
        self.baseURL = ''
        self.graphicsView_3.mousePressEvent = self.my_clicked
        self.graphicsView_4.mousePressEvent = self.my_clicked1
        self.graphicsView_5.mousePressEvent = self.my_clicked2
        self.graphicsView_2.mousePressEvent = self.my_clicked3
        self.pic_path=''
        self.musicflag=0
        self.musicnum=0
        self.musicname=[]
        self.framerate = 8000
        self.channels = 1
        self.sampwidth = 2
        self.NUM_SAMPLES = 2000
        self.TIME = 2
        self.chunk = 1024
        self.file_index =1
        self.wav_queue=Queue()
        self.level = 800
        self.mute_count_limit = 50
        self.mute_begin = 0
        self.mute_end = 1
        self.recordflag=0
        self.recordover=0
        print '1'
        self.mp3=[]
        self.updown=0
        self.tianqi={}
        self.city=[]
        self.startyuyin=0
        self.my_dir_xl=''
        # f = open('tianqi6.txt','r+')
        # content=f.readlines()
        # for i in content:
        #     self.tianqi[unicode(i[9:]).replace('\n','')]=unicode(i[0:9])
        #     self.city.append(unicode(i[9:]).replace('\n',''))

        # # #print self.tianqi
        url='http://www.360doc.com/content/16/0215/14/30681687_534766244.shtml'
        # self.l={}
        #self.mp3=[]
        html=requests.get(url).content
        selector=etree.HTML(html)
        content=selector.xpath('//div[@class="article_body"]/div/p[2]/text()')
        for content1 in content:

            b=unicode(content1.strip())
            self.tianqi[b[10:]]=b[0:9]
            self.city.append(unicode(b[10:]))



    def run(self):
        print 'mp3starting','at:',ctime()
        self.my_mp3()
        print 'finish at:',ctime()
    # def my_mp3(self):


    def my_clicked(self, e):
        webbrowser.open('www.baidu.com')
    def my_clicked1(self, e):
        webbrowser.open('www.taobao.com')
    def my_clicked2(self, e):
        webbrowser.open('http://www.sohu.com/')
    def my_clicked3(self, e):
        webbrowser.open('http://v.qq.com/')
    def getPage(self):
        try:
            print self.baseURL

            url = self.baseURL

            headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
            request = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(request)
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接有道失败,错误原因",e.reason
                return None
    def getcontents(self,flag):
        page=self.getPage()
        selector=etree.HTML(page)

        if not flag:
            content=selector.xpath('//div[@class="trans-container"]/ul/li/text()')
            if content:
                for i in content:
                    if i.replace('\n','').replace('\t','').replace(' ',''):
                        self.textBrowser.append( i.replace('\n','').replace('\t','').replace(' ',''))
            else:
                my_button = QMessageBox.warning(self,u'警告', u'这个单词背偷吃了没找到',u'是的',u'不是' )

        #汉译英
        else:
            content=selector.xpath('//p[@class="wordGroup"]')
            if content:
                for n in content:
                    a =n.xpath('span/a/text()')
                    b = ' '.join(a)#列表转为字符串
                    self.textBrowser.append(b)
            else:
                my_button = QMessageBox.warning(self,u'警告', u'选择一下怎么翻译咯',u'是的',u'不是' )
    def gettq(self):
            page=self.getPage()
            print 'what?'
            pattern = re.compile('<ul class="clearfix">\s+<li>.*?<h1>(.*?)</h1>.*?title.*?>'
                                 '(.*?)</p>.*?<p class="tem">\s+<span>(.*?)</span><em>(.*?)</em>.*?title.*?>(.*?)</span>'
                                 '.*?<span>(.*?)</span>',re.S)
            # pattern1 = re.compile('<ul class="clearfix">\s+<li>.*?<h1>(.*?)</h1>.*?title.*?>'
            #                      '(.*?)</p>.*?<span>(.*?)</span><em>(.*?)</em>.*?title.*?>(.*?)</span>'
            #                      '.*?<span>(.*?)</span>',re.S)
            pattern1 = re.compile('<div class="slid"></div>.*?<h1>(.*?)</h1>.*?title.*?>(.*?)</p>'
                                  '.*?<p class="tem">\s+<span>(.*?)</span><em>(.*?)</em>.*?title.*?>(.*?)</span>'
                                  '.*?<span>(.*?)</span>',re.S)
            pattern2 = re.compile('<li class="li.*?<span>(.*?)</span>\s+<em>(.*?)</em>\s+'
                                  '<p>(.*?)</p>',re.S)
            print 'zha'
            #print page
            result = re.findall(pattern,page)
            print result
            print 's'
            result1 = re.findall(pattern1,page)
            print 's'
            result2 = re.findall(pattern2,page)
            print u'查询结束'
            f=result[0][2]+result[0][3]
            f1=result1[0][2]+result1[0][3]
            self.textBrowser.append(unicode(result[0][0])+'       '+unicode(result1[0][0]))
            self.textBrowser.append(unicode(result[0][1])+'             '+unicode(result1[0][1]))
            self.textBrowser.append(unicode(f)+'           '+unicode(f1))
            self.textBrowser.append(unicode(result[0][4])+'           '+unicode(result1[0][4]))
            self.textBrowser.append(unicode(result[0][5])+'     '+unicode(result1[0][5]))
            for i in result2:
                 self.textBrowser.append(unicode(i[1]+' : '+i[0]))
                 self.textBrowser.append(unicode(i[2]))
            # self.textBrowser.append(unicode(result2[0][1]+' : '+result2[0][0]))
            # self.textBrowser.append(unicode(result2[0][2]))
            # self.textBrowser.append(unicode(result2[1][1]+' : '+result2[1][0]))
            # self.textBrowser.append(unicode(result2[1][2]))

    @pyqtSignature("")
    def on_pushButton_clicked(self):
        print 'sssss'
        self.textBrowser.setText('')
        self.textBrowser.setStyleSheet((""))
        a= self.lineEdit.text()
        b = unicode(a)
        if self.tianqi.has_key(b):
            c= self.tianqi[b]
        else:
            my_button = QMessageBox.warning(self,u'警告', u'该城市确定是中国的？',u'换个地方查查',u'' )
        self.baseURL='http://www.weather.com.cn/weather1d/'+str(c)+'.shtml'
        print u'正在查询'
        self.gettq()

    @pyqtSignature("")
    def on_pushButton_2_clicked(self):
        self.recordflag=1
        self.startyuyin = 1
        print self.startyuyin
        sleep(0.5)
        print '111'


        sleep(10)
        print '222'
        print 'over'
        if self.recordover==1:
            print 'dianle'
            self.on_pushButton_clicked()
            self.recordover=0
        else:
            self.textBrowser.setText(u'语音识别不成功请重试')





    

    @pyqtSignature("")
    def on_radioButton_clicked(self):

        print '1'

    @pyqtSignature("")
    def on_radioButton_2_clicked(self):
        print 'w'
    
    @pyqtSignature("")
    def on_pushButton_3_clicked(self):#提交单词

        a=1
        if self.radioButton.isChecked():
            self.flag = 1
        elif self.radioButton_2.isChecked():
           self.flag = 0
        else:
            my_button = QMessageBox.warning(self,u'警告', u'选择一下怎么翻译咯',u'是的',u'不是' )
            a=0
        if a:
            self.textBrowser.setText('')
            self.textBrowser.setStyleSheet((""))
            word = self.lineEdit.text()
            self.baseURL="http://dict.youdao.com/search?q="+str(word)+"&keyfrom=dict.index"
            self.getcontents(self.flag)

    @pyqtSignature("")
    def on_pushButton_4_clicked(self):
        self.textBrowser.setText('')
        self.textBrowser.setStyleSheet(("border-image: url(:/pic/145558595715.jpg);"))
    @pyqtSignature("")
    def on_pushButton_5_clicked(self):#选择图片

        my_file_path = QtGui.QFileDialog.getOpenFileName(self,u'打开文件','/','jpg(*.jpg)')
        self.pic_path = unicode(my_file_path).replace('/','\\')
        print self.pic_path
        self.textBrowser_2.setStyleSheet(("border-image: url("+unicode(my_file_path)+");"))
        print 'k'
    @pyqtSignature("")
    def on_pushButton_6_clicked(self):
        if self.pic_path:
            dealpic = Dialog(self.pic_path)
            dealpic.exec_()
        else:
            my_button = QMessageBox.warning(self,u'警告', u'先选择一张图片啦',u'OK' )
    @pyqtSignature("")
    def on_pushButton_7_clicked(self): #听音乐
        if self.mp3:
            my_button = QMessageBox.information(self,'Information', u'播放目录已有歌曲是否继续添加',u'添加',u'取消' )
            if not my_button: #添加
                #my_button = QMessageBox.information(self,u'提示', u'选择音乐MP3所在文件夹',u'选择' )
                my_dir =QtGui.QFileDialog.getExistingDirectory(self, u'选择mp3所在文件夹', '/')
                for i in glob(join(unicode(my_dir),'*.mp3')):
                    save_path = unicode(i).replace('\\','\\\\')
                    if unicode(save_path).encode('gbk') in self.mp3:
                        pass
                    else:
                        index=save_path.rindex('\\')
                        self.musicname.append(save_path[index+1:-4])#获取歌曲的名字
                        self.mp3.append(unicode(save_path).encode('gbk'))
                print len(self.mp3),u'首歌'
                a = u'一共'+str(len(self.mp3))+u'首'
                self.lineEdit_2.setText(a)
        else:
            my_button = QMessageBox.warning(self,u'提示', u'选择音乐MP3所在文件夹',u'选择' )
            my_dir =QtGui.QFileDialog.getExistingDirectory(self, u'选择mp3所在文件夹', '/')
            for i in glob(join(unicode(my_dir),'*.mp3')):
                save_path = unicode(i).replace('\\','\\\\')
                index=save_path.rindex('\\')
                self.musicname.append(save_path[index+1:-4])#获取歌曲的名字
                self.mp3.append(unicode(save_path).encode('gbk'))#放完整的路径
            print '1111111111111'
            #self.lineEdit_2.setText(u'一共'+str(len(self.mp3))+u'首')
        self.musicflag = 1
    @pyqtSignature("")
    def on_pushButton_8_clicked(self):
        if self.musicflag:
            self.musicflag = 0
        else:
            self.musicflag = 1

    def my_mp3(self):
        while True:
            if not self.musicflag:
                continue
            else:
                if len(self.mp3)-self.musicnum>0:#判断是否最后一个，是的话提到第一个
                    #self.lineEdit_2.setText(u'正在播放的是')
                    self.lineEdit_2.setText(self.musicname[self.musicnum])
                    filename=self.mp3[self.musicnum]#格式与编码的重要性
                    print filename
                    mp3 = mp3play.load(filename)
                    mp3.play()
                    starttime=time.time()
                    musiclen=mp3.seconds()#计算每首歌的长度
                    print '1'
                    while time.time()-starttime < musiclen:
                        if not self.musicflag:#音乐标志位为0，按下了开始/暂停建
                            if self.updown:
                                mp3.stop()
                                self.musicnum-=1
                                self.updown=0
                                break
                            else:
                                mp3.pause()#暂停
                                while True:
                                    if self.musicflag:
                                        mp3.unpause()
                                        break

                        else:
                            continue
                else:
                    self.musicnum=-1
            self.musicnum+=1
    @pyqtSignature("")
    def on_pushButton_9_clicked(self):#上一曲

        if self.musicnum==0:
            my_button = QMessageBox.warning(self,u'啦啦啦', u'已经是第一首咯',u'OK' )
        else:
            self.updown=1 #标志着是上下曲按下
            self.musicflag = 0
            sleep(0.5)
            self.musicnum = self.musicnum-1
            print self.musicnum
            self.musicflag = 1

    @pyqtSignature("")
    def on_pushButton_10_clicked(self):
        allnum=len(self.mp3)
        if int(self.musicnum)+1==allnum:
            my_button = QMessageBox.warning(self,u'啦啦啦', u'已经是z最后一首咯',u'OK' )
        else:
            self.updown=1 #设置是上下曲按的
            self.musicflag = 0
            sleep(0.5)
            self.musicnum = self.musicnum+1
            print self.musicnum
            self.musicflag = 1
    @pyqtSignature("")
    def on_pushButton_11_clicked(self):
        print 'search'
        print self.my_dir_xl
        print u'关键词', self.lineEdit_3.text()
        if self.lineEdit_3.text() and self.my_dir_xl:
            my_list = re.split(' ',self.lineEdit_3.text())
            print my_list
            num=0
            my_xls=[]  #复制过的就不再复制（但依然会提醒关键字的位置。）
            #这里glob的作用，在指定文件夹下寻找对应的文件（匹配）
            for i in glob(join(unicode(self.my_dir_xl),'*.xls')):#这里的i是每一个待搜索的xls文件。
                self.textBrowser_4.append(i)
            #注意这里的i是一个完整的地址
            #注意jion需要的事python类型，需要转化.这里很神奇，不遍历的时候是unicode表示的汉字，遍历输出就行了
            # if os.path.isdir(self.my_dir):
            #     for my_file in os.listdir(self.my_dir):
            #         if my_file[-4:] == '.xls':
            #             print my_file.decode('gbk')
            #             print join(unicode(self.my_dir),my_file.decode('gbk'))
                from xlrd import open_workbook
                wb = open_workbook(unicode(i))
                for s in wb.sheets():
                    for row in range(s.nrows):
                        for col in range(s.ncols):
                            if s.cell(row,col).value:
                                for eachone in my_list:#关键词遍历
                                    #print eachone
                                    if unicode(eachone) in unicode(s.cell(row,col).value):
                                        #self.textBrowser_4.append(i)
                                        self.textBrowser_4.append(unicode(eachone)+u':  存在'+str(row+1)+u'行' +str(col+1)+u'列')
                                        if i not in my_xls:
                                            if not os.path.exists(unicode(self.my_dir_xl)+u'\\符合条件'):
                                                #注意这里路径目录的合成注意事项
                                                os.mkdir((self.my_dir_xl)+u'\\符合条件')
                                                self.textBrowser_4.append(u'创建文件夹成功：%s'% unicode(self.my_dir_xl)+u'\\符合条件')
                                            else:
                                                self.textBrowser_4.append(u'文件夹已存在')
                                            self.textBrowser_4.append(u'正在复制文件。。。')
                                            shutil.copy(i,unicode(self.my_dir_xl)+u'\\符合条件')
                                            my_xls.append(i)
                                            self.textBrowser_4.append(u'一个文件复制完成')
                                            num+=1
            self.textBrowser_4.append(u'所有文件复制完成%s'%num)
            if num==0:
                self.textBrowser_4.append(u'指定文件夹没有excel文件或所有文件都没有关键词')

        else:
            my_button = QMessageBox.information(self,u'提示', u'请先选择文件夹和关键词',u'OK', )


    @pyqtSignature("")
    def on_pushButton_12_clicked(self):
        print 'xuanze'
        self.my_dir_xl =QtGui.QFileDialog.getExistingDirectory(self, u'选择文件夹', '/')
        #设置了全局变量为了通用
        #选择文件夹的方法，注意与之前的文件的区别
        self.textBrowser_4.append(u'文件夹为：')
        self.textBrowser_4.append(self.my_dir_xl)
    @pyqtSignature("")
    def on_actionDakaitupian_triggered(self):#打开图片
        my_file_path = QtGui.QFileDialog.getOpenFileName(self,u'打开文件','/','jpg(*.jpg)')
        self.pic_path = unicode(my_file_path).replace('/','\\')
        print self.pic_path
        self.textBrowser_2.setStyleSheet(("border-image: url("+unicode(my_file_path)+");"))
        print 'k'


    @pyqtSignature("")
    def on_actionDakaiexcel_triggered(self):#同样的操作打开excel
        print 'xuanze'
        self.my_dir_xl =QtGui.QFileDialog.getExistingDirectory(self, u'选择文件夹', '/')
        #设置了全局变量为了通用
        #选择文件夹的方法，注意与之前的文件的区别
        self.textBrowser_4.append(u'文件夹为：')
        self.textBrowser_4.append(self.my_dir_xl)


    @pyqtSignature("")
    def on_actionGuanyuruanjian_triggered(self):
        button = QMessageBox.about(self,u'使用说明', u'自制软件欢迎测试，本软件具有小巧占内存小方便，具有快速手动语音双输入'
                                                 u'天气查询与预测，并提供相应的生活提示，快读便捷的播放音乐，不用在打开复杂占内存的应用程序'
                                                 u'本软件提供快捷的图像处理处理功能，包括格式的转化（可不是修改一下后缀名就可以哦），简单的图像美化。'
                                                 u'你是否还在为打开excel太慢而苦恼，只是想看看某个词是否存在，本软件可帮你在未打开wps等情况下，快速检查'
                                                 u'多个关键字是否存在，并自动复制好相应满足条件的xls文件。'
                                                 u'在此提醒，在语音输入时，只需点一下按键就可说出城市名，等待软件自动识别响应即可，在此过程中可能会出现稍微短暂的'
                                                 u'未响应状态，不用在意，那是因为响应过程的原因，语音识别模块并不是很完善，但成功率80以上。'
                                                 u'由于本软件测试阶段采用独立exe格式，会使每次运行不会在电脑存放相关信息，会是软件每次运行和第一次'
                                                 u'一样，以后会改进。'
                                                 u'相关功能运用可联系QQ584371093'
                                                 u'自制软件欢迎测试。遇见bug欢迎反馈联系。QQ：584371093' )
    def realdisplay(self):
        if self.startyuyin:
            self.lineEdit.setText(u'请说出查询城市名')
            self.startyuyin=0
            print 'ssssssssssssssssssssssssss'

    def display(self):
        while True:
            self.realdisplay()

    def get_token(self):
        apiKey = "Dl2OyEBhh3ad6fvbfZgMON2K"

        secretKey ="3280d790894a1a4bf40449488e3309e8"
        auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id="+ apiKey +"&client_secret="  + secretKey
        res = urllib2.urlopen(auth_url)
        json_data = res.read()

        return json.loads(json_data)['access_token']
    def save_wave_file(self,filename,data):
        wf = wave.open(filename,'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes(''.join(data))
        wf.close()
    def WriteQ(self,queue,data):
        queue.put(data)
        print "size now",queue.qsize()
    def ReadQ(self,queue):
        val = queue.get()
        return val
    def my_record(self):
        while True:
            if self.recordflag==0:
                continue
            else:

                pa = PyAudio()
                my_buf = []
                count=0
                # if self.file_index > 10:
                #     self.file_index=1
                # else:
                #     pass
                stream = pa.open(format = paInt16,channels = self.channels,
                                     rate = self.framerate,input = True,
                                     frames_per_buffer = self.NUM_SAMPLES)
                    #一次读多少数据从声卡
                while count < self.TIME*10:
                        #共读取的时间
                    string_audio_data = stream.read(self.NUM_SAMPLES)
                    audio_data = np.fromstring(string_audio_data,dtype = np.short)
                    large_sample_count = np.sum(audio_data>self.level)
                    #print large_sample_count
                    if large_sample_count < self.mute_count_limit:
                        self.mute_begin=1
                    else:
                        my_buf.append(string_audio_data)
                        self.mute_begin = 0
                        self.mute_end = 1
                    count+=1
                    if (self.mute_end - self.mute_begin) > 5:
                        self.mute_begin = 0
                        self.mute_end = 1
                        print u'无效录音提前结束'
                        break
                    if self.mute_begin:
                        self.mute_end += 1
                    print '..'
                    print count
                if my_buf:
                    print 'yes'
                    self.save_wave_file('%s.wav' % str(self.file_index),my_buf)
                    filname='%s.wav' % str(self.file_index)
                    self.WriteQ(self.wav_queue,filname)
                    print '%s.wav' % str(self.file_index)
                    #self.file_index+=1
                else:
                    print 'no'

                stream.close()
            #self.textBrowser.setText(u'正在识别请稍候。。')
            self.recordflag=0
    def dump_res(self,buf):
        #print buf
        my_temp = json.loads(buf)
        if my_temp['err_no']:
            if my_temp['err_no']==3300:
                print u'参数输入不正确'
            elif my_temp['err_no']==3301:
                print u'您好像木有说话吧'
            elif my_temp['err_no']==3302:
                print u'验证失败'
            elif my_temp['err_no']==3303:
                print u'语音服务器后端问题'
            elif my_temp['err_no']==3304:
                print u'请求Gps过大'
        else:
            my_list = my_temp['result']
        #print type(my_list)
            print my_list[0]
            print my_list[0].replace('，','').replace('嗯','').replace('的','')
            my_result = unicode(my_list[0].replace('，','').replace('嗯','').replace('的','').replace('妈','').replace('唉','').replace('啊',''))
            #self.textBrowser.append(my_list [0])
            #self.lineEdit.setText(my_result)
            b = unicode(my_result)

            # if self.tianqi.has_key(b):
            #     self.recordover=1
            print type(self.city)
            for i in self.city[1:]:
                if i in b:
                    print i
                    self.lineEdit.setText(i)
                    self.recordover=1
                    break


    def use_cloud(self,token):
        while True:
            if self.recordflag ==0:
                continue
            else:
                if self.wav_queue.qsize():
                    filename=self.ReadQ(self.wav_queue)
                else :
                    continue
                fp = wave.open(filename,'rb')
                nf = fp.getframerate()#获取文件的采样点书
            #print nf
                print 'sampwidth:',fp.getsampwidth()
                print 'framerate:',fp.getframerate()
                print 'channels:',fp.getnchannels()
                f_len = nf *2*10#文件长度计算，每个采样点2个字节
                audio_data=''
                while True:
                    s1 = fp.readframes(nf)
                #print '========'

                    if s1 =='':

                        break
                    audio_data+=s1
            # audio_data = fp.readframes(nf)
            #print type(audio_data)
            #print len(audio_data)
                cuid = 'pwqagwt'
                srv_url = "http://vop.baidu.com/server_api" + '?cuid=' + cuid + '&token=' + token
                http_header = [
                    'Content-Type: autio/pcm; rate = 8000',
                    'Content-Length: %d' % f_len
                ]
            #print '0000'
                c = pycurl.Curl()
                c.setopt(pycurl.URL,str(srv_url))
                c.setopt(c.HTTPHEADER,http_header)
                c.setopt(c.POST,1)
                c.setopt(c.CONNECTTIMEOUT,80)
                c.setopt(c.TIMEOUT,80)
                c.setopt(c.WRITEFUNCTION,self.dump_res)
                c.setopt(c.POSTFIELDS,audio_data)
                c.setopt(c.POSTFIELDSIZE,f_len)
                try:
                    c.perform()
                except Exception as e:
                    print e
                sleep(0.3)

    


class MyThread1(threading.Thread):#录音部分应该接受一个标志位(采用全局变量)，在这里我的功能简单化，不是每次都录音，而是收点击
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func=func
    def run(self):
        print 'MyThread1 starting','at:',ctime()
        self.res = apply(self.func)
        print 'finish at:',ctime()
class MyThread_baidu(threading.Thread):
    def __init__(self, func,a):
        threading.Thread.__init__(self)
        self.func = func
        self.a=a
    def run(self):
        print 'MyThread_baidu starting','at:',ctime()
        self.func(self.a)
class Display(threading.Thread):
    def __init__(self, func):
        threading.Thread.__init__(self)
        self.func = func
    def run(self):
        print 'Display starting','at:',ctime()
        self.func()
if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
    app = QtGui.QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(":/pic/01.jpg"))
    #启动换面的设计
    splash.show()
    #splash.showMessage(u'正在加载图片资源。。。',Qt.AlignCenter,Qt.yellow)
    #修改字体位置颜色
    # splash.showMessage(u'正在加载音频资源。。。')
    app.processEvents()
    #
    # filename='D:\\KuGou\\我.mp3'
    # mp3 = mp3play.load(filename.encode('gbk'))
    # mp3.play()
    print '1111'
    ui = MainWindow()
    ui.setDaemon(True)
    ui.start()
    display=Display(ui.display)
    display.setDaemon(True)
    display.start()
    luyin = MyThread1(ui.my_record)
    luyin.setDaemon(True)
    luyin.start()
    print '1111'
    record=MyThread_baidu(ui.use_cloud,ui.get_token())
    record.setDaemon(True)
    record.start()
    ui.show()
    splash.close()
    sys.exit(app.exec_())
