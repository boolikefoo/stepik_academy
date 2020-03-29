from django.shortcuts import render
from django.views import View
from tour.data import title, subtitle, description, departures, tours

context = { "title" : title, "subtitle" : subtitle, "description" : description, "departures" : departures, "tours" : tours}

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tour/index.html', context=(context) 
        )        

        
class DepartureView(View):
    def get(self, request, departure, *args, **kwargs):        
        return render(
            request, 'tour/departure.html', context=(context)
        )
    

class TourView(View):
    def get(self, request, id):
        return render(
            request, 'tour/tour.html', context=(context)
        )
