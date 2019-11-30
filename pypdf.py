# -*- coding: utf-8 -*-
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
import re
import string
import numpy
 
 
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
    f = open("result.txt","w")
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
    with open('test.pdf', "rb") as my_pdf:
        data=sort_words(read_pdf(my_pdf))
        print(data)
        # print(read_pdf(my_pdf))