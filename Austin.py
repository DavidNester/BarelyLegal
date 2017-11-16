'''
prompt user for seed(s) and add to URLs to-visit list 

prompt user for keyword (may set default)

default termination conditions = time limit OR page limit reached OR out of pages OR acquired sufficient jobs

prompt user for termination conditions
'''
from url import *

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
        
to_visit = []
seeds = []
seed = input("Enter starting URL: ")
count = 0
while seed != '' or count == 0:
    if len(seed) >= 5 and ('.com' in seed or '.edu' in seed or '.gov' in seed or '.net' in seed or '.org' in seed):
        # valid address
        seeds.append(seed)
        seed = input("Enter another URL or enter for next menu: ")
        count += 1
    elif count == 0 and seed == '':
        print("Error: Must have at least one seed")
        seed = input("Enter starting URL: ")
    else:
        # invalid address ending
        print("Enter URL that contains .com, .edu, .gov, .net, .org")# or enter for next menu: ")
        seed = input("Enter URL: ")


# get keyword(s)
keyword = input("Enter keyword to search for or press enter for default: ")
multiple = True
keywords = {}
if keyword == '':
    keywords['job'] = 0 # change default if needed
    multiple = False
else:
    keywords[keyword] = 0
    
while multiple:
    keyword = input("Enter next keyword to search for or press enter for done: ")
    if keyword == '':
        multiple = False
    else:

        keywords[keyword] = 0

# create all URL objects here
for i in range(len(seeds)):
    i = URL(address=seeds[i],keywords=keywords)
    to_visit.append(i)


##print(to_visit)
##for i in to_visit:
##    print(i.toString())
    
# termination conditions 
print(("\nChoose from the following termination conditions:"))
print("1. Time limit\n2. Number of pages\n3. Until out of pages\n4. Collected a sufficient number of jobs")
termCond = False
while not termCond:
    choice = input("Enter the number cooresponding to your termination choice: ") # or d for default?
    if choice == '1':
        # time limit
        termCond = True
        validCond = False
        while not validCond:
            try:
                timelimit = int(input("Enter the number of seconds you want the program to run for: "))
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
                pageslimit = int(input("Enter the number of pages you want the program to visit: "))
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
                jobslimit = int(input("Enter the number of jobs you want the program to collect: "))
                validCond = True
                print("Termination conditions set")
            except:
                print("Error: Please enter a valid number of jobs")
        termination = ['4',jobslimit]
    else:
        print("Error: Insert valid termination condition")


