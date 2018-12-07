from django.utils.timezone import now
from django.db import models

class SpotifyPlaylist(models.Model):
    name = models.CharField(max_length=50, blank=True, default='Recomendaciones musicales')
    embed_code = models.TextField('Playlist Embed Code')
    date = models.DateField(auto_now=True)

    def  __str__(self):
        return self.name
