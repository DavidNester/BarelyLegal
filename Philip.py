import re

with open('data.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')
        
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data)

print(urls)

#justtestingthingsrightnow
