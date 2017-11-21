import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#DO NOT IMPORT ALL
#format time

#Variables used
'''
Imported:
#from Austin
current_url --> the url object

#from Brandon
class: URL (domain, time, date, keywords{"keyword": num, ...}, visited,) --> class used to store each url result 
string: domain --> url address eg: "www.emu.edu"
float: time --> computer time
string: date --> readable timestamp
dictionary: keywords --> keywords with total events
boolean: visited --> has the url been visited
string: keyword --> user entered keyword to search

Made:
#from Finn
url_index --> count for index of to_visit[]
user_keyword --> [word:#] for the keyword dictionary 
'''
#for url_index in to_visit: #url_index is the same as saying for i in...
#open domain
#read file
#this reads the html page with all the divs. We want the actual content of the page

url = (str domain, float time, string date, dict keywords("emu": 0), bool visited)

keynum = 0    

def keyword_search():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urlopen("https://www.emu.edu",context=ctx)

    bsObj = BeautifulSoup(html.read(),"html.parser")
    ##html = urlopen("file://C:/Users/carol/Desktop/Classes/Software Engineering/JobScraper/FinalProject/emu.html")
    ##bsObj = BeautifulSoup(html.read())
    bsObj = bsObj.get_text()
    print(bsObj)
    user_keyword = url.keyword[0]
    global keynum
    mywords = bsObj.split()
    for word in mywords:
        if keyword == word:
            keynum +=1
        else:
            keynum +=0

    print(keynum)
    update_keynum()
    update_date_time()



#update url_index object
def update_url_values():
    global keynum
    if keynum !=0:
        url.keyword[keyword] += keynum
    url.time = datetime.time
    url.date = datetme.date
    url.visited = False
    keynum = 0

##if keyword in file:
##    url_index.time = datetime.time #get time
##    url_index.date = datetime.date#get date
##    url_index.keywords[keyword] = keyword_count  #get count for each user_keyword
##    
