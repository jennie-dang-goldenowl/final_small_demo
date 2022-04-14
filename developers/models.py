from django.db import models

class Dev(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    description = models.TextField("Description")