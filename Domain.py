import time

class Domain:
    def __init__(self, domain):
        self.domain = domain
        self.time = time.time()
        self.keywords = [] #list of strings
        self.urls_to_visit = []
        self.urls_visited = set()
        self.rp = robotparser.RobotFileParser()
        self.rp.set_url(address + "/robots.txt")
        self.rp.read()
        self.wait_time = self.rp.crawl_delay("*")
        if self.wait_time is None:
            self.wait_time = 0

    def add_address(self, address):
        '''
        Checks if a url of the domain can be added to the list of urls
        to visit.
        param address:
        :return:
        '''
        pass

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