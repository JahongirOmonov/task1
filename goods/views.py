
from django.shortcuts import render, get_object_or_404
from .models import TV, simCard
from django.http import JsonResponse
from .serializers import simCardSerializer, TVSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def all(request):
#     result=[]
#     alle=TV.objects.all()
#     # for i in alle:
#     #     result.append({
#     #         'name':i.name,
#     #         'count':i.SN
#     #     })
#     result=TVSerializer(alle, many=True)
#     return JsonResponse(result.data, safe=False)
class getall(APIView):
    def get(self, request):
        all_data=TV.objects.all()
        serialz=TVSerializer(all_data, many=True)
        return Response(serialz.data)
    


def detail(request, myid):
    # each = get_object_or_404(simCard, id=myid)
    # data={'Company_name':each.comName, 'Phone_number':each.number}
    each = simCard.objects.filter(id=myid)
    rest=simCardSerializer(each, many=True)
    return JsonResponse(rest.data, safe=False)

class postall(APIView):
    def post(self, request):
        user_body=request.data
        ssz=TVSerializer(data=user_body)
        if ssz.is_valid():
            ssz.save()
            return Response(ssz.data)
        return Response(ssz.errors)
        
