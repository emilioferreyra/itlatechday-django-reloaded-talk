# Generated by Django 2.0.2 on 2018-02-10 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180210_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make',
            name='product_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='products.ProductType'),
        ),
    ]