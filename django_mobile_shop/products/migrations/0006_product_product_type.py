# Generated by Django 2.0.2 on 2018-02-10 18:16

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='model', chained_model_field='model', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductType'),
        ),
    ]
