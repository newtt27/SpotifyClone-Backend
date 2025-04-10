from rest_framework import serializers
from music.models import Album
from .artist_serializers import ArtistSerializer
class AlbumSerializers(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Album
        fields = '__all__' 