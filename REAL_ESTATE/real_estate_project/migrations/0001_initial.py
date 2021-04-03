# Generated by Django 3.1.7 on 2021-03-26 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agjent',
            fields=[
                ('agjent_id', models.AutoField(primary_key=True, serialize=False)),
                ('name_surname', models.CharField(max_length=50)),
                ('foto_agjent', models.ImageField(blank=True, null=True, upload_to='')),
                ('tel_1_agjent', models.IntegerField()),
                ('tel_2_agjent', models.IntegerField()),
                ('email_agjent', models.EmailField(max_length=30)),
                ('adresa_agjent', models.CharField(max_length=100)),
                ('shitjet', models.IntegerField()),
                ('eksperienca', models.IntegerField()),
                ('agjent_pershkrimi', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_testimonials', models.ImageField(blank=True, null=True, upload_to='')),
                ('testimonials_pershkrim', models.CharField(max_length=250)),
                ('testimonials_vleresim', models.CharField(max_length=10)),
                ('testimonials_foto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pronat',
            fields=[
                ('id_prones', models.AutoField(primary_key=True, serialize=False)),
                ('kodi_prones', models.CharField(max_length=50)),
                ('cmimi', models.IntegerField()),
                ('vendndodhja', models.CharField(max_length=50)),
                ('pershkrim_prones', models.CharField(max_length=250)),
                ('foto_prones', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('siperfaqa', models.IntegerField()),
                ('nrdhoma', models.IntegerField()),
                ('nrtualete', models.IntegerField()),
                ('kati', models.IntegerField()),
                ('parking', models.CharField(choices=[('po', 'Po'), ('jo', 'Jo')], max_length=2)),
                ('negocimi', models.CharField(blank=True, choices=[('I diskutueshem', 'I Diskutueshem'), ('I padiskutueshem', 'I Padiskutueshem')], max_length=30, null=True)),
                ('tipi', models.CharField(choices=[('qera', 'Qera'), ('shitje', 'Shitje')], max_length=30)),
                ('agjent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='real_estate_project.agjent')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='real_estate_project.category')),
            ],
        ),
        migrations.CreateModel(
            name='ImazheProna',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_src', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_keywords', models.CharField(max_length=100)),
                ('prona_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='real_estate_project.pronat')),
            ],
        ),
    ]