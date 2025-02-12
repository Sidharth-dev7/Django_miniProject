from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart
from .forms import imgForm,regForm
from .models import media,useregister
# Create your views here.
def home(request):
    cr1 = useregister.objects.all()
    cr = media.objects.all()
    return render(request, "index.html", {'cr':cr, 'cr1': cr1})


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



def userlog(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        cr=useregister.objects.filter(username=username,password=password)
        if cr:
            user_details=useregister.objects.get(username=username,password=password)
            id=user_details.id
            name=user_details.name
            request.session['id']=id
            request.session['name']=name
            return redirect('Home')
        else:
            return render(request,'login.html')


def loginn(request):
    return render(request, "login.html")

def reg2(request):
    form = regForm()
    if request.method == "POST":
        form = regForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"register2.html",{'form': form})    










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

def remove_item_from_cart(request, item_id):
    try:
        # Get the cart item by ID and delete it
        cart_item = Cart.objects.get(id=item_id)
        cart_item.delete()
    except Cart.DoesNotExist:
        pass  # Handle item not found if necessary
    
    # Redirect to the cart page after removal
    return redirect('cart') 