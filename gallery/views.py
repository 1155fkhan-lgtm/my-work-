from django.shortcuts import render
from .models import Picture

def picture_list(request):
    pictures = Picture.objects.all()
    return render(request, 'gallery/picture_list.html', {'pictures': pictures})