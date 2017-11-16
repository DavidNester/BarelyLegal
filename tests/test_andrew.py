from context import *
import pytest
import time


sample_url_object = url.URL(domain = "www.emu.edu", address = "www.emu.edu/visitedAlready")
visited = ["www.emu.edu/visitedAlready"]
domain_visited_times = {sample_url_object.domain:0}

def clear_variables():
	# Reset the values of testing variables
	global sample_url_object, visited, domain_visited_times
	sample_url_object = url.URL(domain = "www.emu.edu", address = "www.emu.edu/visitedAlready")
	visited = ["www.emu.edu/visitedAlready"]
	domain_visited_times = {sample_url_object.domain:0}

def test_address_already_visited():
	# The url address has already visited so the function call should return False
	clear_variables() # clear variables
	assert check_url(sample_url_object, domain_visited_times, visited) == False

def test_address_not_visited_yet():
	# The url address has not been visited so the function call should return True
	clear_variables() # clear variables
	sample_url_object.address = "www.emu.edu/notVisitedYet"
	assert check_url(sample_url_object, domain_visited_times, visited) == True

def test_part_of_address_is_in_visited():
	# A part of the url address has been visited but not the whole string. Should return True
	clear_variables() # clear variables
	sample_url_object.address = "www.emu.edu/visitedAlr"
	assert check_url(sample_url_object, domain_visited_times, visited) == True

def test_waiting_proper_time_to_revisit_domain():
	# Check that the function waits at least one second to return True
	clear_variables() # clear variables
	sample_url_object.address = "www.emu.edu/notVisitedYet"
	pre_run_time = time.time()
	domain_visited_times[sample_url_object.domain] = pre_run_time - 14
	assert check_url(sample_url_object, domain_visited_times, visited) == True
	assert time.time() - pre_run_time >= 1

def test_address_to_visit_is_not_html():
	# The given address is .js so check_url() should return False
	clear_variables() # clear variables
	sample_url_object.address = "www.emu.edu/notVisitedYet.js"
	assert check_url(sample_url_object, domain_visited_times, visited) == False

def test_address_to_visit_is_html():
	# The given address is .js so check_url() should return False
	clear_variables() # clear variables
	sample_url_object.address = "www.emu.edu/notVisitedYet.html"
	assert check_url(sample_url_object, domain_visited_times, visited) == True
