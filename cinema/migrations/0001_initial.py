# Generated by Django 3.0.8 on 2020-08-03 07:09

import cinema.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaFilmPersonProfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Cinema film person profession',
                'verbose_name_plural': 'Cinema films persons professions',
                'ordering': ['film__title', 'profession', 'cinema_person__user__first_name'],
            },
        ),
        migrations.CreateModel(
            name='CinemaPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('bio', models.TextField(unique=True)),
                ('oscar_awards', models.PositiveSmallIntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_to_cinema_person)),
            ],
            options={
                'ordering': ['user__first_name', 'user__last_name'],
            },
        ),
        migrations.CreateModel(
            name='CinemaProfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64)),
                ('budget', models.PositiveIntegerField(blank=True, null=True)),
                ('usa_gross', models.PositiveIntegerField(default=0)),
                ('world_gross', models.PositiveIntegerField(default=0)),
                ('run_time', models.DurationField()),
                ('description', models.TextField(unique=True)),
                ('release_data', models.DateField()),
                ('oscar_awards', models.PositiveSmallIntegerField(default=0)),
                ('poster', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_to_film)),
                ('country', models.ManyToManyField(to='cinema.Country')),
                ('distributor', models.ManyToManyField(to='cinema.Distributor')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Invalid genre name format.', regex='^[A-Z][a-z]+[-]?[a-z]+$')])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImdbRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=2, unique=True)),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Invalid language name format.', regex='^[A-Z][a-z]+$')])),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MpaaRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=512, unique=True)),
            ],
            options={
                'ordering': ['value'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('price', models.DecimalField(decimal_places=2, error_messages={'min_value': 'Product price cannot be less than 0.99.'}, max_digits=5, validators=[django.core.validators.MinValueValidator(0.99)])),
                ('in_stock', models.PositiveSmallIntegerField(default=0)),
                ('film', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cinema.Film')),
            ],
            options={
                'ordering': ['film__title'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('title', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(unique=True)),
                ('news_source', models.CharField(max_length=32)),
                ('news_author', models.CharField(max_length=64)),
                ('news_feed_photo', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_photo_to_news_feed)),
                ('news_detail_photo', models.ImageField(blank=True, null=True, upload_to=cinema.models.upload_photo_to_news_detail)),
                ('cinema_person', models.ManyToManyField(blank=True, to='cinema.CinemaPerson')),
                ('film', models.ManyToManyField(blank=True, to='cinema.Film')),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='cinema.Genre'),
        ),
        migrations.AddField(
            model_name='film',
            name='imdb_rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.ImdbRating'),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ManyToManyField(to='cinema.Language'),
        ),
        migrations.AddField(
            model_name='film',
            name='mpaa_rating',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cinema.MpaaRating'),
        ),
        migrations.AddField(
            model_name='film',
            name='staff',
            field=models.ManyToManyField(through='cinema.CinemaFilmPersonProfession', to='cinema.CinemaPerson'),
        ),
        migrations.CreateModel(
            name='CommentToProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('author', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Display on screen?')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.Product')),
            ],
            options={
                'verbose_name_plural': 'Comments to products',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CommentToPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('author', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Display on screen?')),
                ('cinema_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.CinemaPerson')),
            ],
            options={
                'verbose_name_plural': 'Comments to persons',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CommentToNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('author', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Display on screen?')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.News')),
            ],
            options={
                'verbose_name_plural': 'Comments to news',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CommentToFilm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('author', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='Display on screen?')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.Film')),
            ],
            options={
                'verbose_name_plural': 'Comments to films',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='cinemaperson',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='cinema.Country'),
        ),
        migrations.AddField(
            model_name='cinemaperson',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cinemafilmpersonprofession',
            name='cinema_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.CinemaPerson'),
        ),
        migrations.AddField(
            model_name='cinemafilmpersonprofession',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.Film'),
        ),
        migrations.AddField(
            model_name='cinemafilmpersonprofession',
            name='profession',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, to='cinema.CinemaProfession'),
        ),
    ]
