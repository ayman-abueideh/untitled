from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class Home(APIView):
    def get(self,request):
        return Response({'message':'hello'})

def handler404(request, *args, **argv):
    return redirect('home')


def handler500(request, *args, **argv):
    return redirect('home')
