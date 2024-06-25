from admin_ui.models import Laptop
from rest_framework.serializers import ModelSerializer
from .models import Groceries


class LaptopSerializer(ModelSerializer):
    class Meta:
        model = Laptop
        fields = "__all__"


class GrocerySerializers(ModelSerializer):
    class Meta:
        model = Groceries
        fields = "__all__"

    def create(self, validated_data):
        print("payload", validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("update_payload", validated_data)
        return super().update(instance, validated_data)


class GroceryImageSerializer(ModelSerializer):
    class Meta:
        model = Groceries
        fields = "__all__"

    def create(self, validated_data):
        image = self.context.get("view").request.FILES
        print("image data", image)
        return "the grocery with image creation part in progress"
