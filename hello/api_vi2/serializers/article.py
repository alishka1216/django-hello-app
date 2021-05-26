from rest_framework import serializers

from article.models import Article
from api_vi2.serializers import UserSerializer
from api_vi2.serializers import TagSerializer


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'author', 'created_at', 'tags')
        read_only_fields = ('id','author')
        # extra_kwargs = {
        #     'author': {
        #         'required': True
        #     }
        # }

    def validate_title(self, value):
        min_lenght = 6
        if len(value) < min_lenght:
            raise serializers.ValidationError(f'длинна заголовка должна быть больше {min_lenght} символов')

        return value

