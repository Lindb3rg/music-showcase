from django.db import models

class Composition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='compositions/')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

