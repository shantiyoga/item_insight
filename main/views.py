from django.shortcuts import render

# Create your views here.
def show_item(request):
    context = {
        'name': 'Pink Diamond Necklace',
        'amount': 21,
        'description': 'A Pink Diamond Necklace meticulously crafted with rare, natural pink diamonds, showcasing exquisite elegance and luxury.',
        'price': 2900,
        'category':'Necklace'
    }

    return render(request, 'main.html', context)