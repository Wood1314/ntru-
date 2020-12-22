from django.urls import path

from . import views

urlpatterns = [
    # path('base/', views.base, name='base'),
    # path('hexAscii/', views.hexAscii, name='hexAscii'),
    # path('urlCode/', views.urlCode, name='urlCode'),
    # path('morse/', views.morse, name='morse'),
    # path('morseTable/', views.morseTable, name='morseTable'),
    # path('tuoyuan/', views.tuoyuan, name='tuoyuan'),
    path('ntru/', views.ntru, name='ntru'),
    path('gen/', views.gen, name='gen'),
]