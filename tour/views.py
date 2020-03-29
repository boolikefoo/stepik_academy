from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'index.html'
        )

        
class DepartureView(View):
    def get(self, request):
        return render(
            request, 'tour/departure.html'
        )


class TourView(View):
    def get(self, request):
        return render(
            request, 'tour/tour.html'
        )


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'test.html', { 'name' : 'artem', 'place' : 'Lab'})


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {})