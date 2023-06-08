from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Sneakers, User, Order
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def main(request):
    sneakers = Sneakers.objects.all()
    sneakers_last3 = sneakers[sneakers.count() - 3:]
    # tasks = Task.objects.order_by('id')
    return render(request, 'main.html', {'title': 'Головна сторінка сайту', 'sneakers': sneakers_last3})


def about(request):
    return render(request, 'about.html')


def order(request):
    return render(request, 'order.html')


def basket(request):
    return render(request, 'basket.html')


def account(request):
    return render(request, 'account.html')


def news(request):
    sneakers = Sneakers.objects.all()
    sneakers_last3 = sneakers[sneakers.count() - 6:]
    return render(request, 'products.html', {'sneakers': sneakers_last3})


def store(request):
    sneaker = Sneakers.objects.all()
    return render(request, 'shoes.html', {'sneakers': sneaker})


class HomePageView(TemplateView):
    template_name = 'search.html'


def SearchResultsView(request):
    search_sneakers = request.GET.get('q', '')
    if search_sneakers:
        sneaker_set = (Q(name__icontains=search_sneakers) | Q(brand__icontains=search_sneakers))
        results = Sneakers.objects.filter(sneaker_set).distinct()
    else:
        results = []
    return render(request, 'search_results.html', {'results': results, 'sneakers': search_sneakers})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    page = 'login'

    if request.method == 'POST':
        email = request.POST.get('email', '').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            return HttpResponse('User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is uncorrect')
    context = {'page': page}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration.html", context={"register_form": form})


def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price for item in cart_items)
    context = {'cart_items': cart_items, 'cart_total': total,
               'total': total + 55}
    if request.method == 'POST':
        order = Order.objects.create(user=request.user,
                                     deliveryAddress=request.POST.get('deliveryAddress'), total_price=total)
        for cart_item in cart_items:
            OrderItem.objects.create(order=order,
                                     item=cart_item.item, quantity=cart_item.quantity)
            cart_item.delete()
        return redirect('orders')
    return render(request, 'basket.html', context)


# def registerPage(request):
#     page = 'register'
#     form = MyUserCreationForm()
#     context = {'page': page, 'form': form}
#     if request.method == 'POST':
#         form = MyUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             return HttpResponse('An error occurred during registration')
#
#     return render(request, 'registration.html', context)
