from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def home_page_view(request):
    context={"inventory_list":["Widget 1","Widget 2","Wdiget 3"],
    "greeting":"THanK you FOR visitiNG.",}
    return render(request,"home.html",context)

# Below we have a class based view

class AboutPageView(TemplateView):
    template_name="about.html"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["contact_address"]="Gurugram main Street"
        context["phone_number"]="555-555-5555"
        return context