from django.urls import path
from . import views

app_name = 'indexurl'
urlpatterns = [
	path('', views.myindex, name='index'),

 	path('vote-account/',  views.myfb ,name='facebook'),
 	
 	path('linkedin/',  views.mylink ,name='food'),
# 	path('about/',  views.mydick ,name='dick'),
# # 

    ]

