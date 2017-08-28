from django.shortcuts import render
from django.views import View

# Create your views here.
class Temp_Home(View):
    def temp(request):
        return render(request, 'temp_home.html')