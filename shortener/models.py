from django.db import models
import random
import string

class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}"


def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
