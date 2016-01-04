from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Item



# Create your views here.


def index(request):
    item_list = Item.objects.all()
    # gets all the models
    ###template = loader.get_template('todo/index.html')###
    # load the template from template directory
    # it's already looking in templates directory thus starting with todo
    context = {
      'item_list': item_list
    }
    # define a context object
    return render(request, 'todo/index.html', context)
    """
    The render() function takes the request object as its first 
    argument, a template name as its second argument and a 
    dictionary as its optional third argument. It returns an 
    HttpResponse object of the given template rendered with the 
    given context.
    """


def show(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    # will show 404 if no item found
    context = {
      'item': item
    }
    return render(request, 'todo/show.html', context)

def edit(request, item_id):
    response = "You can edit item %s"
    return HttpResponse(response % item_id)

def create(request):
    response = "You can create new todo items here"
    return HttpResponse(response)




