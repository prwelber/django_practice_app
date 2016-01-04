from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime
from .models import Item

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    # gets all the models
    # template = loader.get_template('todo/index.html')
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
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'todo/edit.html', context)


def update(request, item_id):
    print(request.POST)
    print(request.POST['done'])
    item = get_object_or_404(Item, pk=item_id)
    print(item.done)
    item.item_text = request.POST['item_text']
    item.save()
    item.done = request.POST['done']
    item.save()
    print(item.done)
    return HttpResponseRedirect(reverse('todo:show', args=(item.id,)))


def new(request):
    return render(request, 'todo/new.html')


def create(request):
    print(request.POST)
    new_item = Item(item_text=request.POST['item_text'], pub_date=timezone.now(), due_date=request.POST['due_date'], done=False)
    new_item.save()
    return redirect('todo:index')


def delete(request):
    print(request.POST)
    item = get_object_or_404(Item, pk=request.POST['delete_id'])
    item.delete()
    return redirect('todo:index')
