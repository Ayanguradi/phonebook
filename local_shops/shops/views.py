

from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory, Shop, ShopImage, CarouselImage
# views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.shortcuts import render
from .forms import ShopForm,ShopImageForm
from django.http import JsonResponse


def get_subcategories(request, category_id):
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse({'subcategories': list(subcategories)})

#search
def search(request):
    query = request.GET.get('q')
    if query:
        shops = Shop.objects.filter(name__icontains=query)
        categories = Category.objects.filter(name__icontains=query)
        subcategories = Subcategory.objects.filter(name__icontains=query)
    else:
        shops = []
        categories = []
        subcategories = []

    context = {
        'query': query,
        'shops': shops,
        'categories': categories,
        'subcategories': subcategories
    }
    return render(request, 'shops/search_results.html', context)

# ------create shop images
def create_shop(request):
    if request.method == 'POST':
        shop_form = ShopForm(request.POST)
        if shop_form.is_valid():
            shop = shop_form.save()
            for image in request.FILES.getlist('images'):
                ShopImage.objects.create(shop=shop, image=image)
            return redirect('home')  # Redirect to a success page

    else:
        shop_form = ShopForm()

    return render(request, 'shops/create_shop.html', {
        'shop_form': shop_form,
    })

def register_view(request):
    context = {
        'signup_form': UserCreationForm(),
        'login_form': AuthenticationForm(),
        'active_form': 'signup'
    }

    if request.method == 'POST':
        if 'signup' in request.POST:
            signup_form = UserCreationForm(request.POST)
            context['signup_form'] = signup_form
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                password = signup_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                context['active_form'] = 'signup'
        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            context['login_form'] = login_form
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
            else:
                context['active_form'] = 'login'
    return render(request, 'shops/register.html', context)



def home(request):
    shops = Shop.objects.all()
    categories = Category.objects.all()
    carousel_images = CarouselImage.objects.all()
    return render(request, 'shops/home.html', {'shops': shops, 'categories': categories,  'carousel_images': carousel_images})

def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shops/shop_detail.html', {'shop': shop})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shops/category_list.html', {'categories': categories})

def subcategory_shops(request, category_id, subcategory_id):
    category = get_object_or_404(Category, id=category_id)
    subcategory = get_object_or_404(subcategory, id=subcategory_id)
    subcategories = subcategory.objects.filter(category=category)
    shops = Shop.objects.filter(category=category, subcategory=subcategory)
    return render(request, 'shops/subcategory_shops.html', {
        'category': category,
        'subcategory': subcategory,
        'subcategories': subcategories,
        'shops': shops
    })

def shop_all_images(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    images = shop.images.all()  # Fetch all related images for the shop
    return render(request, 'shops/shop_all_images.html', {'shop': shop, 'images': images})



# changes 
def category_shops(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = Subcategory.objects.filter(category=category)
    selected_subcategory_id = request.GET.get('subcategory_id')
    
    if selected_subcategory_id:
        subcategory = get_object_or_404(Subcategory, id=selected_subcategory_id)
        shops = Shop.objects.filter(category=category, subcategory=subcategory)
    else:
        # If no subcategory is selected, show all shops under the category
        shops = Shop.objects.filter(category=category)

    return render(request, 'shops/category_shops.html', {
        'category': category,
        'subcategories': subcategories,
        'shops': shops,
        'selected_subcategory_id': selected_subcategory_id,
    })