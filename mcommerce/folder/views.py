from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, mixins,viewsets

from .serializers import FolderSerializer
from .models import Folder

@permission_classes([IsAuthenticated])
class get_all_folders(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer