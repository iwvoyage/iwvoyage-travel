from django.shortcuts import render
from .models import Process

def process_view(request):
    process = Process.objects.last()  # Get the most recent Process
    return render(request, 'process/process.html', {'process': process})
