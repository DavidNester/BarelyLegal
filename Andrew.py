'''
Assuming that we have an object:
class URL:
    float time
    string date
    dict keyword{ string key : int num }
    bool visited
    string address
'''
import time

def check_url(to_visit, domain_times):
    '''
    Check URL to make sure that it meets all of the criteria.
    to_visit is a list of url objects
    domain_times is a dict of domain name strings and floats of the time accessed
    '''
    ACCESS_TIME = 15 #Minimum number of seconds between website visits
    
    if len(to_visit) == 0:
        raise ValueError

    url = to_visit[0]
    
    #check if url.domain is in domain_times
    while time.time() - url.time() <= ACCESS_TIME:
        print('Waiting ', ACCESS_TIME - (time.time() - url.time()), ' seconds')
        time.sleep(time.time()-url.time())
