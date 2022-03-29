from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# these are for the index part.
from django.shortcuts import render
from .forms import CustomerForm

# these are for the index2 part.
from django.shortcuts import render
from .forms import PrivateDoctor


# Create your views here.
def home(request):
    products = Product.objects
    return render(request, 'products/index4.html', {'products': products})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and \
                request.FILES['image']:
            product = Product()
            product.tittle = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'products/create.html')


def detail(request):
    products = Product.objects
    return render(request, 'products/detail.html', {'products': products})


def GetYourDoctor(request):
    products = Product.objects
    return render(request, 'products/GetYourDoctor.html', {'products': products})


def UserInfo(request):
    products = Product.objects
    return render(request, 'products/UserInfo.html', {'products': products})


def LabTest(request):
    products = Product.objects
    return render(request, 'products/LabTest.html', {'products': products})


def GoogleMap(request):
    products = Product.objects
    return render(request, 'products/GoogleMap.html', {'products': products})


def index4(request):
    products = Product.objects
    return render(request, 'products/home.html', {'products': products})


def blog(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/blog.html', {'product': product})


@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))


# @login_required(login_url="/accounts/signup")
def index(request):
    form = CustomerForm()

    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'products/index.html', context)


def index2(request):
    form = PrivateDoctor()

    if request.method == 'POST':
        print(request.POST)
        form = PrivateDoctor(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'products/index2.html', context)
