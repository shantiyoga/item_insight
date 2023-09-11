from django.urls import path
from main.views import show_item

app_name = 'main'

urlpatterns = [
    path('', show_item, name='show_item'),
]