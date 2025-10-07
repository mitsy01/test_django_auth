from django.db import models

# Create your models here.

class Planner(models.Model):
    user = models.ForeignKey("UserManager.MySuperUser", on_delete=models.CASCADE)
    contact = models.ForeignKey("PhoneBook.Contact", on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.TimeField()
    title = models.CharField(max_length=500, null=True, blank=True, default=None)
    address = models.CharField(max_length=150, null=True, blank=True, default="Online")
    link = models.URLField(max_length=500, null=True, blank=True, default=None)
    accept = models.BooleanField(default=None, null=True, blank=True)
    
    
    def __str__(self):
        return f"Зустріч '{self.title}' з {self.contact.first_name} {self.contact.last_name}: {self.date} о {self.time}"
    