from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieform

# Create your views here.
def mywebapp(request):
    movies=movie.objects.all()
    content={
        'movie_list':movies
    }

    return render(request,'index.html',content)

def detail(request,movie_id):
    movieid=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movieid':movieid})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        add_movies=movie(name=name,desc=desc,year=year,img=img)
        add_movies.save()
    return render(request,'add_movie.html')

def updatemovie(request,id):
    editmovie=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=editmovie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':editmovie})

def delete(request,id):
    if request.method=='POST':
        movieid=movie.objects.get(id=id)
        movieid.delete()
        return redirect('/')
    return render(request,'delete.html')

