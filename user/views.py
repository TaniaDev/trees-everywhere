from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache


@never_cache
def user_login(request):
    if request.method != "POST":
        return redirect("dashboard") if request.user.is_authenticated else render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    if not (user := authenticate(username=username, password=password)):
        return render(request, "login.html", {"error": "Authentication failed: email or password is incorrect."})
    login(request, user)
    return redirect("/")


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        if request.method == "POST" and "logout" in request.POST:
            logout(request)
            return redirect("/")
        return render(request, "index.html")
