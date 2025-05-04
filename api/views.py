from api.models import Member, Plan
from api.serializers import MemberSerializer, PlanSerializer
from rest_framework import viewsets


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
