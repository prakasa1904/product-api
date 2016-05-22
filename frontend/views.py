#from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

def index(request):
	#return render(request, 'frontend/index.html')
	return JsonResponse({'code':400, 'message':'Anda tidak memiliki permission halaman ini'})
