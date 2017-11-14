import datetime
#DO NOT IMPORT ALL
#format time

#Variables used
'''
Imported:
#from Austin
current_url --> the url object

#from Brandon
class: URL (domain, time, date, keywords{"keyword": num, ...}, visited,) --> class used to store each url result 
string: domain --> url address eg: "www.emu.edu"
float: time --> computer time
string: date --> readable timestamp
dictionary: keywords --> keywords with total events
boolean: visited --> has the url been visited
string: keyword --> user entered keyword to search

Made:
#from Finn
url_index --> count for index of to_visit[]
user_keyword --> [word:#] for the keyword dictionary 
'''
for url_index in to_visit[] #url_index is the same as saying for i in...
#open domain
#read file
#this reads the html page with all the divs. We want the actual content of the page 
    myFile = codecs.open(url_index, "r")
    print (myFile.read())
    url.index.visited = True


#count keyword events 
for user_keyword in url_index.keywords #user_keyword is the same as for i in...
    for line in myFile:
        if keyword in myFile:
            keyword_count +=1

#update url_index object
if keyword in file
    url_index.time = datetime.time #get time
    url_index.date = datetime.date#get date
    url_index.keywords[keyword] = keyword_count  #get count for each user_keyword
    
