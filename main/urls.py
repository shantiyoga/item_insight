from django.urls import path
from main.views import (show_item, create_product, 
                        show_xml, show_json, show_xml_by_id, show_json_by_id, 
                        register,  login_user, logout_user, increment, decrement, remove)

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
    path('increment/<int:item_id>/', increment, name='increment'),
    path('decrement/<int:item_id>/', decrement, name='decrement'),
    path('remove/<int:item_id>/', remove, name='remove'),
]