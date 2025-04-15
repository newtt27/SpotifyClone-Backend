from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from music.models import Favorite, Song  # Import các model
from music.serializers.song_serializers import SongSerializer  # Import đúng serializer

