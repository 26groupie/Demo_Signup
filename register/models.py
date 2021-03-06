from django.db import models
from django.contrib.auth.models import User
from django_neomodel import DjangoNode
from neomodel import ArrayProperty, StringProperty, IntegerProperty, RelationshipFrom, RelationshipTo, StructuredRel, UniqueIdProperty

class Member(models.Model):
    user = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user

class RUser(DjangoNode):
    uuid = UniqueIdProperty(primary_key=True)
    title = StringProperty()

    # owns = RelationshipTo('TrackGroup', 'OWNS')

    class Meta:
        app_label = 'register'


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=200, null=True)
    artist = models.CharField(max_length=200, null=True)
    genra = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
