from django.http import HttpResponse
  
def index(request):
    return HttpResponse("Таня - любимая девочка!!!!!!!!!!!")
