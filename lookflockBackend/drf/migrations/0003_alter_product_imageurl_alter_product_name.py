# Generated by Django 4.2.3 on 2024-05-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0002_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageURL',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]