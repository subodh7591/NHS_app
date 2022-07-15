from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView


class HomePage(View):

    def get(self, request):
        return HttpResponse("Homepage")

    def post(self, request):
        return HttpResponse("homepage")
