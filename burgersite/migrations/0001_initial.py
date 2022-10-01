# Generated by Django 4.1.1 on 2022-10-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('type', models.CharField(choices=[('BRK', 'Завтрак'), ('LUN', 'Обед'), ('DIN', 'Ужин')], default='BRK', max_length=3, verbose_name='Тип')),
            ],
        ),
    ]
