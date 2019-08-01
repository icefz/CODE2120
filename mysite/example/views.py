from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

# Create your views here.



@csrf_exempt
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			jsob = {'demo': '123', 'var':'The Count is:'}
			data = request.POST['data']
			received = json.loads(data)
			jsob.update(received)

			index = 0
			for i in jsob['demo']:
				index += 1
			index = jsob['var']+str(index)  
			return JsonResponse({'count':index})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")



@csrf_exempt
def fib(request):
	jsob = {'startNumber':0,'length': 10}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)
			###############################################
			#everything above this line is always required#
			###############################################
			startNumber = int(jsob['startNumber'])
			length = int(jsob['length'])
			loop = range(length)
			numarray = []
			fibno = startNumber
			addno = 1
			for l in loop:
				numarray.append(fibno)
				fibno = fibno + addno	
				addno = fibno - addno

          
			return JsonResponse({"fib": numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)


'''
@csrf_exempt
def tem(request):
	jsob = {'Sydneytem ':20,'Chinatem':25,'Americantem':28,'length':'3'}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob.update(received)
			Sydneytem = int(jsob['Sydneytem'])
			Chinatem = int(jsob['Chinatem'])
			Americantem = int(jsob['Americantem'])
			length = int(jsob['length'])
			loop = range(length)
			index = []
			contem = Sydneytem,Chinatem,Americantem
			for contem in loop:
				index = str(jsob)


			

          
			return JsonResponse({"contem": index})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)





@csrf_exempt
def qwe(request):
	jsob = {'StartNumber':0,'length':15}
	log = []
	if request.method == "POST":
		try:
			data = request.POST['data']
			received = json.loads(data)
			jsob.update(received)

			StartNumber = int(jsob['StartNumber'])
			length = int(jsob['length'])
			loop = range(length)
			numarray = []
			oddno = StartNumber
			addno = 1
			for l in loop:
				numarray.append(oddno)
				while oddno < 100:
					if oddno % 2 ==1:
						addno += oddno
						oddno += 1

               
			
			return JsonResponse({'qwe':numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")





@csrf_exempt
def example_post2(request):
	log = []
	if request.method == "POST":
		try:
			jsob = {'demo': "sydney,china,american", 'var':'The whether is:'}
			split(",")
			data = request.POST['data']
			received = json.loads(data)
			jsob.update(received)

			index1 = 'rain'
			index2 = 'sun'
			index3 = 'cloudy'
			for i in jsob['demo']:
				index1 = jsob['demo']+jsob['var']+str(index1)
				index2 = jsob['demo']+jsob['var']+str(index2)
				index3 = jsob['demo']+jsob['var']+str(index3)

			return JsonResponse({'sydney': index1})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")
'''

@csrf_exempt
def FZ(request):
    jsob={}
    log=[]
    if request.method == "POST":
        try:
            data = request.POST["data"]
            received = json.loads(data)
            jsob.update(received)
            a = int(jsob["denominator"])
            b = int(jsob["numerator"])
            c = int(jsob["count"])
            s = 0
            i = 0
            for i in range(1,c):
                s += a / b
                temp = a
                a = a + b
                b = temp
                log.append(s)
                i = i+1
            su = sum(log)

            return JsonResponse({"total": su})

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            other = sys.exc_info()[0].__name__
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            errorType = str(exc_type)
            return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
    else:
        return HttpResponse("<h1>ONLY POST REQUESTS</h1>")