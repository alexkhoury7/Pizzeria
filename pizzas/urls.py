from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizza_options',views.pizza_options, name='pizza_options'),
    path('pizza_options/<int:pizza_id>/',views.pizza, name ='pizza'),
    path('comments/<int:pizza_id>/',views.comments, name='comments'),
    path('picture', views.pizza, name="picture"),
    
]

