from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import APIKey, APIUrl
from cryptography.fernet import Fernet
import logging


logger = logging.getLogger(__name__)
# Генерация ключа
key = Fernet.generate_key()
cipher_suite = Fernet(key)


def index(request):
    return render(request, 'mainapp/general_button.html')


def settings_api(request):
    return render(request, 'mainapp/settings_api.html')


def input_api_key(request):
    if request.method == 'POST':
        form = forms.APIKeyForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            description = form.cleaned_data['description']
            key = bytes(form.cleaned_data['key'], 'utf-8')
            encrypted_key = cipher_suite.encrypt(key)
            # decrypted_text = cipher_suite.decrypt(encrypted_pass)
            apykey = APIKey(company=company, description=description, key=encrypted_key)
            apykey.save()
            logger.info(f'APY-key {apykey.description} saved.')
            return HttpResponse(f"АПИ - ключ {apykey.description} успешно сохранен.")
    else:
        form = forms.APIKeyForm()
    return render(request, 'mainapp/input_api_key.html', {'form': form})


def input_api_url(request):
    if request.method == 'POST':
        form = forms.APIUrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            description = form.cleaned_data['description']
            request_ = form.cleaned_data['request']
            validity = form.cleaned_data['validity']
            apyurl = APIUrl(url=url, description=description, request=request_, validity=validity)
            apyurl.save()
            logger.info(f'APY-url {apyurl.description} saved.')
            return HttpResponse(f"АПИ - url {apyurl.description} успешно сохранен.")
    else:
        form = forms.APIUrlForm()
    return render(request, 'mainapp/input_api_url.html', {'form': form})



