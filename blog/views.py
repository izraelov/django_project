from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.template.loader import get_template
from .forms import ContactForm


def home(request):
    return render(request, 'blog/home.html')


def success(request):
    return HttpResponse('<h1>Success! Thank you for your message.</h1>'
                        '<a href="/" class="btn btn-primary btn-lg active" role="button" aria-pressed="true">Back</a>')

def files(request):
    return render(request, 'blog/files/ITAY_CV.pdf')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            from_email = request.POST.get("from_email")
            to_email = [settings.DEFAULT_FROM_EMAIL]

            # contact_message = "{0}, from {1} with email {2}".format(message, name, email)

            context = {
                'user': name,
                'email': email,
                'subject' : subject,
                'message': message
            }
            contact_message = get_template('contact_message.txt').render(context)
            try:
                send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('blog-success')
    return render(request, "blog/contact.html", {'form': form})


