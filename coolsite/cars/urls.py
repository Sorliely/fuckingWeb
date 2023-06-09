from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('history/', history, name='history' ),
    path('feedback/', feedback, name='feedback'),
    path('login/', login, name='login'),
    path('logup', logup, name='logup'),
    path('category/<int:cat_id>/', show_category, name='category'),
]
