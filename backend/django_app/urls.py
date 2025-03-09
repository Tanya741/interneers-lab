from django.contrib import admin
from django.urls import path
# from django.http import HttpResponse
from django.http import JsonResponse


# def hello_world(request):
#     return HttpResponse("Hi Everyone! Nice to meet you all.")


def user_info(request):
    name= request.GET.get("name", "Sir/Mam")
    age= request.GET.get("age")
    Id= request.GET.get("id")

    return JsonResponse({"message": f"Hello, {name}!, age: {age}, id: {Id}"})
     

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', user_info),
]
