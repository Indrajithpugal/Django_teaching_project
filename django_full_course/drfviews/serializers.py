from admin_ui.models import Laptop
from rest_framework.serializers import ModelSerializer


class LaptopSerializer(ModelSerializer):
    class Meta:
        model = Laptop
        fields = "__all__"
