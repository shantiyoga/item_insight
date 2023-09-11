from django.shortcuts import render

# Create your views here.
def show_item(request):
    context = {
        'name': 'AI',
        'amount': 10,
        'description': 'AI in Computer Science',
        'price': 5000000,
        'category':'Book'
    }

    return render(request, 'main.html', context)