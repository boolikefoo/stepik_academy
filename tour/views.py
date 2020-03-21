from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views import View

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tour/index.html'
        )
        
class DepartureView(View):
    def get(self, request, departure=1):
        return render(
            request, 'tour/departure.html'
        )

class TourView(View):
    def get(self, request, id=1):
        return render(
            request, 'tour/tour.html'
        )