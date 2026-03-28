from django.db import models
from django.db.models.query import Q


class JobOpeningManager(
    models.Manager
):

    def search(self , query : str):
        return self.filter(
            Q(title__icontains = query) | Q(description__icontains = query)
        )
