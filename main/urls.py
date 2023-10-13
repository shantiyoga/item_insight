from django.urls import path
from main.views import (show_item, create_product, 
                        show_xml, show_json, show_xml_by_id, show_json_by_id, 
                        register,  login_user, logout_user, add_amount, decrease_amount, edit_product, remove_items,
                        get_product_json, add_product_ajax)

app_name = 'main'

urlpatterns = [
    path('', show_item, name='show_item'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('add-amount/<int:item_id>/', add_amount, name='add_amount'),
    path('decrease-amount/<int:item_id>/', decrease_amount, name='decrease_amount'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete-product-ajax/<int:item_id>/', remove_items, name='remove_items'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax')
]