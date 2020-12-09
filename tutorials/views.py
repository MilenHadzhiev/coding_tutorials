from django.shortcuts import render  # , redirect

from tutorials.forms import TutorialCreateForm
from tutorials.models import Tutorial


def tutorial_create(request):
    if request.method == 'GET':
        context = {
            'form': TutorialCreateForm,
        }
        return render(request, 'tutorials/create_tutorial.html', context)
    # else:
    #     form = TutorialCreateForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('current user tutorials')
    #     context = {
    #         'form':form,
    #     }
    #     return render(request, 'tutorials/create_tutorial.html', context)


def tutorials(request, pk=None):
    tutorials = Tutorial.objects.all() if pk is None \
        else Tutorial.objects.get(user=request.user)
    context = {
        'tutorials': tutorials,
    }
    return render(request, 'tutorials/tutorials_list.html', context)
