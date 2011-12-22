from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from onekey.debug import debug


def display(request) :
    ''' func to display all the services
    '''
    context = {}
    context['display_service'] = 'Services page goes here'
    return render_to_response("services/display.html", context, RequestContext(request) )
