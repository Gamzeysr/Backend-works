from rest_framework import serializers
from .models import(Artist,Album,Lyric,Song)

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # fields = "__all__"
        fields = ["first_name","last_name"]
    class Meta:
        model = Album
        # fields = "__all__"
        fields = ["artist","name"]
    class Meta:
        model = Lyric
        # fields = "__all__"
        fields = ["title","content"]
    class Meta:
        model = Song
        # fields = "__all__"
        fields = ["name","artist"]