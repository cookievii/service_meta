from rest_framework import serializers


class MetaSerializer(serializers.Serializer):
    """Сериализация элементов списка метаданных"""

    name = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=7)
    time = serializers.DecimalField(max_digits=13, decimal_places=0)


class ContentsSerializers(serializers.Serializer):
    """Сериализация списка метаданных"""

    data = serializers.ListSerializer(child=MetaSerializer())
