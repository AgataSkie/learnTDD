from django.shortcuts import render

# Create your views here.
def get_short_desr(descr):
    return descr[:10]