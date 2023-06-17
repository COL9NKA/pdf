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
    host = request.META["HTTP_HOST"] # получаем адрес сервера
    user_agent = request.META["HTTP_USER_AGENT"]    # получаем данные бразера
    path = request.path     # получаем запрошенный путь
    return HttpResponse(f"""<h2>Таня - 8 888 555 35 35</h2>
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)
