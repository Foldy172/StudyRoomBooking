from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'booking/index.html')

def health(request):
    return JsonResponse({'status': 'ok', 'service': 'StudyRoomBooking'})