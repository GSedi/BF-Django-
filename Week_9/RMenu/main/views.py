from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview
from .forms import RestaurantForm
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
    

class IndexView(TemplateView):
    template_name = "index.html"

class RestaurantList(ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    template_name='restaurant/show.html'

@method_decorator(login_required, name='dispatch')
class RestaurantCreateView(CreateView):
    login_required = True
    model = Restaurant
    form_class = RestaurantForm
    template_name = "restaurant/create.html"
    # success_url = '/main/restaurants'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "restaurant/show.html"


@method_decorator(login_required, name='dispatch')
class RestaurantUpdateView(UpdateView):
    login_required = True
    model = Restaurant
    fields = ['name', 'telephone', 'city']
    template_name = "restaurant/update.html"

@method_decorator(login_required, name='dispatch')
class RestaurantDeleteView(DeleteView):
    login_required = True
    model = Restaurant
    template_name = "restaurant/confirm.html"
    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()
    #     return HttpResponseRedirect(self.get_success_url())
    # template_name = "restaurant/confirm.html"
    success_message = "Thing was deleted successfully."
    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)  

    def get_success_url(self):
        return reverse("show_restaurants")


# def index(request):
#     return render(request, "index.html")

# def show_restaurants(request):
#     rest = Restaurant.objects.all()
#     context = {
#         'restaurants': rest
#     }
#     return render(request, "restaurant/show.html", context)

# def add_restaurant(request):
    
#     return


# def update_restaurant(request, id):
#     return

# def delete_restaurant(request, id):
#     return