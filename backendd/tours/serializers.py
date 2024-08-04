from rest_framework import serializers
from .models import Tour, Hashtag

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['id', 'name']

class TourSerializer(serializers.ModelSerializer):
    hashtags = HashtagSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = ['id', 'image', 'header', 'content', 'hashtags']

    # custom, makes sure that names are sent to the frontend instead of ids(default)
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['hashtags'] = [hashtag.name for hashtag in instance.hashtags.all()]
        return ret
    # the default representation of a ManyToMany field would be a list of IDs
    # isnt useful on the frontend when i need names of the hashtags

    # The to_representation method in Django’s serializers is used to customize the way data is serialized before it is sent to the frontend. By default, the to_representation method provided by ModelSerializer would convert the related fields to their primary key representation or other default representations.