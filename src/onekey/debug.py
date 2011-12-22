from django.conf import settings

# check it the ipdb debug variable is set to true
# if true then take to debugger mode
def debug() :
    if settings.IPDB_DEBUG  == True :
        import ipdb
        ipdb.set_trace() 
