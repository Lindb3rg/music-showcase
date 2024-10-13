from django.db import models

class Composition(models.Model):
    
    GENRE_CHOICES = [
        ('classical', 'Classical'),
        ('acoustic', 'Acoustic'),
        ('rock', 'Rock'),
        ('pop', 'Pop'),
        ('hip_hop', 'Hip Hop'),
        ('electronic', 'Electronic'),
        ('film_score', 'Film Score'),
        
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='compositions/')
    date_created = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='classical')


    def __str__(self):
        return self.title


class Service(models.Model):
    
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    

    def __str__(self):
        return self.title

