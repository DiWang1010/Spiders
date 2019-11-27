# -*- coding: utf-8 -*-
import requests
class downloader(object):
    def __init__(self):
        # self.server='http://www.jjwxc.net/'
        # self.target='http://www.jjwxc.net/onebook.php?novelid=2221448'
        self.target='https://www.9siwa.com/forum.php?mod=viewthread&tid=41196&extra=page%3D1'
        self.check_content()

        # for i in range(len(self.texts)):
        #     self.read_url(i)
        #     self.read_text()
        #     time.sleep(2)
        #     # print(len(self.texts))

    def check_content(self):
        ssion = requests.session()
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "referer":"https://www.9siwa.com/forum.php?mod=forumdisplay&fid=47&page=1",
            "sec-fetch-mode":"navigate",
            "sec-fetch-site":"same-origin",
            "sec-fetch-user":"?1",
            "upgrade-insecure-requests":"1",
            "cookie":"Hm_lvt_f60a109ae9909abf54a3d100a7b5fce3=1574500027,1574541838,1574763213,1574773640; GEiH_2132_saltkey=rBN8H8hG; GEiH_2132_lastvisit=1574784953; GEiH_2132_sendmail=1; GEiH_2132_st_t=0%7C1574788721%7C9ee831e46f45a97371f7f855f7473193; Hm_lpvt_f60a109ae9909abf54a3d100a7b5fce3=1574788723; GEiH_2132_lastact=1574788774%09member.php%09logging; GEiH_2132_ulastactivity=1574788774%7C0; GEiH_2132_auth=7504A6X4GxoW2P2upYxPBqGDZBENXKjqe553RywQOhDa%2BOpLmZz41zXY44M2Z8aFrCeBUqwi8poUTD9s6r84ONrN; GEiH_2132_lastcheckfeed=8754%7C1574788774; GEiH_2132_checkfollow=1; GEiH_2132_lip=195.176.113.70%2C1574788774"
        }
        data = {
            "refer":"https://www.9siwa.com/forum.php?mod=forumdisplay&fid=47&page=1",
            "loginfield":"username",
            "username":"wdwzcoco",
            "password":"Wd19931010",
            "questionid":"0",
            "answer":""
        }
        # ssion.post("https://www.9siwa.com/member.php?mod=logging&action=login&loginsubmit=yes&frommessage&loginhash=LQpl3&inajax=1",headers=header)
        # response = ssion.get("https://www.9siwa.com/forum.php?mod=forumdisplay&fid=47&page=1")
        req = requests.get(url=self.target,headers=header)
        # content=req.text.encode('ISO-8859-1','ignore').decode('GB18030','ignore')
        print(req.text)

    def read_content(self):
        req = requests.get(url=self.target)
        content=req.text.encode('ISO-8859-1','ignore').decode('GB18030','ignore')
        # print(content)
        html = content
        bf = BeautifulSoup(html)
        # texts = bf.find_all('table', class_="cytable") 
        # self.texts = bf.find_all('tr',itemprop='chapter')# jinjiangwenxue
        self.texts = bf.find_all('div',class_='box')
        temp=BeautifulSoup(str(self.texts))
        self.texts=temp.find_all('li')

p=downloader()