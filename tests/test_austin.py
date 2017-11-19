from context import *
import pytest


# def get_input_test(msg=''):
# 		return "www.emu.edu"
# 	Austin.get_input = get_input_test

def test_domain_correct():
	# Check that a valid url is accepted
	address = "www.emu.edu"
	assert Austin.check_domain(address) == True

def test_domain_correct_longer():
	# Check that a valid url is accepted
	address = "www.emu.org/hello/world"
	assert Austin.check_domain(address) == True

def test_domain_incorrect():
	# Check that an invalid url is rejected
	address = "www.emu.me"
	assert Austin.check_domain(address) == False

def test_domain_incorrect_difficult():
	# Check that an invalid url is rejected
	address = "www.emu.government"
	assert Austin.check_domain(address) == False

def test_termination_correct():
	# Check that a valid url is accepted
	
	pass
	# implement later - need to make more descriptive termination names
	