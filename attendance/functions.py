import attendance.models as models
import office

def get_unsigned_eca_requests(user):
	'''returns unviewed eca requests for the user provided if the user is authorized to view'''
	try:
		faculty=office.models.faculty.objects.get(user=user)
	except Exception as e:
		print e
		return None
	else:
		society=faculty.head
		if society!=None:
			return models.eca_request.objects.filter(soc=society).filter(signed=None)
		return None
		
def get_unapproved_eca_requests():
	'''returns unapproved eca requests which have been signed by respective HOD/staff advisors'''
	return models.eca_request.objects.filter(signed=True).filter(approved=None)
