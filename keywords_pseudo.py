import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import url
import re
"""
This code searches a page for instances of the user's keywords and creates a url object for each page with any of the keywords found.
To run, this code needs one parameter "url" that is the address of each webpage.
"""
keynum = 0

def keyword_search(url, keywords):
    """
    Reads website and finds instances of keywords
    url - string of website address
    Returns keynum and runs create_url_values()
    """
    global keynum
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urlopen(url, context=ctx)

    bsObj = BeautifulSoup(html.read(),"html.parser")
    bsObj = bsObj.get_text() 
    mywords = bsObj.split()
    url_list = []
    for i in keywords:
        for word in mywords:
            if keyword == word:
                keynum +=1
        url_obj = create_url_values(url,keynum)
        if not(url_obj is None):
            url_list.append(url_obj)
    return url_list


def create_url_values(url, keynum):
    """
    creates a url object if a keyword is found at least once in page
    url - string of website address
    Returns url object
    """
    if keynum > 0:
        current_url = url()
        current_url.domain(url)
        current_url.date = datetime.date
        current_url.time = datetime.time
        current_url.keyword[keyword] += keynum
        return current_url
    else:
        return None
        

def collect_url(url):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', bsObj)
    return urls


def parse_url(url, keywords):
    """
    Returns url object and a list of other urls found
    """
    url_list = keyword_search(url)
    new_urls = collect_url(url)

