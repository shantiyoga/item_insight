from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import ItemStore
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
def show_item(request):
    items = ItemStore.objects.all()
    context = {
        'creator' : 'Shanti Yoga Rahayu',
        'id' : 2206082360,
        'class' : 'PBP D',
        'items_list': items
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_item'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = ItemStore.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ItemStore.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ItemStore.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ItemStore.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")