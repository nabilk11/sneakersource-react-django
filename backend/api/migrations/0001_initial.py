# Generated by Django 4.0.4 on 2022-04-26 04:48

import api.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('paymentType', models.CharField(blank=True, max_length=200, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shipping', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('totalPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('paymentCompleted', models.BooleanField(default=False)),
                ('paymentTime', models.DateTimeField(blank=True, null=True)),
                ('deliveryTime', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['delivered'],
            },
        ),
        migrations.CreateModel(
            name='ShippingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shippingCost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('address', models.CharField(blank=True, max_length=155, null=True)),
                ('city', models.CharField(blank=True, max_length=155, null=True)),
                ('state', models.CharField(blank=True, max_length=155, null=True)),
                ('zipCode', models.CharField(blank=True, max_length=10, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('shippingDate', models.DateField()),
                ('order', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
            options={
                'ordering': ['shippingDate'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=155, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('color', models.CharField(blank=True, max_length=155, null=True)),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('year', models.PositiveIntegerField(default=2022, validators=[django.core.validators.MinValueValidator(1984), api.models.multi_year_value])),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrderedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('qty', models.IntegerField(blank=True, default=0, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.product')),
            ],
        ),
    ]
