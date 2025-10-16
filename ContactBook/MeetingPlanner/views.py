from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.decorators.http import require_GET, require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PlannerForm
from .models import Planner
from PhoneBook.models import Contact



@require_GET
@login_required
def get_add_form(request: HttpRequest):
    return render(request, "add_planner.html", dict(form=PlannerForm()))


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
    return render(request, "add_planner.html", dict(form=form))


@require_GET
@login_required
def get_planners(request: HttpRequest):
    planners = Planner.objects.filter(user=request.user).all()
    return render(request, "planners.html", dict(planners=planners))


class PlannerView(ListView):
    def get(self, request: HttpRequest):
        current_page = request.GET.get("page", 1)
        paginator = Paginator(Planner.objects.filter(user=request.user).all(), 2)
        page_obj = paginator.get_page(current_page)
            
        return render(request=request, template_name="planners_view.html", context=dict(page_obj=page_obj))
    

@login_required
def get_me_planners(request: HttpRequest):
    current_page = request.GET.get("page", 1)
    planners_obj = Paginator(Planner.objects.filter(user=request.user).all(), 2)
    paginator = Paginator(planners, 2)
    planners = paginator.get_page(current_page)
    return render(request=request, template_name="my_planners.html", context=dict(planners=planners))