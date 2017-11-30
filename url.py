#from Domain import get_domain
import datetime


class URL:
    date = str()
    keywords = dict()
    address = ""

    def __init__(self, date = "", keywords = {}, address = ""):
        self.date = date
        self.keywords = keywords
        self.address = address

    def toString(self):
        return self.address