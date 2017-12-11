import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import ssl
import url
import re

"""
This code searches a page for instances of the user's keywords and creates a url object for each page with any of the keywords found.
To run, this code needs one parameter "url" that is the address of each webpage.
"""


def keyword_search(address, keywords):
    """
    Checks for instances of keywords on page and finds other urls on page
    return: url keywords were found and list of urls found on page
    """
    ctx = ssl._create_unverified_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        html = urlopen(address, context=ctx)
    except:
        #returns empty url object and no new addresses
        print(address, 'failed to open.')
        return url.URL("", {i: 0 for i in keywords}, address), []

    bsObj = BeautifulSoup(html.read(), "html.parser")
    url_list = collect_url(bsObj,address)
    bsObj = bsObj.get_text().lower()
    mywords = bsObj.split()
    keyword_count = {i: 0 for i in keywords}
    for keyword in keywords:
        # Currently set to break the loop if any keyword is found and add the url to the list to be returned
        for word in mywords:
            if keyword.lower() == word:
                keyword_count[keyword] += 1
                #break

    return url.URL(datetime.datetime.now(), keyword_count, address), url_list


def collect_url(bsObj,address):
    if address[-1] == '/':
        address = address[:-1]
    urls = []
    for link in bsObj.find_all('a', href=True):
        new_add = link['href']
        if 'http' in new_add:
            urls += [new_add]
        elif new_add[0] == '/':
            urls += [address+new_add]
    print(urls)
    return urls


if __name__ == "__main__":
    print(keyword_search("www.emu.edu", ["Eastern", "Mennonite"])[0])