from django.forms import ModelForm
from main.models import ItemStore

class ProductForm(ModelForm):
    class Meta:
        model = ItemStore
        fields = ["name", "amount", "price", "category", "description"]