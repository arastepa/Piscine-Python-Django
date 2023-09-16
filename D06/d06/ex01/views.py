
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login as django_login
from .forms import RegistrationForm, LoginForm, TipForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect
from .models import Tip

def home(request):
    return render(request, 'ex01/welcome.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'ex01/reg.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                django_login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'ex01/login.html', {'form': form})


def logout(request):
    django_logout(request)
    return redirect('home')

def profile(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            tip = form.save(commit=False)
            tip.author = request.user
            tip.save()
            messages.success(request, 'Tip created successfully!')
            return redirect('profile')
    else:
        form = TipForm()
    tips = Tip.objects.all().order_by('-date')
    return render(request, 'ex01/profile.html', {'tips': tips, 'form': form})


@login_required
def upvote_tip(request, tip_id):
    tip = Tip.objects.get(pk=tip_id)
    user = request.user

    # Check if the user has already upvoted or downvoted
    if user in tip.downvotes.all():
        tip.downvotes.remove(user)
    tip.upvotes.add(user)

    return JsonResponse({"upvotes": tip.upvotes.count(), "downvotes": tip.downvotes.count()})

@login_required
def downvote_tip(request, tip_id):
    tip = Tip.objects.get(pk=tip_id)
    user = request.user

    # Check if the user has already upvoted or downvoted
    if user in tip.upvotes.all():
        tip.upvotes.remove(user)
    tip.downvotes.add(user)

    return JsonResponse({"upvotes": tip.upvotes.count(), "downvotes": tip.downvotes.count()})

@login_required
def delete_tip(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)

    if request.user == tip.author:
        tip.delete()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "message": "You do not have permission to delete this tip."})