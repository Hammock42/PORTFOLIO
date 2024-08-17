from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from . import forms

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coming_soon(request):
    return render(request, 'coming_soon.html')

def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = [settings.EMAIL_HOST_USER]
            send_mail(subject, message, sender, recipients)
            return redirect('contact')
    else:
        form = forms.ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')


def portfolio(request):
    return render(request, 'portfolio.html')

def resume(request):
    return render(request, 'resume.html')

def skills(request):
    return render(request, 'skills.html')

def testimonials(request):
    return render(request, 'testimonials.html')

