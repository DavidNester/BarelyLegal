#from Domain import get_domain
import datetime


class URL:

    date = str()
    keywords = dict()
    address = ""

    def __init__(self, date = "", keywords = {}, address = ""):
        """
        Initializes the URL object
        :param self: = new object
        :param date: = date visited
        :param keywords: = user defined keywords to search
        :prarm address: = the address of the new url object
        """
        self.date = date
        self.keywords = keywords
        self.address = address

    def __str__(self):
        """
        Overwrites __str__ 
        :param self: url object
        Returns the address of self
        """
        return self.address

    def __eq__(self,other):
        """
        Overwrites __eq__ to compare self and other's addresses
        :param self: First url
        :param other: Second url
        Returns Boolean if the address of self is the same as other
        """
        return self.address == other.address
