from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from tutorials.forms import TutorialCreateForm
from tutorials.models import Tutorial


@login_required
def tutorial_create(request):
    if request.method == 'GET':
        context = {
            'form': TutorialCreateForm,
        }
        return render(request, 'tutorials/create_tutorial.html', context)
    else:
        form = TutorialCreateForm(request.POST)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.user = request.user
            tutorial.save()
            return redirect('current user tutorials')
        context = {
            'form': form,
        }
        return render(request, 'tutorials/create_tutorial.html', context)


def tutorials_all(request):
    tutorials = Tutorial.objects.all()
    tutorials_count = tutorials.count()
    context = {
        'tutorials': tutorials,
        'tutorials_count': tutorials_count,
        'is_user_tutorials_page': False,
    }
    return render(request, 'tutorials/tutorials_list.html', context)


def tutorials_user(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    tutorials_count = user.tutorial_set.all().count()
    tutorials = user.tutorial_set.all()
    context = {
        'user': user,
        'tutorials': tutorials,
        'tutorials_count': tutorials_count,
        'has_create_link': pk is None,
        'is_user_tutorials_page': True,
    }
    return render(request, 'tutorials/tutorials_list.html', context)


@login_required
def tutorial_page(request, pk):
    tutorial = Tutorial.objects.get(pk=pk)
    context = {
        'tutorial': tutorial,
        'can_change': request.user == tutorial.user,
    }
    return render(request, 'tutorials/tutorial_page.html', context)


@login_required
def tutorial_edit(request, pk):
    tutorial = Tutorial.objects.get(pk=pk)
    if request.method == 'GET':
        initial = {
            'tutorial_name': tutorial.tutorial_name,
            'description': tutorial.description,
            'video_url': tutorial.video_url,
            'links_to_documentation': tutorial.links_to_documentation,
        }
        context = {
            'tutorial': tutorial,
            'form': TutorialCreateForm(initial=initial)
        }
        return render(request, 'tutorials/tutorial_edit.html', context)
    else:
        form = TutorialCreateForm(request.POST, instance=tutorial)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.save()
            return tutorial_page(request, pk)
        context = {
            'tutorial': tutorial,
            'form': form,
        }
        return render(request, 'tutorials/tutorial_edit.html', context)


@login_required
def tutorial_delete(request, pk):
    tutorial = Tutorial.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'tutorial': tutorial,
        }
        return render(request, 'tutorials/tutorial_delete.html', context)
    tutorial.delete()
    return tutorials_user(request, pk=tutorial.user.id)
