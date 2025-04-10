from rest_framework.views import APIView
from rest_framework import status
from music.models import Album
from music.serializers.album_serializers import AlbumSerializers
from rest_framework.response import Response

# Create your views here.
class AlbumListView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializers(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
