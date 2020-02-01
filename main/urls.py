from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from .views import *

app_name = 'main'

urlpatterns = [
    path('', all_items, name = 'all'),
    path('found/', found_items, name = 'found'),
    path('lost/', lost_items, name = 'lost'),
    path('item/<int:pk>', ItemDetail.as_view(), name = 'item'),
    path('add/', SubmitView.as_view(), name = 'add'),
    path('search/', search, name = 'search'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
