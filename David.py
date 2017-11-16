import urllib.robotparser
from urlparse import urlparse


def get_domain(url):
    """
    gets domain of URL
    :param url: url that we want to get domain from
    :return: domain of url
    """
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain


def can_visit(url):
    """
    Checks if we are able to visit the website given a URL
    Has to find domain first
    :param url: url of website that we are checking
    :return: True if visit is allowed. False if not
    """
    domain = get_domain(url)
    rp = robotparser.RobotFileParser()
    rp.set_url(domain + "/robots.txt")
    rp.read()
    if rp.canfetch("*", url):
        return True
    return False


