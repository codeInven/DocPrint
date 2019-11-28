from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    context = {"index_page": "active"} # new info here

    return render(request,"index.html",context )


    #return HttpResponse("Hello, world. You're at the main index.")
    