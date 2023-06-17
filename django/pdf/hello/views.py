from django.http import HttpResponse
  
def index(request):
    return HttpResponse("<h2>Таня - любимая девочка!!!!!!!!!!!</h2>")
    
def about(request,name,age,cute,beauty):
    return HttpResponse(f"""
    <h2>О Таньке</h2>
    <p>Имя: {name}</p>
    
    <p>Возраст: {age}</p>
    <p>Красота: {beauty}</p>
    <p>Милота: {cute}</p>
    
    """)
    
def contact(request):
    return HttpResponse("<h2>Таня - 8 888 555 35 35</h2>")
