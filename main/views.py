from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    return render(request,'basemain.html')


def accounts_profile(request):
    return render(request, 'basemain.html')


def acc_pro(request):
    return render(request, 'accounts_profile.html')