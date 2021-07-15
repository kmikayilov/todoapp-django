from django.db import models

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=50, blank=True)
    color = models.CharField(max_length=50, blank=True)
    rank = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=50, blank=True)


class TodoTask(models.Model):
    task = models.CharField(max_length=50, blank=True)
    label = models.ForeignKey(
        Label, on_delete=models.CASCADE, null=True, related_name="tasks")
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=True, related_name="tasks")
    reminder = models.TimeField(auto_now=False, auto_now_add=True, null=True)
    comment = models.CharField(max_length=50, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=True, null=True)
    project = models.CharField(max_length=50, blank=True)
