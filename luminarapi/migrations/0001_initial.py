# Generated by Django 4.1.10 on 2023-07-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('offline', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='DemoClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url_link', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('offline_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('online_fees', models.DecimalField(decimal_places=2, max_digits=10)),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('mod1_text', models.TextField()),
                ('mod2_text', models.TextField()),
                ('mod3_text', models.TextField()),
                ('mod4_text', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('online_fees', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('offline_fees', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.CharField(max_length=200)),
                ('batch_code', models.CharField(max_length=50)),
                ('course_name', models.CharField(max_length=255)),
                ('subjects', models.CharField(max_length=200)),
            ],
        ),
    ]