from django.shortcuts import render
from .models import FallenSoldier, ArrestedPerson, MissingPerson

def home(request):
    fallen_soldiers = FallenSoldier.objects.all().order_by('-date')
    arrested_people = ArrestedPerson.objects.filter(has_representation=False).order_by('-date')
    # missing_people = MissingPerson.objects.filter(found=False).order_by('-time_of_missing')
    missing_people = MissingPerson.objects.order_by('-time_of_missing')
    
    context = {
        'fallen_soldiers': fallen_soldiers,
        'arrested_people': arrested_people,
        'missing_people': missing_people,
    }
    return render(request, 'listings/home.html', context)