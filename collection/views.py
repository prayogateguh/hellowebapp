from django.shortcuts import render, redirect

from collection.forms import ThingForm 
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

def edit_thing(request, slug):
    thing = Thing.objects.get(slug=slug)

    form_class = ThingForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the sumbitted form and apply to the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=thing)
    
    # and render the template
    return render(request, 'things/edit_thing.html', {'thing': thing, 'form': form,})