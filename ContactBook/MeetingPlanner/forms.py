from django import forms 

from .models import Planner
from PhoneBook.models import Contact


class PlannerForm(forms.ModelForm):
    contact = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        label="Оберіть контакти для зустрічі",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    date = forms.DateField(
        label="Дата зустрічі",
        widget=forms.DateInput(attrs={"class": "form-control"})
    )
    time = forms.TimeField(
        label="Час зустрічі",
        widget=forms.TimeInput(attrs={"class": "form-control"})
    )
    titile = forms.CharField(
        label="Тема зустрічі",
        max_length=500,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    address = forms.CharField(
        label="Місце зустрічі",
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    link = forms.URLInput(
        label="Посилання для онлайн зустрічі",
        max_lenght=500,
        required=False,
        widget=forms.URLInput(attrs={"class": "form-control"})
    )
    
    
    class Meta:
        model = Planner
        fields = ["contact", "date", "time", "title", "address", "link"]