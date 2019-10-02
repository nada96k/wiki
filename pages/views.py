from django.shortcuts import render
from .models import Page

def Page_list(request):
	context = {

		"pages":Page.objects.all(),	
	}
	return render(request, 'list.html', context)

def Page_detail(request,page_id):
	context = {
		"page":Page.objects.get(id=page_id),	
	}
	return render(request, 'detail.html', context)