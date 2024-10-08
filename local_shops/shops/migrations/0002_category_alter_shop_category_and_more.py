# Generated by Django 4.2.13 on 2024-07-06 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.category'),
        ),
    ]
