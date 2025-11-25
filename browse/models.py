from django.db import models

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.CharField(null=True, max_length=25)
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(null=True)
    vote_average = models.FloatField(blank=True)
    language = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    
    

