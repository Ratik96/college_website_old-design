import .models as models

def get_unsigned_eca_requests(society):
	'''returns unviewed eca requests for the society provided'''
	return models.eca_request.objects.filter(soc=society).filter(signed=None)
def get_unapproved_eca_requests():
	'''returns unapproved eca requests'''
	return models.eca_request.objects.filter(signed=True).filter(approved=None)
