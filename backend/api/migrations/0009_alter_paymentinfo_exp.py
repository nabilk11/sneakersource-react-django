# Generated by Django 4.0.4 on 2022-05-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_paymentinfo_pppass_alter_paymentinfo_ppuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='exp',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]