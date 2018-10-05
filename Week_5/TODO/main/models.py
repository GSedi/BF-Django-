from django.db import models

class Owner(models.Model):
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Task(models.Model):
    title = models.CharField("Title", max_length=200)
    created = models.DateTimeField("Created", auto_now_add=True)
    due_on = models.DateTimeField("Due on", auto_now_add=False, editable=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owners')
    mark = models.BooleanField("Mark", default=False)

    def __str__(self):
        return self.title
    