from django.shortcuts import render
from .models import Events
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from users import *




def home(request):
	
	context = {
		'events': Events.objects.all()
	}
	Events

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
	fields = ['title', 'about_event', 'invite_link', 'event_loc']

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
	success_url = reverse_lazy('web_home')

	def test_func(self):
		events = self.get_object()
		if self.request.user == events.organiser:
			return True
		return False

#rsvp
def send(request, pk):
	subject = "Invitation for  Event"
	from_email = settings.EMAIL_HOST_USER
	to_email = [request.user.email]
	
	contact_msg = "You have been successfully invited to the event!"
	send_mail(subject, contact_msg, from_email, to_email, fail_silently=False)

	# pk_url_kwargs = 'pk'

	# event = Events.objects.filter(pk = pk)
	# print(event.count())

	return HttpResponse("Check your mail!")