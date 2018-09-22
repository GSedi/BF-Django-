from django.db import models

class Owner(models.Model):
    name = models.CharField("Name", max_length=50)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField("Title", max_length=200)
    created = models.DateTimeField("Created", auto_now_add=True)
    due_on = models.DateTimeField("Due on", auto_now_add=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    mark = models.BooleanField("Mark", default=False)

    def __str__(self):
        return self.title
    