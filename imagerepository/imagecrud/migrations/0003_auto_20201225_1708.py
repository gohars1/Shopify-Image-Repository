# Generated by Django 3.1.1 on 2020-12-25 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imagecrud', '0002_auto_20201225_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='owned_images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imagecrud.image'),
        ),
    ]
