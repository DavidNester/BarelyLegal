from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urlopen("https://www.indeed.com/jobs?q=&l=22802",context=ctx)

bsObj = BeautifulSoup(html.read(),"html.parser")
##html = urlopen("file://C:/Users/carol/Desktop/Classes/Software Engineering/JobScraper/FinalProject/emu.html")
##bsObj = BeautifulSoup(html.read())
bsObj = bsObj.get_text()
print(bsObj)
keynum =0
keyword = "job"

mywords = bsObj.split()
for word in mywords:
    if keyword == word:
        keynum +=1
        print(word)
    else:
        keynum +=0

print(keynum)

