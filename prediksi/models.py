from django.db import models

class PermintaanIkan(models.Model):
    tanggal = models.DateField()
    jumlah = models.IntegerField()

    def __str__(self):
        return f"{self.tanggal} - {self.jumlah}"

