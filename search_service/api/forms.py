import requests

from django import forms


class SearchEngineForm(forms.Form):
    word = forms.CharField(max_length=100)

    def search(self):
        result = {}
        word = self.cleaned_data['word']
        url = f'http://api.tvmaze.com/search/shows?q={word}'
        response = requests.get(url)
        if response.status_code != 200:
            return False

        result = response.json()

        return result
