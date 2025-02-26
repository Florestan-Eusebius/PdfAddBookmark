# PdfAddBookmark
Add bookmark to a pdf file from a txt file
## 基本說明
提供Python腳本，運行腳本需要PyPDF2包的支持，運行
```bash
pip install PyPDF2
```
即可安裝。

使用時將需要添加目錄的pdf文件、保存有目錄的txt文件和python腳本放在同一文件夾下，運行之，按照提示輸入即可。
## 目錄文件格式要求
- 目錄文件爲文本文件，後綴爲`.txt`。
- 目錄文件中一行形成一個書籤。不能有空行。尤其注意文件結尾處。
- 形成書籤的一行應作如下格式：開頭縮進表示層級，後面是文件名，再後面空一格或以上寫頁碼。
- 表示層級的縮進有如下功能：
  - 縮進量相同的書籤同級；
  - 若此行縮進大於上一行，則此書籤爲上一行的子書簽；
  

具體格式示例見示例文件。
## 頁碼偏移量
程序要求用戶輸入的第三個數值是頁碼偏移量，這個量作如下定義：定位到pdf文件的某一頁，這一頁在目錄中顯示爲第x頁，但如果算上封面、前言、目錄等的頁數，它實際上是該文件的第y頁。顯然，x不大於y，定義y和x的差值（一個非負整數）爲頁碼偏移量。
## 示例
在example中顯示了示例，`aim.pdf`爲待添加書籤的文件，`content.txt`爲目錄文件。以Windows系統爲例，打開Powershell，進入example文件夾後，輸入

```powershell
python pdfbookmark.py
```

將會彈出提示，按如下輸入即可

```powershell
Please input the filename (end with '.pdf'): aim.pdf
Please input the filename of you contents (end with '.txt'): content.txt
Please input the shifted page number: 13
```

然後打開`bookmarked-aim.pdf`，即可看到添加了書籤的文件。