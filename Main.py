# main file import relevant functions from each persons file
# add them all to this file at the end
from Domain import Domain
from keywords_pseudo import *


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
            new_domains, relevant_urls = domain.visit_urls()

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


def get_input(msg=''):
    """
    runs input function
    msg - message displayed to user
    returns input function with message
    """
    return input(msg)


def get_seeds():
    """
    gets all seeds from user
    returns list of seeds
    """
    seeds = []
    seed = get_input("Enter starting URL: ")
    count = 0
    while seed != '' or count == 0:
        if check_domain(seed):
            # valid address
            seeds.append(seed)
            seed = get_input("Enter another URL or enter for next menu: ")
            count += 1
        elif count == 0 and seed == '':
            print("Error: Must have at least one seed")
            seed = get_input("Enter starting URL: ")
        else:
            # invalid address ending
            print("Enter URL that contains .com, .edu, .gov, .net, .org")
            seed = get_input("Enter URL: ")
    return seeds


def get_keywords():
    """
    gets keywords searching for from user
    returns the list of keywords
    """
    keyword = get_input("Enter keyword to search for or press enter for default: ")
    multiple = True
    keywords = []
    if keyword == '':
        keywords.append("jobs") # change default if needed
        multiple = False
    else:
        keywords.append(keyword)
        
    while multiple:
        keyword = get_input("Enter next keyword to search for or press enter for done: ")
        if keyword == '':
            multiple = False
        else:
            keywords.append(keyword)
    return keywords


def get_termination_conditions():
    """
    gets termination conditions from the user
    returns a list containing termination conditions & values
    """
    print("\nChoose from the following termination conditions:")
    print("1. Time limit\n2. Number of pages\n3. Until out of pages\n4. Collected a sufficient number of jobs")
    termCond = False
    while not termCond:
        choice = get_input("Enter the number cooresponding to your termination choice: ")  # or d for default?
        if choice == '1':
            # time limit
            termCond = True
            validCond = False
            while not validCond:
                try:
                    timelimit = int(get_input("Enter the number of seconds you want the program to run for: "))
                    validCond = True
                    print("Termination conditions set")
                except:
                    print("Error: Please enter a valid number of seconds")
            termination = ['1',timelimit]
        elif choice == '2':
            # number of pages
            termCond = True
            validCond = False
            while not validCond:
                try:
                    pageslimit = int(get_input("Enter the number of pages you want the program to visit: "))
                    validCond = True
                    print("Termination conditions set")
                except:
                    print("Error: Please enter a valid number of pages")
            termination = ['2',pageslimit]
        elif choice == '3':
            # until list is out of pages
            termCond = True
            termination = ['2',seeds]
            print("Termination conditions set")
        elif choice == '4':
            # number of jobs
            termCond = True
            validCond = False
            while not validCond:
                try:
                    jobslimit = int(get_input("Enter the number of jobs you want the program to collect: "))
                    validCond = True
                    print("Termination conditions set")
                except:
                    print("Error: Please enter a valid number of jobs")
            termination = ['4',jobslimit]
        else:
            print("Error: Insert valid termination condition")
    return termination


if __name__ == "__main__":
    # seeds = get_seeds()
    # keywords = get_keywords()
    # termination_conditions = get_termination_conditions()
    init_seed = 'www.emu.edu'
    keywords = ['royal']
    scraper = Scraper(init_seed)
    scraper.visit_domains()

