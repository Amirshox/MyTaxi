from django.db import models

from shared.django.model import BaseModel


class Order(BaseModel):
    CREATED = 'CREATED'
    CANCELED = 'CANCELED'
    ACCEPTED = 'ACCEPTED'
    FINISHED = 'FINISHED'
    STATUSES = (
        (CREATED, CREATED),
        (CANCELED, CANCELED),
        (ACCEPTED, ACCEPTED),
        (FINISHED, FINISHED),
    )

    client = models.ForeignKey('clients.Client', models.SET_NULL, 'orders', null=True, blank=True)
    driver = models.ForeignKey('drivers.Driver', models.SET_NULL, 'orders', null=True, blank=True)

    status = models.CharField(max_length=8, choices=STATUSES, default=CREATED)

    start_point_lat = models.CharField(max_length=63)
    start_point_long = models.CharField(max_length=63)

    end_point_lat = models.CharField(max_length=63)
    end_point_long = models.CharField(max_length=63)

    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.status
