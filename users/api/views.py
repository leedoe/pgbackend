from django.contrib.auth import mixins
from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed
from users.views import UserDetailView
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(
        CreateModelMixin,
        RetrieveModelMixin,
        ListModelMixin,
        UpdateModelMixin,
        GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False, methods=["GET"])
    def me(self, request):
        print(request)
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


# class UserDetailView(RetrieveModelMixin, GenericViewSet):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     lookup_field = "username"

#     def retrieve(self, request, *args, **kwargs):
#         if kwargs['username'] != request.user.username:
#             return HttpResponse('Unauthorized', status=401)

#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

