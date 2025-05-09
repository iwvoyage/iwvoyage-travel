# Generated by Django 5.1.6 on 2025-04-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_alter_gallerygrid_stars_1_alter_gallerygrid_stars_10_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('subheader', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(upload_to='banners/')),
                ('link', models.URLField(help_text='Link for the CTA button')),
            ],
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_10',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_11',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_12',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_6',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_7',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_8',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='gallerygrid',
            name='price_9',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
