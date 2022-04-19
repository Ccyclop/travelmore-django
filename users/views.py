from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from users.forms import User_creation_form
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import View
from django.utils.decorators import method_decorator
from django.template.defaultfilters import slugify
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, EmailInput, ClearableFileInput, NumberInput, Textarea, PasswordInput

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

@method_decorator(login_required, name='dispatch')
class user_info_view(View):
    template_name = 'user-info.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        return render(request, self.template_name, {'user': user})

@method_decorator(login_required, name='dispatch')
class user_delete(View):
    template_name = 'delete-user.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        return render(request, self.template_name, {'user': user})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        if request.user == user:
            logout(request)
            user.delete()
            return redirect('travelmore:home')

@method_decorator(login_required, name='dispatch')
class user_modify(View):
    template_name = 'edit-user.html'
    form_class = User_creation_form

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.kwargs['username'])
        form = self.form_class(request.POST, request.FILES, instance=user)
        if request.user == user:
            form.save(True)
            login(request, user)
            return redirect('users:user-info', user.username)
        else:
            raise ValidationError("Form Not Valid")
        