from rest_framework import serializers

from article.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)
        #
        # def to_representation(self, instance):
        #     return instance.tag