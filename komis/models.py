from django.db import models
from django.urls import reverse


class Kupujacy(models.Model):
    nazwa = models.CharField(max_length=255)


class Samochod(models.Model):
    marka = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    przebieg = models.IntegerField()
    rok_produkcji = models.IntegerField()
    moc = models.IntegerField()
    pojemnosc = models.FloatField()
    cena = models.IntegerField()
    paliwo = models.CharField(max_length=1, choices=[
        ('b', 'Benzyna'),
        ('d', 'Diesel'),
        ('l', 'LPG'),
    ])
    image = models.ImageField(upload_to='images')

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.marka


class Kupno(models.Model):
    samochod = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    kupujacy = models.ForeignKey(Kupujacy, on_delete=models.CASCADE)



