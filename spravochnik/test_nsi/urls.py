from django.urls import path

from . import views

urlpatterns = [
    path('api/dictionaries/', views.GetDictionariesInfoView.as_view()),
    path('api/dictionaryitem/', views.GetDictionaryItemInfoView.as_view()),

]