from django.db import models


class kategori(models.Model):
    baju = models.CharField(max_length=100)
    kaos = models.CharField(max_length=100)
    kemeja = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.baju}"



class aplikasi_utama(models.Model):
    kategori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    toko = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.toko}"
