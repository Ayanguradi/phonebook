import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'local_shops.settings')

import django
django.setup()

from shops.models import Category, Subcategory

# Create categories first
categories = {
    'restaurants': '<i class="fas fa-utensils"></i>',
    'education': '<i class="fas fa-graduation-cap"></i>',
    'food': '<i class="fas fa-apple-alt"></i>',
    'groceries': '<i class="fas fa-shopping-cart"></i>',
    'clothing': '<i class="fas fa-tshirt"></i>',
    'electronics': '<i class="fas fa-laptop"></i>',
    'beauty': '<i class="fas fa-spa"></i>',
    'sports': '<i class="fas fa-football-ball"></i>',
    'health': '<i class="fas fa-heartbeat"></i>',
    'entertainment': '<i class="fas fa-film"></i>',
}

for name, icon in categories.items():
    Category.objects.create(name=name, icon=icon)

# Create subcategories
subcategories = {
    'restaurants': ['Fast Food', 'Fine Dining', 'Cafes'],
    'education': ['Schools', 'Colleges', 'Training Centers'],
    'food': ['Supermarkets', 'Organic Food', 'Bakery'],
    'groceries': ['General Stores', 'Fruit Shops', 'Vegetable Shops'],
    'clothing': ['Men', 'Women', 'Kids'],
    'electronics': ['Mobiles', 'Laptops', 'Home Appliances'],
    'beauty': ['Salons', 'Spas', 'Cosmetics'],
    'sports': ['Gyms', 'Sports Equipment', 'Yoga'],
    'health': ['Pharmacies', 'Clinics', 'Hospitals'],
    'entertainment': ['Cinemas', 'Gaming', 'Parks'],
}

for category_name, subcategory_names in subcategories.items():
    category = Category.objects.get(name=category_name)
    for subcategory_name in subcategory_names:
        Subcategory.objects.create(category=category, name=subcategory_name)
