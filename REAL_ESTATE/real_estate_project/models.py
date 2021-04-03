# from importlib._common import _

from django.db import models

# Create your models here.
from django.urls import reverse


class Agjent(models.Model):
    agjent_id =models.AutoField(primary_key=True)
    name_surname = models.CharField(max_length=50)
    foto_agjent = models.ImageField(null=True ,blank=True)
    tel_1_agjent = models.IntegerField()
    tel_2_agjent = models.IntegerField()
    email_agjent = models.EmailField(max_length=30)
    adresa_agjent = models.CharField(max_length=100)
    shitjet = models.IntegerField()
    eksperienca = models.IntegerField()
    agjent_pershkrimi = models.CharField(max_length=250)

    def __str__(self):  #jep emrin
        return str(self.agjent_id)

    @property
    def imageURL(self):
        try:
           url = self.foto_agjent.url
        except:
           url = ''
        return url

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):  #jep emrin
        return str(self.name)



class Pronat(models.Model):
    PARKING = (
        ('po', ('Po')),
        ('jo', ('Jo')),
    )

    NEGOCIMI = [
        ('I diskutueshem', ('I Diskutueshem')),
        ('I padiskutueshem', ('I Padiskutueshem')),
    ]

    TIPI = [
        ('qera', ('Qera')),
        ('shitje', ('Shitje')),
    ]

    # KATEGORIA = (('apartamente', 'toka', 'shtepi', 'vila', 'zyra', 'hapesira biznesi'))
    # KATEGORIA = [
    #     ('apartament', ('Apartamente')),
    #     ('toke', ('Toka')),
    #     ('shtepi', ('Shtepi')),
    #     ('vile', ('Vila')),
    #     ('zyre', ('Zyra')),
    #     ('hapesira biznesi', ('Hapesira Biznesi')),
    # ]

    id_prones = models.AutoField(primary_key=True)
    kodi_prones = models.CharField(max_length=50)
    cmimi = models.IntegerField()
    vendndodhja = models.CharField(max_length=50)
    pershkrim_prones = models.CharField(max_length=250)
    # foto_prones = models.ImageField(null=True, blank=True)
    foto_prones = models.ImageField(null=True, blank=True, upload_to='static/images')
    siperfaqa = models.IntegerField()
    nrdhoma = models.IntegerField()
    nrtualete = models.IntegerField()
    kati = models.IntegerField()
    parking = models.CharField(max_length=2, choices=PARKING)
    negocimi = models.CharField(max_length=30, choices=NEGOCIMI, null=True, blank=True)
    tipi = models.CharField(max_length=30, choices=TIPI)
    # kategoria = models.CharField(max_length=30, choices=KATEGORIA)
    agjent = models.ForeignKey(Agjent, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('real_estate_project:prona', args=[self.id_prones])

    def __str__(self):
        return str(self.kodi_prones)


    @property
    def imageURL(self):
        try:
            url = self.foto_prones.url
        except:
            url = ''
        return url


class ImazheProna(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_src = models.ImageField(null=True, blank=True)
    image_keywords = models.CharField(max_length=100)
    prona_title = models.ForeignKey(Pronat, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.image_id)

    @property
    def imageURL(self):
        try:
            url = self.image_src.url
        except:
            url = ''
        return url


class Testimonials(models.Model):
    id_testimonials = models.ImageField(null=True ,blank=True)
    testimonials_pershkrim = models.CharField(max_length=250)
    testimonials_vleresim = models.TextField(max_length=250)
    testimonials_foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.testimonials_foto)

    @property
    def imageURL(self):
        try:
            url = self.testimonials_foto.url
        except:
            url = ''
        return url

