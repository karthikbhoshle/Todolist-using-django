from django.db import models

class Tasklist(models.Model):
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)

    def __str__(self):
        return self.task


# Create your models here.
