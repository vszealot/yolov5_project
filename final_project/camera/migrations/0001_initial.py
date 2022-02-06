# Generated by Django 3.2.5 on 2021-10-13 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodInfo',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=200, unique=True)),
                ('calorie', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MealInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_object_id', models.CharField(max_length=200)),
                ('pub_time', models.CharField(max_length=10)),
                ('pub_date', models.DateField()),
                ('food_name', models.ForeignKey(db_column='food_name', on_delete=django.db.models.deletion.CASCADE, related_name='mealinfo', to='camera.foodinfo', to_field='food_name')),
                ('username', models.ForeignKey(db_column='username', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mealinfo', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]