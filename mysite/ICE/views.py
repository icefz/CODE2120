from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *

# Create your views here.

def hello(request):
	returnob = {
	"data": "HELLO, I AM FRANK!" ,
	}
	return JsonResponse(returnob)