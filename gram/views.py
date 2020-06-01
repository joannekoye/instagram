from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Image, Comment, Profile, Likes
# from .forms import 
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required

def index(request):
    '''
    view function to display landing page
    '''

    return render(request, 'index.html')
