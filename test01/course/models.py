from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{self.id}  {self.name}  {self.desc}'