'''
prompt user for seed(s) and add to URLs to-visit list 

prompt user for keyword (may set default)

default termination conditions = time limit OR page limit reached OR out of pages OR acquired sufficient jobs

prompt user for termination conditions
'''
from url import *

ALLOWED_DOMAINS = ['.com','.edu','.gov','.net','.org']

def check_domain(address):
    for i in ALLOWED_DOMAINS:
        if i in address:
            return True
    return False

def checktermination(cond_num, current_val, termination_val):
    '''return True if termination condition has been met, False otherwise'''
    if cond_num == '1' or cond_num == '2' or cond_num == '4':
        if current_val >= termination_val:
            return False
    elif cond_num == '3':
        if current_val == termination_val:
            # if to_visit list is empty lsit
            return False
    return True

def get_input(msg=''):
    return input(msg)


        
def get_seeds():
    seeds = []
    seed = get_input("Enter starting URL: ")
    count = 0
    while seed != '' or count == 0:
        if len(seed) >= 5 and check_domain(seed):
            # valid address
            seeds.append(seed)
            seed = get_input("Enter another URL or enter for next menu: ")
            count += 1
        elif count == 0 and seed == '':
            print("Error: Must have at least one seed")
            seed = get_input("Enter starting URL: ")
        else:
            # invalid address ending
            print("Enter URL that contains .com, .edu, .gov, .net, .org")# or enter for next menu: ")
            seed = get_input("Enter URL: ")
    return seeds

def get_keywords():
    # get keyword(s)
    keyword = get_input("Enter keyword to search for or press enter for default: ")
    multiple = True
    keywords = {}
    if keyword == '':
        keywords['job'] = 0 # change default if needed
        multiple = False
    else:
        keywords[keyword] = 0
        
    while multiple:
        keyword = get_input("Enter next keyword to search for or press enter for done: ")
        if keyword == '':
            multiple = False
        else:

            keywords[keyword] = 0
    return keywords

def get_termination_conditions():    
    # termination conditions 
    print(("\nChoose from the following termination conditions:"))
    print("1. Time limit\n2. Number of pages\n3. Until out of pages\n4. Collected a sufficient number of jobs")
    termCond = False
    while not termCond:
        choice = get_input("Enter the number cooresponding to your termination choice: ") # or d for default?
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
            termination = ['2',to_visit]
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
    seeds = get_seeds()
    keywords = get_keywords()
    termination_conditions = get_termination_conditions()
    
