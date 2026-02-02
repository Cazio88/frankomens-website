from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
# Create your views here.

# core/views.py

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message_text = request.POST.get("message")

        # Save message in DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")  # make sure this is your contact page url name

    return render(request, "contact.html")