from django.shortcuts import render, get_object_or_404

from events.models import Event


# Create your views here.

def index(request):
    events = Event.objects.all()
    return render(request, "index.html", {"events":events})

def event(request, event_id):
    event = get_object_or_404(Event,pk=event_id)
    context = {"event": event}
    return render(request,"event.html", context)
