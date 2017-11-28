import json
import url
import datetime

MAX_WRITE_BUFFER = 5
data_to_write = {}


def append_to_log(url_object):
	global data_to_write
	data_to_write[url_object.address] = [url_object.keywords, url_object.date]
	print(data_to_write)
	if len(data_to_write) == MAX_WRITE_BUFFER:
		write_to_log(data_to_write)
		data_to_write = {}

def write_to_log(data):
	with open('log.json', 'w+') as output_file:
		json.dump(data, output_file)


if __name__ == "__main__":
	urls_list = [url.URL(str(datetime.datetime.now()), {"job" : 2}, "www.emu.edu"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 5}, "www.google.com"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 7}, "www.facebook.com"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 1}, "www.nasa.com"),\
				 url.URL(str(datetime.datetime.now()), {"job" : 6}, "www.jmu.edu"), \
				 url.URL(str(datetime.datetime.now()), {"job" : 5}, "www.apple.com")]
	for i in range(urls_list):
		append_to_log(urls_list[i])