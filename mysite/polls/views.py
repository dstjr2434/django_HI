from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request:HttpResponse):


    return HttpResponse("Hello")

def page(request:HttpResponse, page_number):


    return HttpResponse("요청하신 페이지는" + str(page_number))

def html(request:HttpResponse):

    name = "Mingyu"
    return HttpResponse(f"<h1>안녕하세요 {name} </h1>")

def welcome(request:HttpResponse):

    context = {
        "name" : "이민규입니다."

    }

    return HttpResponse(render(request,"polls/hello.html",context))
