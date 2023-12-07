from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import ItemStore
from django.urls import reverse
from django.shortcuts import render

#Tugas 4
import datetime
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt


import json

# Create your views here.
@login_required(login_url='/login')
def show_item(request):
    items = ItemStore.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'creator' : 'Shanti Yoga Rahayu',
        'id' : 2206082360,
        'class' : 'PBP D',
        'items_list': items,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
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

@csrf_exempt
def add_amount(request, item_id):
    if request.method == 'POST':
        item = ItemStore.objects.get(pk=item_id)
        item.user = request.user
        if item.amount > 0:
            item.amount += 1
            item.save()
        return HttpResponse(b"ADDED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def decrease_amount(request, item_id):
    if request.method == 'POST':
        item = ItemStore.objects.get(pk=item_id)
        item.user = request.user
        if item.amount > 1:
            item.amount -= 1
            item.save()
        else:
            item.delete()
        return HttpResponse(b"REDUCED", status=201)
    
    return HttpResponseNotFound()

@csrf_exempt
def remove_items(request, item_id):
    if request.method == "DELETE":
        item = ItemStore.objects.get(pk=item_id, user=request.user)
        item.delete()
        return HttpResponse(b"DELETED", status=201)
    
    return HttpResponseNotFound()

def edit_product(request, id):
    product = ItemStore.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_item'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_product_json(request):
    product_item = ItemStore.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = request.POST.get("category")
        user = request.user

        new_product = ItemStore(name=name, amount=amount, description=description, price=price, category=category, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_item")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = ItemStore.objects.create(
            user = request.user,
            name = data["name"],
            category = data['category'],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_json_by_user(request):
    data = ItemStore.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")