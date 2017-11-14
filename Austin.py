'''
prompt user for seed(s) and add to URLs to-visit list 

prompt user for keyword (may set default)

default termination conditions = time limit OR page limit reached OR out of pages OR acquired sufficient jobs

prompt user for termination conditions
'''
from url import *
to_visit = []
seeds = []
seed = input("Enter starting URL: ")
while seed != '':
    if len(seed) > 5 and ('.com' in seed or '.edu' in seed or '.gov' in seed or '.net' in seed or '.org' in seed):
        # valid address
        seeds.append(seed)
        seed = input("Enter  another URL or enter for next menu: ")
    else:
        # invalid address ending
        seed = input("Enter URL that ends with .com, .edu, .gov, .net, .org or enter for next menu: ")


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

######### create all URL objects here #########

#what do i need to initialize date and domain to?        
for i in range(len(seeds)):
    i = URL(address=seeds[i],keywords=keywords)
    to_visit.append(i)

print(to_visit)
for i in to_visit:
    print(i.toString())

    
###############################################


print(("\nChoose from the following termination conditions:"))
print("1. Time limit\n2. Number of pages\n3. Until out of pages\n4. Collected a sufficient number of jobs")
termCond = False
while not termCond:
    termination = input("Enter the number cooresponding to your termination choice: ") # or d for default?
    if termination == '1':
        # time limit
        termCond = True
    elif termination == '2':
        # number of pages
        termCond = True
    elif termination == '3':
        # until list is out of pages
        termCond = True
    elif termination == '4':
        # number of jobs
        termCond = True
    else:
        print("Error: Insert valid termination condition")
