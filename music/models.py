from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='artists/', blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name="songs")
    audio_file = models.FileField(upload_to='songs/')
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Album(models.Model):
    name = models.CharField(max_length=255)
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="albums", null=False, default=1)
    cover_image = models.ImageField(upload_to='albums/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} (by {self.created_by.username})"


class AlbumSongs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album_songs")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="album_songs")
    order = models.PositiveIntegerField(default=0)  # Thứ tự bài hát trong album

    class Meta:
        unique_together = ('album', 'song')

    def __str__(self):
        return f"{self.album.name} - {self.song.title}"

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="favorited_by")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')
