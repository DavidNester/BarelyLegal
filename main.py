# main file import relevant functions from each persons file
# add them all to this file at the end
from domain import Domain, get_domain
from page_parser import *
import user_input


class Scraper:
    def __init__(self, seeds, termination_cond):
        #TODO: make a list of seeds
        self.domains = []
        self.visited_domains = set()
        self.job_urls = []
        self.termination_cond = termination_cond
        self.add_domains(seeds)

    def terminated(self):
        """
        ***This should be combined with austins function below***
        This method will decide if we should terminate based on our conditions
        Currently defaulted to just visit one domain
        Can customize later to handle different conditions
        :return: True if should stop looking. False else
        """
        if len(self.visited_domains) > 1:
            return True
        return False

    def visit_domains(self, keywords):
        while not self.terminated() and len(self.domains) > 0:
            domain = self.domains.pop(0)
            self.visited_domains.update([domain])
            outside_urls = domain.visit_urls(keywords,self)
            self.add_domains(outside_urls)

    def add_domains(self,urls):
        for url in urls:
            try:
                if check_domain(url):
                    self.domains += [Domain(url)]
            except:
                print("Invalid domain")

ALLOWED_DOMAINS = ['.com','.edu','.gov','.net','.org']


def check_domain(address):
    """
    checks given address to determine if it is valid
    returns True or False
    """
    for i in ALLOWED_DOMAINS:
        if (str(i+'/') in address or address.endswith(i)) and len(address) >= 5:
            return True
    return False


def check_termination(cond_num, current_val, termination_val):
    """
    Checking if the termination conditions have been met
    return True or False
    """
    if cond_num == '1' or cond_num == '2' or cond_num == '4':
        if current_val >= termination_val:
            return False
    elif cond_num == '3':
        if current_val == termination_val:
            # if to_visit list is empty
            return False
    return True



if __name__ == "__main__":
    # init_seed = 'https://www.techrepublic.com/article/transform-plain-text-files-into-web-pages-automatically-with-this-php-script/'
    keywords = ['most']
    seeds, keywords, terminate_cond = user_input.run()
    scraper = Scraper(seeds,termination_cond)
    scraper.visit_domains(keywords)
