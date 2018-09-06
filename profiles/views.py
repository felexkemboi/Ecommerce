from django.shortcuts import render,redirect
from profiles.models import Album,Song


# Create your views here.
def home(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def albums(request):
	albums = Album.objects.all()
	return render(request,'albums.html',{ 'albums':albums})

def songs(request):
	songs = Song.objects.all()
	return render(request,'songs.html',{ 'songs':songs})



#ndio hii io io view
def addalbum(request):
	return render(request,'addalbum.html')





	

def add(request):
	artist = request.GET['artist']
	album_title = request.GET['album_title']
	genre = request.GET['genre']
	album_logo = request.GET['album_logo']
	album = Album.objects.create(
		artist =artist,
		genre = genre,
		album_logo = album_logo,
		album_title = album_title 
		)
	album.save()
	return redirect('albums')
	#return render(request,'add.html',{'name':artist})




	