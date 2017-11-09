'''
prompt user for seed(s) and add to URLs to-visit list 

prompt user for keyword (may set default)

default termination conditions = time limit OR page limit reached OR out of pages OR acquired sufficient jobs

prompt user for termination conditions
'''
toVisit = []
valid = ['.com','.edu','.gov','.net','.org']
seed = input("Enter starting URL: ")
while seed != 'n':
    if '.com' in seed or '.edu' in seed or '.gov' in seed or '.net' in seed or '.org' in seed:
        # valid address
        toVisit.append(seed)
        seed = input("Enter another URL or n for next menu: ")
    else:
        # invalid address ending
        seed = input("Enter URL that ends with .com, .edu, .gov, .net, .org or n for next menu: ")


keyword = input("Enter keyword to search for or press enter for default: ")
default = 'job' # change if needed
if keyword == '':
    keyword = default

print(("\nChoose from the following termination conditions:"))
print("1. Time limit\n2. Number of pages\n3. Until out of pages\n4. Collected a sufficient number of jobs")
termCond = False
while not termCond:
    termination = input("Enter the number cooresponding to your termination choice: ") # or d for default?
    if termination == '1':
        # time limit
    elif termination == '2':
        # number of pages
    elif termination == '3':
        # until list is out of pages
    elif termination == '4':
        # number of jobs
    else:
        print("Error: Insert valid termination condition")
