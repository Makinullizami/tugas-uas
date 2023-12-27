# aplikasi_utama/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'aplikasi_utama/home.html')
