from django.urls import path, include
from . import views
from .views import SnippetView, SnippetDetail, AddSnippet

urlpatterns = [
    path('', views.contact, name='home'),
    path('snippet/', AddSnippet.as_view(), name='add-snippet'),
    path('snippet/all', SnippetView.as_view(), name='snippet'),
    path('snippet/all/<int:pk>', SnippetDetail.as_view(), name='snippet-details'),
    path('accounts/', include('django.contrib.auth.urls')),
]
