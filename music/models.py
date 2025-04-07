from django.db import models
from users.models import User
from django.db import models
# Create your models here.

#Artist model
class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.name

#Artist - Songs relationship - tức là 1 bài hát sẽ có thể có nhiều artist tham gia sáng tác
class ArtistSong(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist.name} - {self.song.title}"


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums_covers/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='albums_created')

    def __str__(self):
        return self.title

# Model for Song
class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)
    duration = models.DurationField()
    file_url = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Playlist thuộc về người dùng
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('playlist', 'song')  # Một bài hát chỉ có thể xuất hiện một lần trong playlist

    def __str__(self):
        return f"{self.song.title} in {self.playlist.title}"

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField(max_length=255)
    thumbnail = models.ImageField(upload_to='video_thumbnails/', null=True, blank=True)
    duration = models.DurationField()  # Thời gian video
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True)  # Video thuộc về nghệ sĩ
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title