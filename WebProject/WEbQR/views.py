from django.shortcuts import render
from django.http import HttpResponse
import tkinter
import json
from tkinter import *
from tkinter import messagebox


def home(request):
    response = HttpResponse('<h1>This is our homepage</h1> <h2>HTML Image</h2> <img src="/home/artem/Pictures/Logo_QR.png" alt="LOGO" width="499" height="500">')
    return response

def guide(request):
    response = HttpResponse('<h1>The Guide on how to use Olympia will come soon</h1>')
    return response

def start(request):
    response = HttpResponse('<h1>Here you could start using Olympia</h1>')
    return response

def code(request):
    response = HttpResponse('<h1>Wait a bit and the project will be launched</h1>')
    return response
