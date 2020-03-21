from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views import View

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tour/index.html', context={ 

            }
        )
        
class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tour/departure.html', context={    

            }
        )

class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tour/tour.html', context={   
                             
            }
        )