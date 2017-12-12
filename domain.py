from output import *
from page_parser import *

import time
from urllib import robotparser
from urllib.parse import urlparse
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from url import URL
import re


def get_domain(url):
    """
    gets domain of URL. Raises value error on invalid domain.
    :param url: string url that we want to get domain from
    :return: domain of url
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    if len(domain) > 8 and domain[:7] != 'http://' and domain[:8] != 'https://':
        print(domain)
        #running into error here with URL 'mailto:///'
        raise ValueError
    return domain


class Domain:
    def __init__(self, url):
        domain = get_domain(url)
        self.domain = domain  # The domain address (facebook.com)
        self.time = time.time()
        self.urls_to_visit = []
        self.urls_visited = set()
        self.rp = robotparser.RobotFileParser()
        self.rp.set_url(domain + "/robots.txt")
        try:
        	self.rp.read()
        except:
        	print("Invalid seed")
        	raise ValueError
        self.wait_time = self.rp.crawl_delay("*")
        if self.wait_time is None:
            self.wait_time = 5
        self.add_address(url)

    def add_address(self, url):
        '''
        Checks if a url of the domain can be added to
        the list of urls to visit.
        url: the new address to be added
        return: true if the address is in the domain.
        '''
        if get_domain(url) != self.domain:
            #print('Domain does not belong to this domain instance')
            return False
        elif url in self.urls_visited:
            #print('Site already visited')
            return True
        elif url in self.urls_to_visit:
            #print('Already going to visit site')
            return True
        elif not(self.can_visit(url)):
            self.urls_visited.add(url)
            #print('Not allowed to access url.')
            return True
        else:
            #print('Added to list to visit')
            self.urls_to_visit.append(url)
        return True

    def visit_urls(self, keywords, scraper):
        '''
        :return: set of new urls
        '''
        outside_urls = set()
        while self.has_next_url() and not scraper.terminated():
            address = self.get_next_url()
            scraper.pages_visited += 1
            url, new_urls = keyword_search(address,keywords)
            self.urls_visited.update(address)
            if url is not None:
                append_to_log(url)
            for nurl in new_urls:
                if not(self.add_address(nurl)):
                    outside_urls.update(nurl)
        #print("Url's found outside {}: {}".format(self.domain,outside_urls))
        return outside_urls


    def __eq__(self, other):
        return self.domain == other.domain

    def __hash__(self):
        return hash(self.domain)

    def __str__(self):
        return self.domain

    def has_next_url(self):
        '''
        Check URL to make sure that it meets all of the criteria. Not already visited,
        not .js, .php, or .css and met domain wait time.
        return: True if the site is valid, False otherwise
        '''
        if len(self.urls_to_visit) > 0:
        	address = self.urls_to_visit[0]
        else:
            return False
        if not(self.can_visit(address)):
            return False
        not_accepted = ['.js','.php','.css']
        for ending in not_accepted:
            if ending in address:
                return False
        if address in self.urls_visited:
            return False
        while (time.time() - self.time) <= self.wait_time:
            print('Waiting ', self.wait_time - (time.time() - self.time), ' seconds for', address)
            time.sleep(self.wait_time - (time.time() - self.time))
        return True

    def get_next_url(self):
        '''
        return - the next url
        '''
        return self.urls_to_visit.pop(0)

    def can_visit(self, url):
        if self.rp.can_fetch("*", url):
            return True
        return False

if __name__ == '__main__':
    print("Domain file stores all of the urls of one domain in lists"
          " either visited or to visit.")