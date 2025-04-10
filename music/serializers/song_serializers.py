from rest_framework import serializers
from music.models import Song
from music.serializers.artist_serializers import ArtistSerializer

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    
    class Meta:
        model = Song
        fields = '__all__'