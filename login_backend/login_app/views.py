from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Add your login logic here
        # Query the database to authenticate the user

        if authenticated:
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Login failed'}, status=400)