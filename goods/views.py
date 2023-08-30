
from django.shortcuts import render, get_object_or_404
from .models import TV, simCard
from django.http import JsonResponse

# Create your views here.

def all(request):
    result=[]
    alle=TV.objects.all()
    for i in alle:
        result.append({
            'name':i.name,
            'count':i.SN
        })
    return JsonResponse(result, safe=False)
    


def detail(request, myid):
    each = get_object_or_404(simCard, id=myid)
    data={'Company_name':each.comName, 'Phone_number':each.number}
    return JsonResponse(data, safe=False)
        
