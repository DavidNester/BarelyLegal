#from Domain import get_domain
import datetime


class URL:

    date = str()
    keywords = dict()
    address = ""

    def __init__(self, date = "", keywords = {}, address = ""):
        """
        Initializes the URL object 
        """
        self.date = date
        self.keywords = keywords
        self.address = address

    def __str__(self):
        """
        Returns the address of self
        """
        return self.address

    def __eq__(self,other):
        """
        Returns Boolean if the address of self is the same as other
        """
        return self.address == other.address
