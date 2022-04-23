from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
	item_text = models.CharField(max_length=500)
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.item_text
