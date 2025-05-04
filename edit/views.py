from django.http import JsonResponse
from rest_framework.decorators import api_view
from api.models import Member, Plan
from api.serializers import PlanSerializer
from rest_framework import status
from rest_framework.response import Response
import datetime


@api_view(['POST'])
def modify_plan(request):
    id = request.data['id']
    try:
        new_end = request.data['plan_end']
    except:
        new_end = None
    plan = Plan.objects.get(id=id)
    if new_end is not None:
        new_end = datetime.datetime.strptime(new_end, "%Y-%m-%d").date()
        if new_end <= plan.plan_start:
            return JsonResponse({"status":"error", "message":"方案時間錯誤"})
        plan.plan_end = new_end
        plan.save()
        serializer = PlanSerializer(plan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
