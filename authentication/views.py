import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully', 'user': {'id': user.id, 'username': user.username}}) #includes user in response in console, also id
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})


@api_view(['GET'])
def user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
