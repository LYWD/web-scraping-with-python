# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:21:48 2018

@author: lenovo
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup



'''
https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/M/xoffset/
0/sortfeld/company/sortfolge/ASC/filterhash/ff5454a194832323cef70c2f4c531a31/
https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/M/xoffset/
20/sortfeld/company/sortfolge/ASC/filterhash/ff5454a194832323cef70c2f4c531a31/
https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/M/xoffset/
40/sortfeld/company/sortfolge/ASC/filterhash/6efcb2530fcfa96036ee65200d76ee22/
https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/M/xoffset/
60/sortfeld/company/sortfolge/ASC/filterhash/ff5454a194832323cef70c2f4c531a31/
https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/M/xoffset/
80/sortfeld/company/sortfolge/ASC/filterhash/ea63a98cf22f1aeb04d3ca5c1f0611d5/
https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/M/xoffset/
100/sortfeld/company/sortfolge/ASC/filterhash/2682ffc0cc259b1c73ff6e776a5cf288/

'''

def open_url (url):
    re_header = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
            }
    res = requests.get(url,headers=re_header)
    return res
def find_depth(res):
    soup = BeautifulSoup(res.text,"html.parser")
    depth = soup.find('li',class_='next').previous_sibling.previous_sibling.text
    return int(depth)

def find_info(response):
    #打开/创建文件,,网页下载到本地
    fo = open('soup.txt','w',encoding = "utf-8")
    fo.write(response.text)
    fo.close()
    #utf-8码
    response.encoding=response.apparent_encoding    
    soup = BeautifulSoup(response.text,"html.parser")
   
    #fileopen = open('公司名称展位国家.txt','w',encoding = "utf-8")
    
    #获取目标的内容
    target1 = soup.find_all("div",class_ = "pull-left")
    print ("所有class为pull-left的div")
    for each in target1:
        strings=each.a.text.strip().replace("\n","").replace("/","")
        list1.append(strings)
    
    #    fileopen.write(each.a.text.strip()+ '\\')
   
    target2 = soup.find_all("td",class_ = "col-sm-3 content_hall")
    print ("所有class为col-sm-3 content_hall的td")
    for each in target2:
        strings=each.a.text.strip()
        list2.append(strings)

    #    fileopen.write(each.a.text.strip() + '\\')
    
    target3 = soup.find_all("td",class_ = "col-sm-2 content_country")
    print ("所有class为col-sm-2 content_country的tdv")
    for each in target3:
         strings=each.div.div.text.strip()
         list3.append(strings)
   
    #    fileopen.write(each.div.div.text.strip()+ '\\')
    
###更改不同首字母
letter = 'A'
###更改不同结尾乱码
host='https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/\
'+letter+'/xoffset/0/sortfeld/company/sortfolge/ASC/filterhash/1b61ce8d7d962bf2e316362502084b5e/'

res = open_url(host)
depth =  find_depth(res)
dt ={}
pdDF=pd.DataFrame(dt)
list1 = []
list2 = []
list3 = []
list4 = []
###更改深度
for i in range(depth):
    ###更改不同结尾乱码
    strings1='https://exhibitors.bau-muenchen.com/en/exhibitor-details/exhibitors-brand-names/action/defaultlist/controller/Exhibitors/letter/'+letter+'/xoffset/'
    strings2='/sortfeld/company/sortfolge/ASC/filterhash/1b61ce8d7d962bf2e316362502084b5e/'
    url = strings1+str(i*20)+strings2
    res = open_url(url)
    find_info(res)

for i in range (len(list1)):
    strings=list1[i].replace(" ","+")
    url = "https://cn.bing.com/search?q="+strings+"&qs=n&form=QBRE&sp=-1&pq="+strings+"&sc=0-0&sk=&cvid=CC61018545B74EC8843DC3D747ED269C"
    res = open_url(url)
    soup = BeautifulSoup(res.text,"html.parser")
    fileopen = open('websearchsoup/soup'+str(i)+'.txt','w',encoding = "utf-8")
    fileopen.write(res.text)
    fileopen.close()
    target4 = None
    target4=soup.find("div",class_="b_attribution")
    if (target4 !=None ):
        print("找到第一个class为b_attribution的div")
        strings = target4.cite.text
        list4.append(strings)
    else:
        print("跳过")
        list4.append("")

pdDF.columns.insert(0,'公司名称')
pdDF.columns.insert(1,'展位')
pdDF.columns.insert(2,'国家')
pdDF.columns.insert(3,'网址')
pdDF['公司名称']=list1
pdDF['展位'] = list2
pdDF['国家'] = list3
pdDF['网址'] =list4
pdDF.to_excel('bau.xlsx',sheet_name='Sheet1')


#获取网页
#    response = requests.get(url,headers=re_header)

#更改编码
#response.encoding = 'gbk'

#获得BeautifulSoup对象
#soup = BeautifulSoup(r.text,"html.parser")

#获得章节内容
#chapter_content = soup.select('#nr1')[0].text

#打开/创建文件
#fo = open('1.txt','w')

#fo.write((chapter_content).encode('utf-8'))

#print(chapter_content)

#使用完后关闭文件
#fo.close()

#print('下载成功')


