from django.shortcuts import render,redirect
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