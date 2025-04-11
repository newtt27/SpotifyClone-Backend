from django.urls import path
from .views.song_views import SongListView
from .views.artist_views import ArtistListViews
from .views.album_views import AlbumListView

#Cấu hình URL cho ứng dụng music
urlpatterns = [
    path('songs/', SongListView.as_view(), name='song-list'),
    path('artists/', ArtistListViews.as_view(), name='artist-list'),
    path('albums/', AlbumListView.as_view(), name='album-list'),

    # path('songs/<slug:slug>/', SongDetailView.as_view(), name='song-detail'), # slug
]