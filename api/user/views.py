import string
import random
import re
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer


# Signin
@csrf_exempt
def signin(request):
    if request.method != 'POST':
        return JsonResponse({"Error": "Not a valid request"})

    email = request.POST.get('email')
    password = request.POST.get('password')
    # print("Provided ", email, password)

    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email):
        return JsonResponse({'Error': 'Enter a valid email'})
    if len(password) < 3:
        return JsonResponse({'Error': 'Password needs to be at least of 3 char'})

    # Return the User model that is active in this project. Similar as calling CustomUser()
    userModel = get_user_model()

    try:
        # Check if the given Email is present
        user = userModel.objects.get(email=email)
        # Authenticate with provided Email & Password
        if authenticate(email=email, password=password):
            login(request, user)
            return JsonResponse({'Info': 'Logged in successful.', 'UUID': user.user_uuid, 'name': user.name, 'email': user.email, 'gender': user.gender, 'phone': user.phone, 'is_active': user.is_active, 'is_superuser': user.is_superuser})
        else:
            return JsonResponse({"Error": "Wrong Username and Password. Authentication Failed!!!"})
    except userModel.DoesNotExist:
        return JsonResponse({'Error': 'Invalid Email'})


# Sing out
def signout(request, uuid):
    userModel = get_user_model()
    try:
        user = userModel.objects.get(pk=uuid)
        logout(request)
    except userModel.DoesNotExist:
        return JsonResponse({'Error': 'Invalid User ID'})
    else:
        return JsonResponse({"Info": "Successfully Logged Out"})


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
