from django.shortcuts import render
from .forms import imgForm
from .models import media
# Create your views here.
def home(request):
    return render(request, "index.html")

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