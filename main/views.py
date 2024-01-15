from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
def main(request):
    return render(request, "main/main.html")


class FindView(APIView):
    template_name = 'main/find_title.html'
    def get(self, request):
        return render(request, self.template_name)