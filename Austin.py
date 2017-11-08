'''
prompt user for seed(s) and add to URLs to-visit list 

prompt user for keyword (may set default)

default termination conditions = time limit OR page limit reached OR out of pages OR acquired sufficient jobs

prompt user for termination conditions
'''
visited = []
seed = input("Enter starting URL: ")
while seed != 'n':
    if '.com' in seed or '.edu' in seed or '.gov' in seed or '.net' in seed or '.org' in seed:
        # valid address
        visited.append(seed)
        seed = input("Enter another URL or n for next menu: ")
    else:
        # invalid address ending
        seed = input("Enter URL that ends with .com, .edu, .gov, .net, .org: ")


keyword = input("Enter keyword to search for or press enter for default: ")
default = 'job' # change if needed
if keyword = '':
    keyword = default
