from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login 


def home(request):
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now)
    past_events = Event.objects.filter(date__lt=now)
    return render(request, 'events/home.html', {
        'upcoming_events': upcoming_events,
        'past_events': past_events
    })

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('home')
        else:
            print("Form Errors:", form.errors)  
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})