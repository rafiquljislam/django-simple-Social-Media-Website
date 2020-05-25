from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

class RegisterView(View):
    def get(self,request):
        form = UserRegisterForm()
        context = {
            'form':form,
        }
        return render(request, 'user/register.html',context)
    def post(self,request):
        data = UserRegisterForm(request.POST)
        if data.is_valid():
            data.save()
            username = data.cleaned_data['username']
            password = data.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('profile')


class ProfielView(LoginRequiredMixin,View):
    def get(self,request):
        form = UserUpdateForm(instance=self.request.user)
        context = {
            'form':form
        }
        return render(request, 'user/profile.html',context)
    def post(self,request):
        data = UserUpdateForm(request.POST ,instance=self.request.user)
        if data.is_valid():
            data.save()
            return redirect('profile')