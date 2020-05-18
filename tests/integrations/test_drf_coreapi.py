# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet

from test_project.one_to_one.models import Restaurant
from url_filter.filtersets import ModelFilterSet
from url_filter.integrations.drf_coreapi import CoreAPIURLFilterBackend


class TestCoreAPIURLFilterBackend(object):
    def test_get_schema_fields(self):
        class FilterSet(ModelFilterSet):
            class Meta(object):
                model = Restaurant
                extra_kwargs = {"place": {"id": {"no_lookup": True}}}

        class ViewSet(ModelViewSet):
            model = Restaurant
            queryset = Restaurant.objects
            filter_backend = CoreAPIURLFilterBackend
            filter_class = FilterSet

        view = ViewSet()
        fields = view.filter_backend().get_schema_fields(view)

        assert set(i.name for i in fields) == {
            "place__address",
            "place__address__contains",
            "place__address__date",
            "place__address__day",
            "place__address__endswith",
            "place__address__exact",
            "place__address__gt",
            "place__address__gte",
            "place__address__hour",
            "place__address__icontains",
            "place__address__iendswith",
            "place__address__iexact",
            "place__address__in",
            "place__address__iregex",
            "place__address__isnull",
            "place__address__istartswith",
            "place__address__lt",
            "place__address__lte",
            "place__address__minute",
            "place__address__month",
            "place__address__range",
            "place__address__regex",
            "place__address__second",
            "place__address__startswith",
            "place__address__week_day",
            "place__address__year",
            "place__id",
            "place__name",
            "place__name__contains",
            "place__name__date",
            "place__name__day",
            "place__name__endswith",
            "place__name__exact",
            "place__name__gt",
            "place__name__gte",
            "place__name__hour",
            "place__name__icontains",
            "place__name__iendswith",
            "place__name__iexact",
            "place__name__in",
            "place__name__iregex",
            "place__name__isnull",
            "place__name__istartswith",
            "place__name__lt",
            "place__name__lte",
            "place__name__minute",
            "place__name__month",
            "place__name__range",
            "place__name__regex",
            "place__name__second",
            "place__name__startswith",
            "place__name__week_day",
            "place__name__year",
            "serves_hot_dogs",
            "serves_hot_dogs__contains",
            "serves_hot_dogs__date",
            "serves_hot_dogs__day",
            "serves_hot_dogs__endswith",
            "serves_hot_dogs__exact",
            "serves_hot_dogs__gt",
            "serves_hot_dogs__gte",
            "serves_hot_dogs__hour",
            "serves_hot_dogs__icontains",
            "serves_hot_dogs__iendswith",
            "serves_hot_dogs__iexact",
            "serves_hot_dogs__in",
            "serves_hot_dogs__iregex",
            "serves_hot_dogs__isnull",
            "serves_hot_dogs__istartswith",
            "serves_hot_dogs__lt",
            "serves_hot_dogs__lte",
            "serves_hot_dogs__minute",
            "serves_hot_dogs__month",
            "serves_hot_dogs__range",
            "serves_hot_dogs__regex",
            "serves_hot_dogs__second",
            "serves_hot_dogs__startswith",
            "serves_hot_dogs__week_day",
            "serves_hot_dogs__year",
            "serves_pizza",
            "serves_pizza__contains",
            "serves_pizza__date",
            "serves_pizza__day",
            "serves_pizza__endswith",
            "serves_pizza__exact",
            "serves_pizza__gt",
            "serves_pizza__gte",
            "serves_pizza__hour",
            "serves_pizza__icontains",
            "serves_pizza__iendswith",
            "serves_pizza__iexact",
            "serves_pizza__in",
            "serves_pizza__iregex",
            "serves_pizza__isnull",
            "serves_pizza__istartswith",
            "serves_pizza__lt",
            "serves_pizza__lte",
            "serves_pizza__minute",
            "serves_pizza__month",
            "serves_pizza__range",
            "serves_pizza__regex",
            "serves_pizza__second",
            "serves_pizza__startswith",
            "serves_pizza__week_day",
            "serves_pizza__year",
            "waiter__id",
            "waiter__id__contains",
            "waiter__id__date",
            "waiter__id__day",
            "waiter__id__endswith",
            "waiter__id__exact",
            "waiter__id__gt",
            "waiter__id__gte",
            "waiter__id__hour",
            "waiter__id__icontains",
            "waiter__id__iendswith",
            "waiter__id__iexact",
            "waiter__id__in",
            "waiter__id__iregex",
            "waiter__id__isnull",
            "waiter__id__istartswith",
            "waiter__id__lt",
            "waiter__id__lte",
            "waiter__id__minute",
            "waiter__id__month",
            "waiter__id__range",
            "waiter__id__regex",
            "waiter__id__second",
            "waiter__id__startswith",
            "waiter__id__week_day",
            "waiter__id__year",
            "waiter__name",
            "waiter__name__contains",
            "waiter__name__date",
            "waiter__name__day",
            "waiter__name__endswith",
            "waiter__name__exact",
            "waiter__name__gt",
            "waiter__name__gte",
            "waiter__name__hour",
            "waiter__name__icontains",
            "waiter__name__iendswith",
            "waiter__name__iexact",
            "waiter__name__in",
            "waiter__name__iregex",
            "waiter__name__isnull",
            "waiter__name__istartswith",
            "waiter__name__lt",
            "waiter__name__lte",
            "waiter__name__minute",
            "waiter__name__month",
            "waiter__name__range",
            "waiter__name__regex",
            "waiter__name__second",
            "waiter__name__startswith",
            "waiter__name__week_day",
            "waiter__name__year",
        }
