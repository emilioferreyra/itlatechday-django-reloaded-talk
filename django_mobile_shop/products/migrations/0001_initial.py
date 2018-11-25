# Generated by Django 2.0.2 on 2018-02-10 16:31

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Make',
                'verbose_name_plural': 'Makes',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Make')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('reviews', models.PositiveIntegerField(null=True)),
                ('stars', models.PositiveSmallIntegerField(null=True)),
                ('comment', models.TextField(max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('picture', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='product_pictures')),
            ],
            options={
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Make')),
                ('model', smart_selects.db_fields.ChainedForeignKey(chained_field='make', chained_model_field='make', on_delete=django.db.models.deletion.CASCADE, to='products.Model')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Product Feature',
                'verbose_name_plural': 'Product Features',
            },
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='product_pictures')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product')),
            ],
            options={
                'verbose_name': 'Product Picture',
                'verbose_name_plural': 'Product Pictures',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'ProductType',
                'verbose_name_plural': 'ProductTypes',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductType'),
        ),
        migrations.AddField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
        migrations.AddField(
            model_name='make',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.ProductType'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('make', 'model')},
        ),
    ]