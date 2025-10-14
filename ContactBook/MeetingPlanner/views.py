from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import PlannerForm
from .models import Planner
from PhoneBook.models import Contact



@require_GET
@login_required
def get_add_form(request: HttpRequest):
    return render(request, "add_meet.html", dict(form=PlannerForm()))


@require_POST
@login_required
def add_planner(request: HttpRequest):
    form = PlannerForm(data=request.POST)
    if form.is_valid():
        planner: Planner = form.save(commit=False)
        planner.user = request.user
        planner.save()
        messages.add_message(request=request, level=messages.SUCCESS, message="Зустріч створена")
        return redirect("planners")
    messages.add_message(request=request, level=messages.ERROR, message="Помилка")
    return render(request, "add_meet.html", dict(form=form))


@require_GET
@login_required
def get_planners(request: HttpRequest):
    planners = Planner.objects.all()
    return render(request, "planners.html", dict(planners=planners))