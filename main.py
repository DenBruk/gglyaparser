# -*- coding: utf-8 -*-
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design
import csv
import time
from selenium import webdriver
import re
import os
import errno
from time import gmtime, strftime
from selenium.webdriver.common.keys import Keys
import random
import uuid
from PyQt5.QtWidgets import QFileDialog
#from selenium.webdriver import Actionchains
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.startParser)
        self.pushButton_2.clicked.connect(self.selectFile)
    def selectFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;CSV (*.csv)", options=options)
        loadedStr = ""
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                if row[0]!='id':
                    loadedStr += row[1]+"," + row[2] + "\n"
            self.textEdit.setText(loadedStr)
        self.lineEdit.setText(filename) # Сохраняем имя файла в lineEdit

    @staticmethod
    def startParsePictures(self,driver,myData,row,iter,data):
        filerandoname = uuid.uuid4()
        try:
            driver.get('https://www.google.ru/imghp?hl=ru')
            driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(row+' jpg');
            driver.find_element_by_xpath('//*[@id="lst-ib"]').send_keys(Keys.ENTER)
            time.sleep(0.5
            )
            #result = re.search('imgurl=(.*)imgrefurl', driver.find_element_by_xpath('//*[@id="rg_s"]/div[3]/a').get_attribute("href")).group(1).replace('%3A%2F%2F','://').replace('%2F','/').replace('&','').replace('%3F','?').replace('%3D','=').replace('%26','&')
            myData.append([row,re.search('imgurl=(.*)imgrefurl', driver.find_element_by_xpath('//*[@id="rg_s"]/div[5]/a').get_attribute("href")).group(1).replace('%3A%2F%2F','://').replace('%2F','/').replace('%252C','%2C').replace('&','').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%25','%'),re.search('imgurl=(.*)imgrefurl', driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a').get_attribute("href")).group(1).replace('%3A%2F%2F','://').replace('%252C','%2C').replace('%2F','/').replace('&','').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%25','%'),re.search('imgurl=(.*)imgrefurl', driver.find_element_by_xpath('//*[@id="rg_s"]/div[2]/a').get_attribute("href")).group(1).replace('%3A%2F%2F','://').replace('%252C','%2C').replace('%2F','/').replace('&','').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%25','%'),re.search('imgurl=(.*)imgrefurl', driver.find_element_by_xpath('//*[@id="rg_s"]/div[3]/a').get_attribute("href")).group(1).replace('%3A%2F%2F','://').replace('%2F','/').replace('&','').replace('%3F','?').replace('%252C','%2C').replace('%3D','=').replace('%26','&').replace('%25','%'),re.search('imgurl=(.*)imgrefurl', driver.find_element_by_xpath('//*[@id="rg_s"]/div[4]/a').get_attribute("href")).group(1).replace('%3A%2F%2F','://').replace('%2F','/').replace('&','').replace('%3F','?').replace('%3D','=').replace('%252C','%2C').replace('%26','&').replace('%25','%'),re.search('imgurl=(.*)imgrefurl', driver.find_element_by_xpath('//*[@id="rg_s"]/div[6]/a').get_attribute("href")).group(1).replace('%3A%2F%2F','://').replace('%2F','/').replace('%252C','%2C').replace('&','').replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%25','%')])
        except:
            myData.append([row])
            with open("failed/"+str(filerandoname)+".csv", "w",encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(myData)
                iter = iter+1
        return myData


    @staticmethod
    def startParseSnippets(self,data,row,deep,iter,driver):
        mData=[]
                #try:
        for y in range(deep):
            print("Текущая глубина " + str(y+1))
            if y==0:
                driver.get('https://www.startpage.com/')
                time.sleep(0.5)
                driver.find_element_by_xpath('//*[@id="query"]').send_keys(row)
                driver.find_element_by_xpath('//*[@id="query"]').send_keys(Keys.ENTER)
                for x in range(10):
                    if x==0:
                        crText = driver.find_element_by_xpath('//*[@id="first-result"]/p[2]').text.rstrip()
                        crText=re.sub('[a-z A-Zа-яА-Я0-9]*?(\.\.\.)', '', crText)
                        crText=re.sub('\d{1,2} \w{3} \d{4}','',crText)
                        crText=crText.replace(' . ','')
                        mData.append(crText+' ')
                    else:
                        crText = driver.find_element_by_xpath('//*[@id="result'+str(x+1)+'"]/div/p[2]').text
                        crText=re.sub('[a-z A-Zа-яА-Я0-9]*?(\.\.\.)', '', crText)
                        crText=re.sub('\d{1,2} \w{3} \d{4}','',crText)
                        crText=crText.replace(' . ','')
                        mData.append(crText+' ')
            else:
                try:
                    driver.find_element_by_xpath('//*[@id="nextnavbar"]/form/a').click()
                except:
                    break
                for x in range(10):
                    try:
                        crText = driver.find_element_by_xpath('//*[@id="result'+str(x+1+10*y)+'"]/div/p[2]').text
                        crText=re.sub('[a-z A-Zа-яА-Я0-9]*?(\.\.\.)', '', crText)
                        crText=re.sub('\d{1,2} \w{3} \d{4}','',crText)
                        crText=crText.replace(' . ','')
                        mData.append(crText+' ')
                    except:
                        continue
        return mData

    @staticmethod
    def startParseSnippetsYa(self,data,row,deep,iter,driver):
        mData=[]
                #try:
                #try:
        driver.get('https://yandex.ru/search/customize')
        #time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/form/div[1]/fieldset[1]/dl/dd/span/label[2]/button/span').click()
        driver.find_element_by_xpath('/html/body/form/div[4]/button[1]/span').click()

        driver.find_element_by_xpath('//*[@id="text"]').send_keys(row)
        driver.find_element_by_xpath('//*[@id="text"]').send_keys(Keys.ENTER)
        for y in range(deep):
            print("Текущая глубина " + str(y+1))
            for x in range(10):
                try:
                    crText = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/ul/li['+str(x+1)+']/div/div[2]/div').text
                    crText=re.sub('[a-z A-Zа-яА-Я0-9]*?(\.\.\.)', '', crText)
                    crText=re.sub('Читать ещё', '', crText)
                    mData.append(crText + " ")
                except:
                    None
            try:

                driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/a[1]').click()
            except:
                try:

                    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[3]/a[1]').click()
                except:
                    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[4]/a[1]').click()
            time.sleep(1)
        return mData
    @staticmethod
    def parse_escaped_character_match(match):
        return unichr(int(match.group(1), 16))

    def startParser(self):
        text = self.textEdit.toPlainText()
        stopWords = self.te.toPlainText()
        deep = self.spinBox.value()
        data=text.splitlines()
        stopWordsData = stopWords.splitlines()
        myData = []
        readyData = []
        iter=0;
        driver=webdriver.Chrome('chromedriver.exe');
        #driver.set_window_position(-3000, 0);
        filerandoname = uuid.uuid4()
        for row in data:
            iter=iter+1;
            searchStr = row
            for x in stopWordsData:
                searchStr = row + " -" + x
            #Сохранение картинок
            if self.radioButton_2.isChecked():
                filename ='pictures/'+str(filerandoname)+".csv"
                RESULTS = self.startParsePictures(self,driver,myData,searchStr,iter,data)
                print(iter/len(data),iter, len(data),row)
                rows=""
                i=0
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(filename,'a',encoding = 'utf-8') as resultFile:
                    wr = csv.writer(resultFile, lineterminator='\n',delimiter=';')
                    RESULTS=RESULTS[::-1]
                    try:
                        myrow = str(iter)+","+row+","+RESULTS[0][1]+","+RESULTS[0][2]+","+RESULTS[0][3]+","+RESULTS[0][4]+","+RESULTS[0][5]
                    except:
                        with open('failed/'+filename,'a',encoding = 'utf-8') as resulteds:
                            wr1 = csv.writer(resulteds, lineterminator='\n',delimiter=';')
                            wr1.writerow(['',row])
                    wr.writerow([myrow])
                #Удаление из файла строки в случае обрыва
                if self.lineEdit.text() != "":
                    with open(self.lineEdit.text(), 'r') as inp, open(self.lineEdit.text(), 'w') as out:
                        writer = csv.writer(out)
                        for row in csv.reader(inp):
                            if row[0] != str(iter):
                                writer.writerow(row) #TODO если выкидывает except на RESULT, то формировать новый файл для отправки, отформа
            elif self.radioButton_3.isChecked():
                filename ='google/'+str(filerandoname)+".csv"
                RESULTS = self.startParseSnippets(self,data,searchStr,deep,iter,driver)
                print(RESULTS)
                print(iter/len(data),iter, len(data),row)
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                for i in range(len(RESULTS)):
                    RESULTS[i]=RESULTS[i].replace('\n',' ')
                RESULTS.insert(0,row)
                with open(filename, "a",newline='',encoding='utf-8') as f:
                    writer = csv.writer(f,delimiter=";")
                    writer.writerow(RESULTS)

            elif self.radioButton_1.isChecked() or self.radioButton_4.isChecked():
                if self.radioButton_4.isChecked():
                    snips = self.startParseSnippetsYa(self,data,searchStr,deep,iter,driver)
                    yaorgoo='yandex'
                else :
                    snips = self.startParseSnippets(self,data,searchStr,deep,iter,driver)
                    yaorgoo = 'google'
                pics = self.startParsePictures(self,driver,myData,searchStr,iter,data)
                #snips=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
                #pics=[['1','2','3','4']]
                i = 0
                pics=pics[::-1]
                resulthtml=""
                i = 0
                firstsnippet = ""
                otherSnippets = ""
                otherPics = ""
                for x in snips:
                    if i<=self.spinBox_2.value()-1:
                        firstsnippet += snips[i].replace('\n'," ")
                    else:
                        otherSnippets +=snips[i].replace('\n'," ")
                    i=i+1
                for x in pics[0][2:]:
                    otherPics += x + ","
                rndP = random.randint(self.spb_3.value(),self.spb_4.value()) # Рандомное количество абзацев
                rndSnips = []
                abz1 =""
                abz2 =""
                for x in range(rndP):
                    rndSnips.append(random.randint(self.spb_5.value(),self.spb_6.value())) #Рандомное колbrичество сниппетов в каждом абзаце
                for x in range(self.spinBox_2.value()):
                    abz1+=snips[x]
                prevSnip=0
                i=0
                try:
                    for y in range(rndP):
                        abz2 += '<br>'+'<img class="alignnone size-full wp-image-60" src="'+pics[0][x+2]+'" />' + '<br>'
                        for x in range(rndSnips[y-1]):
                            abz2 += snips[i+rndP]
                            i+=1
                    i=0
                except:
                    print("Ошибка данных в строке ",row)
                    failarray = ['',row]
                    with open('failed/'+str(filerandoname)+".csv", "a",newline='',encoding='utf-8') as f:
                            writer = csv.writer(f,delimiter=";")
                            writer.writerow(failarray)
                            continue
                abz1 = abz1.replace('\n'," ")
                abz2 = abz2.replace('\n'," ")
                if self.radioButton_6.isChecked():
                    try:
                        result = [row.capitalize(),abz1,'<!--more-->',abz2,pics[0][1]]
                    except:
                        print("Что-то пошло не так",row)
                        failarray = ['',row]
                        with open('failed/'+str(filerandoname)+".csv", "a",newline='',encoding='utf-8') as f:
                            writer = csv.writer(f,delimiter=";")
                            writer.writerow(failarray)
                else:
                    try:
                        result = [row.capitalize(), firstsnippet,otherSnippets,pics[0][1],otherPics]
                    except:
                        failarray = ['',row]
                        with open('failed/'+str(filerandoname)+".csv", "a",newline='',encoding='utf-8') as f:
                            writer = csv.writer(f,delimiter=";")
                            writer.writerow(failarray)
                filename ='mix/'+yaorgoo+'/'+str(filerandoname)+".csv"
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(filename, "a",encoding='utf-8') as output:
                    writer = csv.writer(output, lineterminator='\n',delimiter=';')
                    if iter==1:
                        writer.writerow(['','','','',''])
                    writer.writerow(result)
                print(iter/len(data),iter, len(data),row)
            elif self.radioButton.isChecked():
                filename ='yandex/'+str(filerandoname)+".csv"
                RESULTS = self.startParseSnippetsYa(self,data,searchStr,deep,iter,driver)  #Парсер яндекса
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc: # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                RESULTS.insert(0,row)
                with open(filename, "a",newline='',encoding='utf-8') as f:
                    writer = csv.writer(f,delimiter=";")
                    writer.writerow(RESULTS)
                print(iter/len(data),iter, len(data),row)
        driver.close()
        print('DONE')
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
