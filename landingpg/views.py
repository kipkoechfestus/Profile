from django.shortcuts import render

# Create your views here.

def landingpgView(request):
	template='landingpg/landingpg.html'
	context={}
	return render(request,template,context)