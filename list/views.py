from django.shortcuts import render
from .models import list_krsteni
from .forms import list_krsteniForm

# Create your views here.
def index(request):
    rubrike = list_krsteni.objects.all()
    return render(request, 'list/index.html', {'rubrike':rubrike})
