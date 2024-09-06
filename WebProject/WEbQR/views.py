from django.shortcuts import render
from django.http import HttpResponse
import tkinter
import json
from tkinter import *
from tkinter import messagebox


def home(request):
    response = HttpResponse(content='Hello, this is an ultimate Qr coder')
    return response

def guide(request):
    response = HttpResponse('Use it properly')
    return response

def start(request):
    response = HttpResponse('Anyway, the day is great!')
    return response

def code(request):
    response = HttpResponse('Hope you enjoy it!')
    return response
