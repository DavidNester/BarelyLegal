# main file import relevant functions from each persons file
# add them all to this file at the end
from Domain import Domain
from David import get_domain

class Scraper:
    def __init__(self, seed):
        # list of domains
        self.domains = [Domain(get_domain(seed))]
        self.visited_domains = set()
        self.job_urls = []

    def terminated(self):
        """
        This method will decide if we should terminate based on our conditions
        Currently defaulted to just visit one domain
        Can customize later to handle different conditions
        :return: True if should stop looking. False else
        """
        if len(self.visited_domains) > 0:
            return True
        return False

    def visit_domains(self):
        while not self.terminated():
            domain = self.domains.pop(0)
            self.visited_domains += [domain]
            # domain.visit_urls() visits all pages in domain and returns a list of new domains that are found
            # and a list of relevant urls
            new_domains,relevant_urls = domain.visit_urls()