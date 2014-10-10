from django import forms
import admission

class candidate(forms.ModelForm):
	class Meta:
		model=admission.models.admission_candidate
		exclude=['cutoff_status','admitted']
