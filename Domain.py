import time

def get_domain(url):
    """
    gets domain of URL
    :param url: url that we want to get domain from
    :return: domain of url
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain

class Domain:
    def __init__(self, domain):
        self.domain = domain #The domain address (facebook.com)
        self.time = time.time()
        self.keywords = [] #list of strings
        self.urls_to_visit = []
        self.urls_visited = set()
        self.rp = robotparser.RobotFileParser()
        #What happens if no robots.txt is found?
        self.rp.set_url(domain + "/robots.txt")
        self.rp.read()
        self.wait_time = self.rp.crawl_delay("*")
        if self.wait_time is None:
            self.wait_time = 0

    def add_address(self, address):
        '''
        Checks if a url of the domain can be added to
        the list of urls to visit.
        param address: the new address to be added
        :return: true if the address is in the domain.
        '''
        if  get_domain(address) != self.domain:
            return False
        elif address in self.urls_visited:
            return True
        elif address in self.urls_to_visit:
            return True
        else:
            self.urls_to_visit.append(address)
        return True

    def can_visit(self, url):
        if self.rp.canfetch("*", url.address):
            return True
        return False

    def visit_urls(self):
        while len(self.urls_to_visit) > 0:
            pass
            # visit site
            # go to site
            # get new URLS
            # add new URLS to visited
            #return list of domains found, whatever valuable info we got from

    def __eq__(self, other):
        return self.domain == other.domain

    def has_next_url(self):
        '''
        Check URL to make sure that it meets all of the criteria.
        return: True if the site is valid, False otherwise
        '''

        if (address in visited):
            return False

        while (time.time() - last_time) <= access_time:
            print('Waiting ', access_time - (time.time() - last_time), ' seconds for', site.domain)
            time.sleep(access_time - (time.time() - last_time))

        return True