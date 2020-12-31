from url_shortener.forms import ShorteneddURLForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.http.response import JsonResponse
from rest_framework import status
from url_shortener.models import ShorteneddURL
import random
import json


def index(request):
    return render(request, 'url_shortener/index.html')


def create_key():
    l = [str(n) for n in range(0, 10)] + \
        [c for c in 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']
    random.shuffle(l)
    key = ''.join(l[:7])
    return key


@require_POST
def shorten_url(request):
    data = json.loads(request.body.decode('utf-8'))
    url  = data['url']

    try:
        short = ShorteneddURL.objects.get(url=url)
    except ShorteneddURL.DoesNotExist:
        form = ShorteneddURLForm(request.POST)
        if form.is_valid():
            short = form.save()
            return JsonResponse({'key': short.key}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)



@require_GET
def get_url(request, key):
    short = get_object_or_404(ShorteneddURL, key=key)
    url = short.url

    return redirect(url)
