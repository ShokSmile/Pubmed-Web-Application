from django.urls import path
from .views import journal_list, journal_page, author_page




urlpatterns = [
    path('', journal_list, name='journal_list'),
    path('journal/<str:journal_title>/', journal_page, name='journal_page'),
    path('author/<str:author_name>/', author_page, name='author_page')
]