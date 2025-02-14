from django.db import models

# Create your models here.
class Tasks(models.Model):
    STATUS_TASKS = (
        ("S", "Tarefa concluída"),
        ("N", "Tarefa não concluida")
    )
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_TASKS,blank=False,null=False)
    def __str__(self):
        return self.description