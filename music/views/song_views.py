from rest_framework.views import APIView
from rest_framework import status
from music.models import Song
from music.serializers.song_serializers import SongSerializer
from rest_framework.response import Response
from django.views.generic import DetailView

# Create your views here.
class SongListView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




