import django_filters

from REAL_ESTATE.real_estate_project.models import Pronat


class PronatFilter (django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='prona')

    class Meta:
        model = Pronat
        fields = ['KATEGORIA', 'vendndodhja']