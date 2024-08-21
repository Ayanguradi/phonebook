# Generated by Django 5.0.6 on 2024-07-05 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('restaurants', 'Restaurants'), ('education', 'Education'), ('food', 'Food'), ('groceries', 'Groceries'), ('clothing', 'Clothing'), ('electronics', 'Electronics'), ('beauty', 'Beauty & Wellness'), ('sports', 'Sports & Fitness'), ('health', 'Health & Medical'), ('entertainment', 'Entertainment')], max_length=50)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('category', models.CharField(choices=[('restaurants', 'Restaurants'), ('education', 'Education'), ('food', 'Food'), ('groceries', 'Groceries'), ('clothing', 'Clothing'), ('electronics', 'Electronics'), ('beauty', 'Beauty & Wellness'), ('sports', 'Sports & Fitness'), ('health', 'Health & Medical'), ('entertainment', 'Entertainment')], max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('opening_hours', models.CharField(blank=True, max_length=255, null=True)),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shops.subcategory')),
            ],
        ),
    ]
