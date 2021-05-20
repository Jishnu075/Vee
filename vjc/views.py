from django.shortcuts import render
from .models import Events
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
	
	context = {
		'events': Events.objects.all()
	}


	return render(request, 'vjc/tmp.html', context)


def about(request):
	return render(request, 'vjc/about.html')

def login(request):
	return render(request, 'users/register.html')




class EventListView(ListView):
	model = Events
	template_name = 'vjc/tmp.html'
	context_object_name = 'events'
	ordering = ['-date_posted']

class EventDetailView(DetailView):
	model = Events
	
class EventCreateView(LoginRequiredMixin,CreateView):
	model = Events
	fields = ['title', 'about_event']

	def form_valid(self, form):
		form.instance.organiser = self.request.user
		return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Events
	fields = ['title', 'about_event']

	def form_valid(self, form):
		form.instance.organiser = self.request.user
		return super().form_valid(form)
	
	def test_func(self):
		events = self.get_object()
		if self.request.user == events.organiser:
			return True
		return False

class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Events
	success_url = '/'

	def test_func(self):
		events = self.get_object()
		if self.request.user == events.organiser:
			return True
		return False