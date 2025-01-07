from django.urls import path
from news import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsHomeView.as_view(), name='home'),
    path('create/', views.NewsCreateView.as_view(), name='create'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update/', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news-delete')
]
