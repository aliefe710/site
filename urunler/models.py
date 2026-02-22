from django.db import models
from django.utils import timezone


# Create your models here.
class Urunler(models.Model):
    urun_adi = models.CharField(max_length=500)
    urun_marka = models.CharField(max_length=500)
    urun_enerji_sinifi = models.CharField(max_length=10)
    urun_fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    urun_resim = models.ImageField(upload_to='urun_resimleri/')
    urun_aciklama = models.TextField(default="Telefonla ulasinabilir.")
    urun_yayinlanma_tarihi = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.urun_adi