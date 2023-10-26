from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class BaseModelViewSet(RetrieveModelMixin, ListModelMixin, viewsets.GenericViewSet):
    ...
