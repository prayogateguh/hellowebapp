from django.shortcuts import render

from collection.models import Thing

def index(request):
    things = Thing.objects.all()
    #thing = Thing.objects.filter(name__startswith='Prayoga')

    return render(request, 'index.html', {'things': things,})

def thing_detail(request, slug):
    # grab the object
    thing = Thing.objects.get(slug=slug)

    # pass to the template
    return render(request, 'things/thing_detail.html', {'thing': thing,})