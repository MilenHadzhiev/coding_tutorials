from django.shortcuts import render, redirect


def homepage(request):
    if request.user.is_authenticated:
        return redirect('current user profile')
    else:
        return render(request, 'index.html')
