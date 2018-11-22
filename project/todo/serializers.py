# todo/urls
from rest_framework.serializers import ModelSerializer
# local  imports
from .models import Todo


class TodoSerializer(ModelSerializer):
    """
    Todo model serializer
    """
    class Meta:
        """
        Meta class for the serializer
        """
        model = Todo
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")

