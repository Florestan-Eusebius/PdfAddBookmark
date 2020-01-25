from PyPDF2 import PdfFileReader, PdfFileWriter
import re

class PdfModify:
    def __init__(self, inputfile, contents, shiftpage=0):
        self.input=PdfFileReader(open(inputfile,'rb'))
        self.output=PdfFileWriter()
        self.output.cloneDocumentFromReader(self.input)
        self.shift=shiftpage
        fl=open(contents,'r',encoding='utf-8')
        self.bookmarklist=fl.readlines()
        fl.close()
        self.rank=0
        self.parent=[]
        self.outputtitle="bookmarked-"+inputfile
    def add_one_bookmark(self, rawbookmark):
        i=0
        while re.match(r"\s",rawbookmark[i]):
            i=i+1
        l=rawbookmark[i:]
        content=re.sub(r"\s+\d+(\n|$)",'',l)
        p=re.findall(r"\d+",rawbookmark)
        page=int(p[-1])+self.shift-1
        if i<self.rank:
            self.parent=self.parent[:-2]
        elif i==self.rank:
            self.parent=self.parent[:-1]
        else:
            pass
        if len(self.parent)==0:
            newparent=self.output.addBookmark(content,page)
            self.parent.append(newparent)
        else:
            newparent=self.output.addBookmark(content,page,self.parent[-1])
            self.parent.append(newparent)
        self.rank=i
    def add_bookmarks(self):
        for rawbookmark in self.bookmarklist:
            self.add_one_bookmark(rawbookmark)
        with open(self.outputtitle,'wb') as fout:
            self.output.write(fout)
            
inputfile=input("Please input the filename (end with \'.pdf\'): ")
contents=input("Please input the filename of you contents (end with \'.txt\'): ")
shiftpage=int(input("Please input the shifted page number: "))

filee=PdfModify(inputfile,contents,shiftpage)
filee.add_bookmarks()