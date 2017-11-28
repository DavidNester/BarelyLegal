import json
import url
import datetime

# Global variables to store log state
MAX_WRITE_BUFFER = 5
data_to_write = {}


def append_to_log(url_object):
	"""
	Writes url objects to log file
	url_object - a URL object to be written to the file
	Returns void
	"""
	global data_to_write
	data_to_write[url_object.address] = [url_object.keywords, url_object.date]
	if len(data_to_write) == MAX_WRITE_BUFFER:
		_write_to_log(data_to_write)

def _write_to_log(data):
	"""
	Private function which writes to log.json
	data - the dictionary to be written to the file
	Returns void
	"""
	with open('log.json', 'w+') as output_file:
		json.dump(data, output_file)


if __name__ == "__main__":
	urls_list = [url.URL(str(datetime.datetime.now()), {"job" : 2}, "www.emu.edu"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 5}, "www.google.com"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 7}, "www.facebook.com"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 1}, "www.nasa.com"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 6}, "www.jmu.edu"), \
				 url.URL(str(datetime.datetime.now()), {"job" : 5}, "www.apple.com")]
	for i in range(len(urls_list)):
		append_to_log(urls_list[i])
	urls_list = []