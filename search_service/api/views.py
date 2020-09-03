from django.shortcuts import render

from .forms import SearchEngineForm


def home(request):
    search_result = {}
    if 'word' in request.GET:
        form = SearchEngineForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = SearchEngineForm()

    return render(
        request, 'home.html', {'form': form, 'search_result': search_result}
    )
