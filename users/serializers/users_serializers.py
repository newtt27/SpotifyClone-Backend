from rest_framework import serializers
from users.models import User
from music.serializers.artist_serializers import ArtistSerializer

class User_Serializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'