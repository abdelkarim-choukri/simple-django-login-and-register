from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def profile(request):
    return render(request, "app_auth/profile.html")


