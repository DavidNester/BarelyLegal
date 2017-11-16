class Domain:
    def __init__(self, domain):
        self.domain = domain
        self.urls_to_visit = [domain]
        self.urls_visited = set()
        self.rp = robotparser.RobotFileParser()
        self.rp.set_url(domain + "/robots.txt")
        self.rp.read()
        self.wait_time = self.rp.crawl_delay("*")
        if self.wait_time is None:
            self.wait_time = 0

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
