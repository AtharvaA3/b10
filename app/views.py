from django.shortcuts import render , HttpResponse

# Create your views here.
#aftter hitting a url what is give in return that we have to right here 

# def homepage(request):   #it follow a http protocal  simple it return a "Hello " after hitting a url
#     print(request)
#     return HttpResponse("Hello")


def homepage(request):   #for html language it will return a page and its original what we want return is shown in home.html 
    print(request.method,request.user)
    return render (request, "home.html")    #for hotmail website 