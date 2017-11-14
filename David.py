import urllib.robotparser
from urlparse import urlparse


def get_domain(url):
	parsed_uri = urlparse(url)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
	return domain

def can_visit(url):
    domain = get_domain(url)
    rp = robotparser.RobotFileParser()
    rp.set_url(domain + "/robots.txt")
    rp.read()
    if rp.canfetch("*", url):
        return True
    