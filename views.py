from django.shortcuts import render
from items.models import *

def dashboard(request):

    items = Item.objects.all()

    return render(
        request,
        'dashboard.html',
        {'items':items}
    )