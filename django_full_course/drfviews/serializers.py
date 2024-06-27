from admin_ui.models import Laptop
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Groceries, Images


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


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class GroceryImageSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, obj):
        image_data = Images.objects.filter(id=obj.id)
        result = ImageSerializer(image_data, many=True).data
        return result

    class Meta:
        model = Groceries
        fields = "__all__"

    def create(self, validated_data):
        print("payload", validated_data)
        images = self.context.get("view").request.FILES

        grocery_instance = Groceries.objects.create(
            name=validated_data["name"],
            price=validated_data["price"],
            rating=validated_data["rating"],
            review=validated_data["review"],
        )
        for image in images.getlist("image"):
            print("image_name", image.name)
            Images.objects.create(grocery_image=image, grocery_id=grocery_instance)
        return grocery_instance
