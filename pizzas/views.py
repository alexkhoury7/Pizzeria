from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.template import loader
# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizza_options(request):
    pizza_options = Pizza.objects.filter().order_by()

    context = {'pizza_options':pizza_options}
    return render(request, 'pizzas/pizza_options.html', context)

def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=pizza)
    comment = pizza.comment_set.all()

    context = {'pizza':pizza, 'toppings':toppings, 'comment':comment}
        
    return render(request, 'pizzas/pizza.html', context)

def toppings(request, topping_id,pizza_id):
    toppings = Topping.objects.get(id=topping_id)
    pizza = Pizza.objects.get(id=pizza_id)

    context = {'toppings':toppings,'pizza':pizza}
    return render(request, 'pizzas/pizza.html', context)

def comments(request,pizza_id):    
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comments = form.save(commit=False)
            comments.pizza = pizza
            comments.save()
            
            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/comments.html', context)


