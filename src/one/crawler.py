#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
@author: df
'''
import requests
import codecs
import re
from bs4 import BeautifulSoup

def crawler_entrance(url):
    one = []
    req = requests.get(url)
    html_doc = req.text.encode("utf-8")
    soup = BeautifulSoup(html_doc)
    tds = soup.findAll("p", attrs={"class":"cat-subject-items"})
    tdas = tds[0].select("a")
    pattern = re.compile(r'tagId=\d*')
    
    for tda in tdas:
        a = []
        tagId = pattern.findall(str(tda))[0]
        a.append(url + "&"+tagId)
        a.append(tda.get_text()) 
        one.append(a)
    return one

def commodity_list(url):
    one = []
    req = requests.get(url)
    html_doc = req.text.encode("utf-8")
    soup = BeautifulSoup(html_doc)
#     tds = soup.findAll("dd", attrs={"class":"title"}, limit=8)
    dls = soup.findAll("dl", attrs={"class":"to-item"}, limit=8)
#     print dls[0].select("dd")
    pattern = re.compile('http://item\\.taobao\\.com/item\\.htm\\?id=\\d+')
#     match = pattern.findall(str(tds))
    for commodity in dls:
        comm = []
        commdity_clear = commodity.select("dd")
        url = pattern.findall(str(commdity_clear[0].a))[0]
        price = commdity_clear[1].select("strong")[0].get_text().strip()
        real_price = commdity_clear[2].select("del")[0].get_text().strip()
        comm.append(url)
        comm.append(price)
        comm.append(real_price)
        one.append(comm)
    return one
        
def shop_list(url_list):
    for shop_list in url_list:
        url = shop_list[0]
        req = requests.get(url)
        html_doc = req.text.encode("utf-8")
        soup = BeautifulSoup(html_doc)
        shop_list.append(soup.find("h3", attrs={"class":"tb-main-title"}).get_text().strip())
#         print soup.find_all("div",attrs={"class":"tb-sell-counter"})
        #one['price'] = str(tds[0].text)
        #price = soup.findAll(attrs={"id":"J_PromoPriceNum"})
    
    return  url_list


def phone_shop_list(url):
    html_doc = requests.get(url).text.encode("utf-8")
    soup = BeautifulSoup(html_doc)
    print html_doc    


if __name__ == '__main__':
#     url = 'http://tejia.taobao.com/tejiaListRec.htm?promotionId=1'
#     entrance_url = crawler_entrance(url)
#     print entrance_url[0][1]
#     print commodity_list("http://tejia.taobao.com/tejiaListRec.htm?promotionId=1&tagId=103400")
#     one = [['http://item.taobao.com/item.htm?id=44185706165', u'44.99', u'128.00'], ['http://item.taobao.com/item.htm?id=44696936945', u'34.90', u'188.00'], ['http://item.taobao.com/item.htm?id=42945598913', u'19.90', u'68.00'], ['http://item.taobao.com/item.htm?id=44064484541', u'28.50', u'159.00'], ['http://item.taobao.com/item.htm?id=40739517488', u'24.00', u'89.00'], ['http://item.taobao.com/item.htm?id=44318165548', u'31.00', u'95.00'], ['http://item.taobao.com/item.htm?id=39846929531', u'35.00', u'218.00'], ['http://item.taobao.com/item.htm?id=43843450724', u'54.90', u'199.00']]
#     print shop_list(one)
    phone_shop_list("http://h5.m.taobao.com/awp/core/detail.htm?id=44185706165")
      
        
  
    
    
    