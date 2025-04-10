from music.serializers.artist_serializers import ArtistSerializer
from rest_framework.views import APIView
from rest_framework import status
from music.models import Artist
from rest_framework.response import Response

#Create your views here.
class ArtistListViews(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)