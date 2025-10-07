from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages


from .forms import PlannerForm
from .models import Planner
from PhoneBook.models import Contact



@require_GET
def get_add_form(request: HttpRequest):
    return render(request, "add_meet.html", dict(form=PlannerForm()))