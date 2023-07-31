from django.urls import path
from . import views
app_name='webapp'
urlpatterns =[
    path('',views.mywebapp,name='mywebapp'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.add_movie,name='add_movie'),
    path('edit/<int:id>/',views.updatemovie,name='updatemovie'),
    path('delete/<int:id>/',views.delete,name='delete')
]