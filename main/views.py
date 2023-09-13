from django.shortcuts import render

# Create your views here.
def show_item(request):
    context = {
        'name': 'Peony',
        'amount': 52,
        'description': 'The peony is a lush and extravagant flowering plant known for its large, fragrant, and beautifully layered blooms in a variety of colors, making it a symbol of romance and prosperity.',
        'price': 57000,
        'category':'Flowers'
    }

    return render(request, 'main.html', context)