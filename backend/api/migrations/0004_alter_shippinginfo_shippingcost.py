# Generated by Django 4.0.4 on 2022-04-30 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_shippinginfo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippinginfo',
            name='shippingCost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
