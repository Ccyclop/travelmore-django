from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from users.forms import User_creation_form
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import View
from django.utils.decorators import method_decorator
from django.template.defaultfilters import slugify
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

class user_registration_view(View):
    form_class = User_creation_form
    template_name = 'register.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(True)
            return redirect('users:login')
        else:
            raise ValidationError('Form Not Valid')
        return render(request, self.template_name, {'form': form})
# paroli ar ihasheba dasafixia

class login_view(View):
    form_class = AuthenticationForm
    template_name='login.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('travelmore:home')
        return render(request, self.template_name, {'form': form})
