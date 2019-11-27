# -*- coding: utf-8 -*-
import requests,json
from bs4 import BeautifulSoup
import os
class downloader(object):
    def __init__(self):
        # self.server='http://www.jjwxc.net/'
        # self.target='http://www.jjwxc.net/onebook.php?novelid=2221448'
        self.target=r'http://www.darren-faraway.com/travel'
        # self.check_content()
        self.read_content()
        for i in range(len(self.texts)): 
            self.read_url(i)
            self.read_page()
        #     self.read_text()
        #     time.sleep(2)
            # print(len(self.texts))

    def check_content(self):
        # ssion = requests.session()
        # header = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        #     "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        #     "referer":"https://www.9siwa.com/forum.php?mod=forumdisplay&fid=47&filter=author&orderby=dateline",
        #     "sec-fetch-mode":"navigate",
        #     "sec-fetch-site":"same-origin",
        #     "sec-fetch-user":"?1",
        #     "upgrade-insecure-requests":"1",
        #     "cookie":"GEiH_2132_saltkey=rBN8H8hG; GEiH_2132_lastvisit=1574784953; GEiH_2132_smile=1D1; GEiH_2132_nofavfid=1; GEiH_2132_onlineusernum=637; GEiH_2132_sendmail=1; Hm_lvt_f60a109ae9909abf54a3d100a7b5fce3=1574763213,1574773640,1574840408,1574861594; GEiH_2132_ulastactivity=1574861593%7C0; GEiH_2132_auth=3bf0EqvC0QMiT6%2BmtUPb3%2FkwewgXOUbXtzXMQWMvx4vTCUDKsbGBt4Xx1vCdDJyNxB1yREVFpGrYvElPeWuP7pBW; GEiH_2132_lastcheckfeed=8754%7C1574861593; GEiH_2132_lip=195.176.113.113%2C1574861593; GEiH_2132_visitedfid=47D52D55D43; GEiH_2132_st_t=8754%7C1574861745%7Cc240a39488440533dcb98b4b8b78398c; GEiH_2132_forum_lastvisit=D_55_1574840632D_52_1574840648D_47_1574861745; GEiH_2132_viewid=tid_41196; GEiH_2132_checkpm=1; GEiH_2132_st_p=8754%7C1574861792%7Cf3aa4be99f90df4cc7b5a2023bdb4ec3; Hm_lpvt_f60a109ae9909abf54a3d100a7b5fce3=1574861795; GEiH_2132_lastact=1574861794%09misc.php%09patch"
        # }
        # data = {
        #     "refer":"https://www.9siwa.com/forum.php?mod=forumdisplay&fid=47&page=1",
        #     "loginfield":"username",
        #     "username":"wdwzcoco",
        #     "password":"Wd19931010",
        #     "questionid":"0",
        #     "answer":""
        # }
        # ssion.post("https://www.9siwa.com/member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash=LQpl3&inajax=1",headers=header)
        # response = ssion.get("https://www.9siwa.com/forum.php?mod=forumdisplay&fid=47&page=1")
        req = requests.get(url=self.target)
        # content=req.text.encode('ISO-8859-1','ignore').decode('GB18030','ignore')
        print(req.text)

    def read_content(self):
        # header = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        #     "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        #     "referer":"https://www.9siwa.com/forum.php?mod=forumdisplay&fid=47&filter=heat",
        #     "sec-fetch-mode":"navigate",
        #     "sec-fetch-site":"same-origin",
        #     "sec-fetch-user":"?1",
        #     "upgrade-insecure-requests":"1",
        #     "cookie":"GEiH_2132_saltkey=rBN8H8hG; GEiH_2132_lastvisit=1574784953; GEiH_2132_smile=1D1; GEiH_2132_nofavfid=1; Hm_lvt_f60a109ae9909abf54a3d100a7b5fce3=1574763213,1574773640,1574840408,1574861594; GEiH_2132_auth=3bf0EqvC0QMiT6%2BmtUPb3%2FkwewgXOUbXtzXMQWMvx4vTCUDKsbGBt4Xx1vCdDJyNxB1yREVFpGrYvElPeWuP7pBW; GEiH_2132_lastcheckfeed=8754%7C1574861593; GEiH_2132_lip=195.176.113.113%2C1574861593; GEiH_2132_visitedfid=47D52D55D43; GEiH_2132_ulastactivity=1574866242%7C0; GEiH_2132_st_t=8754%7C1574866938%7C4d334e1d4047cab0476d8100a5c34b2b; GEiH_2132_forum_lastvisit=D_55_1574840632D_52_1574840648D_47_1574866938; GEiH_2132_st_p=8754%7C1574866940%7Cc3af0ff7618817a71521a0e6c226d2fb; GEiH_2132_viewid=tid_56649; Hm_lpvt_f60a109ae9909abf54a3d100a7b5fce3=1574867495; GEiH_2132_lastact=1574867495%09misc.php%09patch"
        # }
        req = requests.get(url=self.target)
        content=req.text
        # content=req.text.encode('ISO-8859-1','ignore').decode('GB18030','ignore')
        # html = json.loads(content)
        # img = html['img']
        # print('pic:',img)
        # print(content)
        html = content
        bf = BeautifulSoup(html)
        # texts = bf.find_all('table', class_="cytable") 
        # self.texts = bf.find_all('tr',itemprop='chapter')# jinjiangwenxue
        self.texts = bf.find_all('div',class_='et_pb_ajax_pagination_container')
        # print(self.texts)
        temp=BeautifulSoup(str(self.texts))
        # print(temp)
        self.texts=temp.find_all('h2')
        # # self.texts=temp.find_all('href')
        # for each in self.texts:
        #     print(each.get('href'))
        # print(self.texts)
    def read_url(self,i):
        a_bf = BeautifulSoup(str(self.texts[i]))
        a = a_bf.find_all('a')
        print(i)
        print(a)
        for each in a:
            print(each.string, each.get('href'))
        self.filename=each.string
        self.url=each.get('href')
        # print(self.url)
    
    def read_page(self):
        dirss='E:/CODER/Spiders/'
        try:
            os.makedirs(dirss+str(self.filename))
        except:
            pass
        os.chdir(dirss+str(self.filename))
        req = requests.get(url=self.url)
        content=req.text
        html = content
        bf = BeautifulSoup(html)
        self.texts = bf.find_all('div',class_='et_post_meta_wrapper')
        self.texts = bf.find_all('img')
        id=1
        for each in self.texts:
            # print(each.get('src'))
        #     try:
            img = requests.get(each.get('src'))
        #     except:
        #         img = requests.get("https://www.9siwa.com/"+each.get('file'))
            print(each.get('src'))
            f = open(str(id)+'.jpg','ab') 
            id=id+1
            f.write(img.content) #多媒体存储content
            f.close()
        

p=downloader()