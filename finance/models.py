from django.db import models

# Create your models here.
class Transaction(models.Model):
	who = models.CharField(blank=True, max_length=300)
	email = models.EmailField(blank=True)
	amount = models.FloatField()
	purpose = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
