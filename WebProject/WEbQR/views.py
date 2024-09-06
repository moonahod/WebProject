from django.shortcuts import render
from django.http import HttpResponse
import tkinter
import json
from tkinter import *
from tkinter import messagebox


def home(request):
    response = HttpResponse(content='Hello, Im a banana')
    return response

def guide(request):
    response = HttpResponse('Are You a banana?')
    return response

def start(request):
    response = HttpResponse('Anyway, the day is great!')
    return response

def code(request):
    response = HttpResponse('Wait, arent you a mtber? ;)')
    return response