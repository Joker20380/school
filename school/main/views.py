from django.contrib.auth.models import User
from django.views.generic import ListView




class Index(ListView):
    queryset = User.objects.all()
    template_name = "school/index.html"
    model = User
    paginate_by = 5
