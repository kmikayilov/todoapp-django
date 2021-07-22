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
    color = models.CharField(max_length=50, blank=True)


class Project(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
class TodoTask(models.Model):
    task = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True)
    label = models.ForeignKey(
        Label, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks")
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks", default=Priority.objects.all()[3])
    reminder = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    comment = models.CharField(max_length=50, blank=True)
    time = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks", default=Project.objects.all()[0])


    def __str__(self):
        return f"{self.task} ({self.priority})"
