import ipdb

"""
Installation Instruction :

"""

class DomainFinder(object):
    """ A Django middleware to find the host name """

    def process_request(self, request) :
        """ Built in Django function for request processing """

        try :
            request.host = request.META['HTTP_HOST']
        except :
            request.host = None

