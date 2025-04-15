from rest_framework.views import APIView
from rest_framework import status
from music.models import Album
from music.serializers.album_serializers import AlbumSerializers
from rest_framework.response import Response
from users.models import User
from users.serializers.users_serializers import User_Serializers
from music.models import Song
from music.serializers.song_serializers import SongSerializer
from music.models import Artist
from music.serializers.artist_serializers import ArtistSerializer

# Create your views here.
class AlbumListView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializers(albums, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateAlbum(APIView):
    def post(self, request):
        name = request.data.get('name')
        artist_id = request.data.get('artist')
        user_id = request.data.get('created_by')
        songs_id = request.data.get('songs', [])
        cover_image = request.FILES.get('cover_image')  # nếu có gửi ảnh

        try:
            artist = Artist.objects.get(id=artist_id)
            creator = User.objects.get(id=user_id)

            album = Album.objects.create(
                name=name,
                artist=artist,
                created_by=creator,
                cover_image=cover_image
            )

            songs = Song.objects.filter(id__in=songs_id)
            for song in songs:
                album.songs.add(song)  # nếu Album có ManyToMany với Song

            album.save()
            serializer = AlbumSerializers(album)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Artist.DoesNotExist:
            return Response({"detail": "Artist not found."}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        except Song.DoesNotExist:
            return Response({"detail": "One or more songs not found."}, status=status.HTTP_404_NOT_FOUND)


      