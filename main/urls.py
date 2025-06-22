from django.urls import path
from .views import IndexView, ListNews, ListGallary, NewsView, GallaryView,accept_murojaat

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('news/', ListNews.as_view(), name='list_news'),
    path('send-murojaat/', accept_murojaat, name='accept-murojaat'),
    path('gallary/', ListGallary.as_view(), name='list_gallary'),
    path('news/<str:slug>/', NewsView.as_view(), name='news_detail'),
    path('gallary/<int:pk>/', GallaryView.as_view(), name='gallary_detail'),
]
