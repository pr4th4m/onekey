from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from onekey.debug import debug
from django.core.urlresolvers import reverse


def index(request):
    context = {}
    context['test_context'] = 'test_context'
    return render_to_response("index.html", context, RequestContext(request) )

def org(request, organization=None, template_name=None, model_name=None) :
    context = {}
    context['test_context'] = 'test_context'
    return render_to_response(template_name, context, RequestContext(request) )

