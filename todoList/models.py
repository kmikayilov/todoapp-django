from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Priority(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    rank = models.IntegerField(default=0, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name

class Label(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=True, blank=True, related_name="labels")

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=True, blank=True, related_name="projects")

    def __str__(self):
        return self.name
class TodoTask(models.Model):
    task = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    label = models.ForeignKey(
        Label, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks")
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks")
    reminder = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    comment = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="tasks")


    def __str__(self):
        return self.task
