from django.http import HttpResponse

def index(request):
    return HttpResponse('Simple home page')
