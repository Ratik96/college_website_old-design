from django.db import models
from django.forms import ModelForm
def hash_table(models.Model):
	'''Table to store hashes and their answers'''
	string=models.CharField(max_length=5)
	hash=models.CharField(max_length=32)
