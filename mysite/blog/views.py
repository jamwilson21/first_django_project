from django.http import HttpResponse

# create your views here
def index(request):
    return HttpResponse("Hello, world. This is my first django app.")