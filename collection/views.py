from django.shortcuts import render

from collection.models import Thing

def index(request):
    things = Thing.objects.all()
    #thing = Thing.objects.filter(name__startswith='Prayoga')

    return render(request, 'index.html', {'things': things,})