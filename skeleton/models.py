from django.db import models

# Create your models here.

class Skeleton(models.Model):
	product_name=models.CharField(max_length=50)
	product_description=models.CharField(max_length=200)

	def get_absolute_url_update(self):
		return f"/update/{self.id}"

	def get_absolute_url_delete(self):
		return f"/delete/{self.id}"