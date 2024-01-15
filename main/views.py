from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse

def main(request):
    return render(request, "main/main.html")


class FindView(APIView):
    template_name = 'main/find_title.html'
    def get(self, request):
        return render(request, self.template_name)
    
    
from django.http import HttpResponse

def health_check(request):
    return HttpResponse(status=200)