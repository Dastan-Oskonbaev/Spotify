from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.spotify.forms import ProposalForm
from apps.spotify.models import Author


def hello(request):
    return HttpResponse('Hello, world!')


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'spotify/authors_list.html', {'authors': authors})


class AuthorsListView(ListView):
    model = Author
    template_name = 'spotify/authors_list_2.html'
    context_object_name = 'authors'


# def about(request):
#     return render(request, 'about.html')

def album(request):
    return render(request, 'album.html')


def create_proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spotify/authors_list_2.html')
        else:
            return render(request, 'about.html', {'form': form})
    else:
        form = ProposalForm
        return render(request, 'about.html', {'form': form})