from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import ContentsSerializers
from api.services import path_exists, get_contents_from_path
from service_meta.config import path


class MetaViewSet(viewsets.ViewSet):
    def list(self, request):
        if path_exists(path):
            contents = get_contents_from_path(path)
            serializer = ContentsSerializers(contents)
            return Response(serializer.data)
        return Response({"error: Указанный путь не существует"})
