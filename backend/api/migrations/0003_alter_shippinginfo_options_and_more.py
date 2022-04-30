# Generated by Django 4.0.4 on 2022-04-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippinginfo',
            options={'ordering': ['createdAt']},
        ),
        migrations.RemoveField(
            model_name='shippinginfo',
            name='shippingDate',
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
