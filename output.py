import json
import url
import csv

# Global variables to store log state
MAX_WRITE_BUFFER = 1 # change to 5
FILE_NAME = 'log.csv'
data_to_write = {}


def append_to_log(url_object):
    """
    Writes url objects to log file
    url_object - a URL object to be written to the file
    Returns void
    """
    global data_to_write
    data_to_write[url_object.address] = [url_object.keywords, url_object.date]
    if len(data_to_write) >= MAX_WRITE_BUFFER:
        _write_to_log(data_to_write)
        data_to_write = {}


def _write_to_log(data):
    """
    Private function which writes to the file
    data - the dictionary to be written to the file
    Returns void
    """
    with open(FILE_NAME, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        for entry in data:
            csv_writer.writerow([entry, data[entry][0], data[entry][1]])


def convert_csv_to_json():
    """
    Converts the log file into JSON format
    Returns true if the file was converted, false otherwise
    """
    result = {}
    try:
        with open(FILE_NAME, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
                for entry_id in range(len(row)):
                    row[entry_id] = row[entry_id].replace("'", "\"")
                result[row[0]] = [json.loads(row[1])] + [row[2]]
    except FileNotFoundError:
        print('Could not find csv')
        return False
    with open('log.json', 'w+') as output_file:
        json.dump(result, output_file)
        return True

if __name__ == "__main__":
    # Only for testing:
    import datetime
    urls_list = [url.URL(str(datetime.datetime.now()), {"job": 2}, "www.emu.edu"), \
                 url.URL(str(datetime.datetime.now()), {"job": 5}, "www.google.com"), \
                 url.URL(str(datetime.datetime.now()), {"job": 7}, "www.facebook.com"), \
                 url.URL(str(datetime.datetime.now()), {"job": 1}, "www.nasa.com"), \
                 url.URL(str(datetime.datetime.now()), {"job": 6}, "www.jmu.edu"), \
                 url.URL(str(datetime.datetime.now()), {"job": 5}, "www.apple.com")]
    for i in range(len(urls_list)):
        append_to_log(urls_list[i])
    urls_list = []
    convert_csv_to_json()