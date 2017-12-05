from Brandon import *
from keywords import *
import time
from urllib import robotparser
from urllib.parse import urlparse
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import ssl
from url import URL
import re


def get_domain(url):
    '''
    gets domain of URL
    :param url: string url that we want to get domain from
    :return: domain of url
    '''
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


class Domain:
    def __init__(self, url):
        domain = get_domain(url)
        self.domain = domain  # The domain address (facebook.com)
        self.time = time.time()
        self.urls_to_visit = []
        self.urls_visited = set()
        self.rp = robotparser.RobotFileParser()
        # What happens if no robots.txt is found?
        self.rp.set_url(domain + "/robots.txt")
        self.rp.read()
        self.wait_time = self.rp.crawl_delay("*")
        if self.wait_time is None:
            self.wait_time = 0
        self.add_address(url)

    def add_address(self, url):
        '''
        Checks if a url of the domain can be added to the list of urls to visit.
        url: the new address to be added
        return: true if the address is in the domain.
        '''
        if get_domain(url) != self.domain:
            print('Domain does not belong to this domain instance')
            return False
        elif url in self.urls_visited:
            print('Site already visited')
            return True
        elif url in self.urls_to_visit:
            print('Already going to visit site')
            return True
        elif not(self.can_visit(url)):
            self.urls_visited.add(url)
            print('Not allowed to access url.')
            return True
        else:
            self.urls_to_visit.append(url)
        return True

    def visit_urls(self, keywords, scraper):
        '''
        return: Set of knew urls
        '''
        outside_urls = set()
        while len(self.urls_to_visit) > 0 and not scraper.terminated:
            address = self.urls_to_visit.pop(0)
            bs_obj = connect(address)
            if isinstance(bs_obj,bool) and bs_obj == False:
                print(address, 'is not valid')
            else:
                url, new_urls = parse_page(address,keywords)
                self.urls_visited.update(address)
                append_to_log(url)

            for nurl in new_urls:
                if not(self.add_address(nurl)):
                    outside_urls.update(nurl)
        return outside_urls


    def __eq__(self, other):
        return self.domain == other.domain

    def __hash__(self):
        return hash(self.domain)

    def __str__(self):
        return self.domain

    def collect_url(self, url, text):
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        return urls

    def has_next_url(self):
        '''
        Check URL to make sure that it meets all of the criteria. Not already visited,
        not .js or .php, and met domain wait time.
        return: True if the site is valid, False otherwise
        '''
        address = self.urls_to_visit.pop(0)
        if not(self._can_visit(address)):
            return False
        not_accepted = ['.js','.php']
        if not_accepted in address:
            return False
        elif address in self.urls_visited:
            return False
        while (time.time() - self.time) <= self.wait_time:
            print('Waiting ', self.wait_time - (time.time() - self.time), ' seconds for', address)
            time.sleep(self.wait_time - (time.time() - self.time()))
        return True

    def _can_visit(self, url):
        #self.rp.allow_all = True
        if self.rp.can_fetch("*", url):
            return True
        return False

if __name__ == '__main__':
    test_url = 'http://webscraper.io/test-sites/e-commerce/allinone'
    #test_url = 'https://www.techrepublic.com/article/transform-plain-text-files-into-web-pages-automatically-with-this-php-script/'
    d = Domain(get_domain(test_url))
    d.add_address(test_url)
    keywords = ['most']
    d.visit_urls(keywords)
