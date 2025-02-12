from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from .forms import imgForm,regForm
from .models import media,useregister
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def registration(request):
    form = imgForm()
    if request.method == "POST":
        form = imgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"register.html",{'form': form})

def vieww(request):
    cr = media.objects.all()
    return render(request,"view_products.html", {'cr':cr})

def detailvieww(request,pk):
    cr=media.objects.get(id=pk)
    return render(request,"detailed_view.html",{'cr':cr})



from django.contrib.auth import authenticate, login

def userlog(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Logs in the user and starts a session
            return redirect('view')  # Redirect to the home page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def loginn(request):
    return render(request, "login.html")

def reg2(request):
    form = regForm()
    if request.method == "POST":
        form = regForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"register2.html",{'form': form})    






def user_logout(request):
    logout(request)
    return redirect('view') 



@login_required(login_url='/logins/')
def add_to_cart(request, product_id):
    product = get_object_or_404(media, id=product_id)
    
    # Check if the product is already in the cart
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        # If the product is already in the cart, increment the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to the cart page




def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total_price() for item in cart_items)
    
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})



def increment_quantity(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def decrement_quantity(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    
    return redirect('cart')


def delete_from_cart(request, item_id):
    item = get_object_or_404(Cart, id=item_id)
    item.delete()
    return redirect('cart')