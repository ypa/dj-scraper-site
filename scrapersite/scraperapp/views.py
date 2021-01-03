from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def scrape(request):
    requests.get('https://wwww.google.com')
    soup = BeautifulSoup(page.text, 'html.parser')

    link_addresses = [link.get('href') for link in soup.find_all('a')]

    return render(request, 'scraperapp/result.html',
                  {'link_addresses': link_addresses})

