from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return redirect('RayliApp:inicio')