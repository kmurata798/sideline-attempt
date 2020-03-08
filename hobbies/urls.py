from django.urls import path
from .views import HobbiesListView, HobbiesDetailView, HobbiesCreateView, HobbiesUpdateView, HobbiesDeleteView
from . import views

urlpatterns = [
    path('', views.home, name='hobbies-home'),
    path('hobbies/list', HobbiesListView.as_view(), name='hobbies-list'),
    path('hobbies/<int:pk>/', HobbiesDetailView.as_view(), name='hobbies-detail'),
    path('hobbies/new/', HobbiesCreateView.as_view(), name='hobbies-create'),
    path('hobbies/<int:pk>/update/', HobbiesUpdateView.as_view(), name='hobbies-update'),
    path('hobbies/<int:pk>/delete/', HobbiesDeleteView.as_view(), name='hobbies-delete'),
    path('hobbies/about/', views.about, name='hobbies-about'),
    path('hobbies/explore/', views.explore, name='hobbies-explore')
]