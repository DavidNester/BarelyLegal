# main file import relevant functions from each persons file
# add them all to this file at the end
from domain import Domain, get_domain
from page_parser import *
import user_input
import time
import output


class Scraper:

    def __init__(self, seeds, terminate_cond, termination_data):
        self.domains = []
        self.visited_domains = set()
        self.job_urls = []
        self.terminate_cond = terminate_cond
        self.add_domains(seeds)
        self.termination_value = termination_data
        self.start_time = time.time()
        self.pages_visited = 0

    def terminated(self):
        """
        1 -- Time Limit
        2 -- Number of Pages
        3 -- Until out of Pages
        4 -- Collected sufficient number of jobs
        :return: True if should stop looking. False else
        """
        if self.terminate_cond == '1':
            if time.time() - self.start_time > self.termination_value:
                return True
        elif self.terminate_cond == '2':
            if self.pages_visited >= self.termination_value:
                return True
        elif self.terminate_cond == '3':
            for domain in self.domains:
                if len(domain.urls_to_visit) > 0:
                    return False
            return True
        elif self.terminate_cond == '4':
            if len(self.job_urls) >= self.termination_value:
                return True
        return False

    def visit_domains(self, keywords):
        while not self.terminated():
            found = False
            for domain in self.domains:
                if len(domain.urls_to_visit) > 0:
                    found = True
                    break
            if not found:
                break
            domain = self.domains.pop(0)
            self.visited_domains.update([domain])
            outside_urls = domain.visit_urls(keywords,self)
            self.add_domains(outside_urls)

    def add_domains(self,urls):
        for url in urls:
            try:
                if check_domain(url):
                    self.domains += [Domain(url)]
            except ValueError:
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
    #'''
    seeds = ['https://www.techrepublic.com/article/transform-plain-text-files-into-web-pages-automatically-with-this-php-script/']
    keywords = ['the','and']
    terminate_cond = ['3',0] # go until list is empty
    #'''
    seeds, keywords, terminate_cond = user_input.run()

    try:
        scraper = Scraper(seeds,terminate_cond[0],terminate_cond[1])
        scraper.visit_domains(keywords)
    finally:
        print("The program has exited.")
        output.convert_csv_to_json()
        
