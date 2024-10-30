from rest_framework.serializers import ModelSerializer

from Core.models.About import About


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = ('version', 'upd', 'address', 'info', 'instruction')
