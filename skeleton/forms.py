from django import forms
from .models import Skeleton

class Skeleton_form(forms.ModelForm):
	class Meta:
		model = Skeleton
		fields = [
			'product_name',
			'product_description',
		] 