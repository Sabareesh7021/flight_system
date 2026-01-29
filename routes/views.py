from django.views import View
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, TemplateView)

from .models import AirportRoute
from .forms import AirportRouteForm, SearchRouteForm


class HomeView(TemplateView):
    template_name = 'routes/home.html'

class AirportRouteCreateView(CreateView):
    model = AirportRoute
    form_class = AirportRouteForm
    template_name = 'routes/add_route.html'
    success_url = reverse_lazy('search-route')

class LastReachableNodeView(View):
    template_name = 'routes/search_route.html'

    def get(self, request):
        form = SearchRouteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SearchRouteForm(request.POST)
        last_node = None

        if form.is_valid():
            current = form.cleaned_data['start_airport']
            direction = form.cleaned_data['direction']

            while True:
                next_node = AirportRoute.objects.filter(
                    connected_airport=current,
                    position=direction
                ).first()

                if not next_node:
                    last_node = current
                    break

                current = next_node

        return render(
            request,
            self.template_name,
            {
                'form': form,
                'last_node': last_node
            }
        )


class DurationResultView(TemplateView):
    template_name = 'routes/results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        longest = AirportRoute.objects.order_by('-distance').first()
        shortest = AirportRoute.objects.order_by('distance').first()

        context['longest'] = longest
        context['shortest'] = shortest

        return context
