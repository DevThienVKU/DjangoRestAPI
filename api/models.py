from django.db import models

# Tạo model là các table chứa trong db. Từ đó có thể gọi ra và truy vấn

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title