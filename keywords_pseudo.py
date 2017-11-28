import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import url

'''
This code searches a page for instances of the user's keywords and creates a url object for each page with any of the keywords found.
To run, this code needs one parameter "url" that is the address of each webpage.
'''
keynum = 0
keywords = ["jobs", "software"] # example keywords (these will be changed as the user specifies what they want)

def keyword_search(url):
    '''
    Reads website and finds instances of keywords
    bsObj   - website text without divs
    mywords - bsObj split into a list of individual words
    word    - each word in mywords
    Returns keynum and runs create_url_values()
    '''
    global keynum
    global keywords
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urlopen(url, context=ctx)

    bsObj = BeautifulSoup(html.read(),"html.parser")
    bsObj = bsObj.get_text() 
    mywords = bsObj.split()
    for i in keywords:
        for word in mywords:
            if keyword == word:
                keynum +=1
            else:
                keynum +=0

        print(keynum)
        create_url_values(url)



def create_url_values(url):
    '''
    creates a url object if a keyword is found at least once in page
    current_url - object name
    domain      - string address
    date        - srting readable time accessed
    time        - float computer time accessed
    keyword     - dictionary with keyword and instances
    Returns url object
    '''
    global keynum
    if keynum !=0:
        current_url = url()
        current_url.domain(url)
        current_url.date = datetme.date
        current_url.time = datetime.time
        current_url.keyword[keyword] += keynum
        
        keynum = 0


