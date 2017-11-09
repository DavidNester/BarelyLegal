import urllib.robotparser
def checkRobots(url):
	rp = robotparser.RobotFileParser()
	rp.set_url(url+"/robots.txt")
	rp.read()
	if rp.canfetch("*",url):
		return True
	return False
		#the following came from a stackexchange post and may be useful for 
		"""
		site = urllib.request.urlopen(url)
		sauce = site.read()
		soup = BeautifulSoup(sauce, "html.parser")
		actual_url = site.geturl()[:site.geturl().rfind('/')]
		my_list = soup.find_all("a", href=True)
		for i in my_list:
			# rather than != "#" you can control your list before loop over it
			if i != "#":
				newurl = str(actual_url+"/"+i)
				try:
					if rp.can_fetch("*", newurl):
						site = urllib.request.urlopen(newurl)
						# do what you want on each authorized webpage
				except:
					pass
		"""