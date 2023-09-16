
from django.shortcuts import render, get_object_or_404
from .models import TV, simCard
from django.http import JsonResponse
from .serializers import simCardSerializer, TVSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

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

# def detail(request, myid):
#     # each = get_object_or_404(simCard, id=myid)
#     # data={'Company_name':each.comName, 'Phone_number':each.number}
#     each = simCard.objects.filter(id=myid)
#     rest=simCardSerializer(each, many=True)
#     return JsonResponse(rest.data, safe=False)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class GetAllFirst(generics.ListAPIView):
    queryset=TV.objects.all()
    serializer_class=TVSerializer

class GetDetailFirst(generics.RetrieveAPIView):
    queryset = TV.objects.all()
    serializer_class=TVSerializer

class PostFirst(generics.CreateAPIView):
    queryset=TV.objects.all()
    serializer_class=TVSerializer

class PatchFirst(generics.UpdateAPIView):
    queryset=TV.objects.all()
    serializer_class=TVSerializer

class DeleteFirst(generics.DestroyAPIView):
    queryset=TV.objects.all()
    serializer_class=TVSerializer

class PostGetFirst(generics.ListCreateAPIView):
    queryset=TV.objects.all()
    serializer_class=TVSerializer

class AllFunctionFirst(generics.RetrieveUpdateDestroyAPIView):
    queryset=TV.objects.all()
    serializer_class=TVSerializer

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class GetAllSecond(generics.ListAPIView):
    queryset=simCard.objects.all()
    serializer_class=simCardSerializer

class GetDetailSecond(generics.RetrieveAPIView):
    queryset = simCard.objects.all()
    serializer_class=simCardSerializer

class PostSecond(generics.CreateAPIView):
    queryset=simCard.objects.all()
    serializer_class=simCardSerializer

class PatchSecond(generics.UpdateAPIView):
    queryset=simCard.objects.all()
    serializer_class=simCardSerializer

class DeleteSecond(generics.DestroyAPIView):
    queryset=simCard.objects.all()
    serializer_class=simCardSerializer

class PostGetSecond(generics.ListCreateAPIView):
    queryset=simCard.objects.all()
    serializer_class=simCardSerializer

class AllFunctionSecond(generics.RetrieveUpdateDestroyAPIView):
    queryset=simCard.objects.all()
    serializer_class=simCardSerializer



# class GetAllFirst(APIView):
#     def get(self, request):
#         all_data=TV.objects.all()
#         serialz=TVSerializer(all_data, many=True)
#         return Response(serialz.data)

# class GetDetailFirst(APIView):
#     def get(self, request, *args, **kwargs):
#         x=get_object_or_404(TV, id=kwargs['forid'])
#         ser=TVSerializer(x)
#         return Response(ser.data)

# class PostFirst(APIView):
#     def post(self, request):
#         ssz=TVSerializer(data=request.data)
#         if ssz.is_valid():
#             ssz.save()
#             return Response(ssz.data)
#         return Response(ssz.errors)

    
# class PatchFirst(APIView):
#     def patch(self, request, *args, **kwargs):
#         x=get_object_or_404(TV, id=kwargs['forid'])
#         ssz=TVSerializer(x, data=request.data, partial=True)
#         if ssz.is_valid():
#             ssz.save()
#             return Response(ssz.data)
#         return Response(ssz.errors)
# class PutFirst(APIView):
#     def put(self, request, *args, **kwargs):
#         x=get_object_or_404(TV, id=kwargs['forid'])
#         ssz=TVSerializer(x, data=request.data, partial=True)
#         if ssz.is_valid():
#             ssz.save()
#             return Response(ssz.data)
#         return Response(ssz.errors)
    
# class DeleteFirst(APIView):
#     def delete(self, request, *args, **kwargs):
#         x=get_object_or_404(TV, id=kwargs['forid'])
#         x.delete()
#         return Response({"msg":"got"})
        
