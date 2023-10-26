import django_filters as df
from django.db import models

from drive.bot.const import Language


class NumberArrayExactFilter(df.NumberFilter):
    def filter(self, qs, value):
        if isinstance(value, str):
            value = [value]
        lookup = "%s__%s" % (self.field_name, self.lookup_expr)
        for id_ in value:
            qs = self.get_method(qs)(**{lookup: id_})
        return qs


class NumberArrayInFilter(df.NumberFilter):
    def filter(self, qs, value):
        if isinstance(value, str):
            value = [value]
        return super().filter(qs, value)


class BaseFilterSet(df.FilterSet):
    lang = df.ChoiceFilter(choices=Language.choices)

    def filter_queryset(self, queryset):
        forbidden_keys = ["limit", "offset", "lang"]
        query_params = {}
        if self.form.data:
            query_params = {k: v if len(v) > 1 else v[0] for k, v in self.form.data.lists()}
        for key in forbidden_keys:
            if key in query_params:
                query_params.pop(key)
        for name, value in query_params.items():
            queryset = self.filters[name].filter(queryset, value)
            assert isinstance(
                queryset, models.QuerySet
            ), "Expected '%s.%s' to return a QuerySet, but got a %s instead." % (
                type(self).__name__,
                name,
                type(queryset).__name__,
            )
        return queryset
