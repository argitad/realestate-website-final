from django.urls import path
from . import views
from .views import SearchResultsView

app_name = 'real_estate_project'

urlpatterns = [
    path('', views.home, name='home'),
    path('listprona/', views.listprona, name='listprona'),
    path('pronat/<category>', views.CatListView.as_view(), name='pronat'),
    path('prona/<id>', views.prona, name='prona'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('About/', views.About, name="about"),
    path('AgjentPershkrim/<id>', views.AgjentPershkrim , name="agjent-pershkrim"),   #vendosim id per te nxjerre agjentin e klikuar
    path('ListaAgjenteve/', views.ListaAgjenteve, name="lista-agjenteve"),
    path('Kontakt/', views.Kontakt, name="kontakt"),
    path('search', views.search, name='search'),
    path('search_results', views.search_results, name='search_results'),
]