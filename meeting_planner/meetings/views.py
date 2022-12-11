from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room

# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})

def room_listing(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/room_listing.html', {'rooms': rooms})