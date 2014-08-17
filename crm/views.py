from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.core import serializers 
import json

from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.core.serializers.json import DjangoJSONEncoder

from crm.models import SearchKeyword
# Create your views here.


def index(request):
	return render(request, 'crm/index.html')

def grab_data(request):
	keywords = SearchKeyword.objects.all()
	for keyword in keywords:
		grab_item(keyword)
	return HttpResponse('Erm')

def grab_item(keyword):
	print keyword.xpath
	return HttpResponse('Erm')




# @login_required
# def ajax_search(request,keyword):
# 	result_list = Student.objects.filter(Q(name__contains=keyword)|Q(phone__contains=keyword))
# 	context = {'result_list':result_list}
# 	data = serializers.serialize('json', result_list, fields=('name','size'))
# 	return HttpResponse(data, mimetype="application/json") 