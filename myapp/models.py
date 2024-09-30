from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

'Pau Porta'

class Tasks(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete = models.CASCADE)


