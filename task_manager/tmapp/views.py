from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tmapp.models import UserTask
from tmapp.serializers import UserTaskSerializer


class UserTaskViewSet(ModelViewSet):
    queryset = UserTask.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserTaskSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['status', 'deadline']
    ordering_fields = ['status', 'deadline']

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset

