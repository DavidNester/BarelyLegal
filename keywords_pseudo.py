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


def keyword_search(url, keywords):
    """
    Checks for instances of keywords on page and finds other urls on page
    Returns whether keywords were found and list of urls found on page
    """
    ctx = ssl._create_unverified_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        html = urlopen(url, context=ctx)
    except:
        return False
    

    bsObj = BeautifulSoup(html.read(),"html.parser")
    bsObj = bsObj.get_text().lower() 
    mywords = bsObj.split()
    url_list = collect_url(bsObj)
    keywords_found = False
    keyword_count = {i:0 for i in keywords}
    print(keyword_count)
    for keyword in keywords:
        # Currently set to break the loop if any keyword is found and add the url to the list to be returned
        for word in mywords:
            if keyword.lower() == word:
                keywords_found = True
                keyword_count[keyword] += 1
                break
    
    return create_url_values(url, keyword_count), url_list


def create_url_values(url_string, keywords_count):
    """
    creates a url object if a keyword is found at least once in page
    current_url - object name
    domain      - string address
    date        - sorting readable time accessed
    time        - float computer time accessed
    keyword     - dictionary with keyword and instances
    url - string of website address
    Returns url object
    """
    """
    This function is basically just a constructor for a URL class (which should be inside the URL class). We also may 
    not need the URL class. We have no need to store the date and time that it was accessed because we only ever access 
    a URL once. The one thing a URL class could do is be able to store the associated keywords with each URL that is 
    found but that could be done as part of the keyword_search function. -- David
    """
    current_url = url.URL(datetime.date, keywords_count, url_string)
    return current_url


def collect_url(bsObj):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', bsObj)
    return urls


if __name__ == "__main__":
    print(keyword_search("https://www.emu.edu", ["Eastern", "Mennonite"])[0])
