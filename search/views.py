from api.models import Member
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET'])
def search(request):
    phone = request.GET.get('phone')
    user_name = request.GET.get('username')

    if phone is not None:
        user = Member.objects.filter(phone=phone)
        result = []
        for u in user:
            result.append({
                "serial_number": u.serial_number,
                "card_number": u.card_number,
                "username": u.username,
                "gender": u.gender,
                "phone": u.phone,
                "address": u.address,
                "points": u.points,
                "created_at": u.created_at,
                })
        return JsonResponse(result, safe=False, status=200)
    elif user_name is not None:
        print(user_name)
        user = Member.objects.filter(username=user_name)
        result = []
        for u in user:
            print(user)
            result.append({
                "serial_number": u.serial_number,
                "card_number": u.card_number,
                "username": u.username,
                "gender": u.gender,
                "phone": u.phone,
                "address": u.address,
                "points": u.points,
                "created_at": u.created_at,
                })
        return JsonResponse(result, safe=False, status=200)
    
    return Response(JsonResponse({}), status=status.HTTP_400_BAD_REQUEST)
