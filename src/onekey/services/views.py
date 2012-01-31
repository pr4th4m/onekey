from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from onekey.debug import debug
from onekey.services.forms import AuthorForm, BookForm


def display(request) :
    ''' func to display all the services
    '''
    context = {}
    # debug()


    if request.method == 'GET' :
        author = AuthorForm()

    if request.method == 'POST' :
        debug()
        author = AuthorForm(request.POST)

    context['display_service'] = 'Services page goes here'
    context['author'] = author
    return render_to_response("services/display.html", context, RequestContext(request) )
