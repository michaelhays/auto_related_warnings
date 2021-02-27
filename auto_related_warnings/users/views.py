from auto_related.tracer import Tracer, optimized_queryset_given_trails
from rest_framework import mixins, permissions, viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tracer = Tracer(self.get_serializer())
        traces = tracer.trace()
        select_related, prefetch_related = optimized_queryset_given_trails(traces)

        return User.objects.select_related(*select_related).prefetch_related(
            *prefetch_related
        )
