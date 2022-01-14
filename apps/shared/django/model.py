from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import DateTimeField, Model, BooleanField

from shared.django.queryset import DeleteManager


class BaseModel(Model):
    created_date = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeleteModel(Model):
    is_delete = BooleanField(default=False)

    objects = DeleteManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.is_delete = True
        self.save()
