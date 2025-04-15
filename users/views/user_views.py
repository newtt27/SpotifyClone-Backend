from rest_framework.views import APIView
from rest_framework import status
from users.models import User
from users.serializers.users_serializers import User_Serializers
from rest_framework.response import Response
from music.models import Album
from music.serializers.album_serializers import AlbumSerializers



