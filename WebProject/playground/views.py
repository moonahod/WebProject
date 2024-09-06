from django.shortcuts import render
from django.http import HttpResponse


def greeting(request):
    response =  HttpResponse('Hello, Im a banana')