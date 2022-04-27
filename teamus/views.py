from django.views import generic
from .form import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect


class Home(generic.TemplateView):
    template_name = 'home.html'


def register_request(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(f'/account/{request.user.username}')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render(request=request, template_name="register.html", context={"form": form})
