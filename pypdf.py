# -*- coding: utf-8 -*-
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import re
import string
import os
 
 
def read_pdf(pdf):
    # resource manager
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    # device
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdf)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    # 获取所有行
    # lines = str(content).split("\n")
    return content

def sort_words(strs):
    # f = open("result.txt","w")
    s = re.findall("\w+",str.lower(strs))
    #去除列表中的重复项，并排序
    l = sorted(list(set(s)))
    #去除含有数字和符号，以及长度小于5的字符串
    words=list()
    number=list()
    for i in l:
        m = re.search("\d+",i)
        n = re.search("\W+",i)
        if not m and  not n and len(i)>4 and s.count(i)>10:
            number.append(s.count(i))
            words.append(i)
            # words[count][0]=s.count(i)
            # words[count][1]=i
            # count=count+1;
            # print(i +" : "+str(s.count(i))+"\n")
            # f.write(i +" : "+str(s.count(i))+"\n
    # pages = numpy.zeros([len(words),2])
    pages = [[str(0) for i in range(2)] for j in range(len(words))]
    for i in range(len(words)):
        pages[i][0]=number[i]
        pages[i][1]=words[i]
    # print(pages)
    return sorted(pages,key=(lambda x:x[0]),reverse=True)
 
if __name__ == '__main__':
    dirname='./example'
    # dirname='./test'
    filenames=list()
    for root, dirs, files in os.walk(dirname):
        files = [f for f in files if not f[0] == '.']
        dirs = [d for d in dirs if not d[0] == '.']
        for names in files:
            filenames.append(os.path.join(root,names))
    total_data=list()
    for name in filenames:
        print(name)
        with open(name, "rb") as my_pdf:
            # total_content=total_content+read_pdf(my_pdf)
            content=read_pdf(my_pdf)
            # total_data.append(sort_words(content))
            total_data=total_data+sort_words(content)
            # print(total_content)
    sum_data=list()
    for i in range(len(total_data)):
        if(not total_data[i][1]):
            continue
        temp=[total_data[i][0],total_data[i][1]]
        # print(temp)
        for j in range(i+1,len(total_data)):
            if(total_data[i][1]==total_data[j][1]):
                temp[0]=temp[0]+total_data[j][0]
                total_data[j][1]=''
        sum_data.append(temp)
    sum_data=sorted(sum_data,key=(lambda x:x[0]),reverse=True)
    print(sum_data)