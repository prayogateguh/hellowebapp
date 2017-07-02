from django.shortcuts import render

def index(request):
    number = 5
    name = "prayoga teguh"
    return render(request, 'index.html', {'number': number, 'name': name,})