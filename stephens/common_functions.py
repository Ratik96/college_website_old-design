import datetime
from django.utils import timezone
from django.core.mail import send_mail

def contact_notification(email_from,email_to,subject,message):
	'''
	Sends an email to email_to and mentions that email_from has sent it
	'''
	msg='Sir/Madam ,\nThis email is from the college website. A person with email Id\n'+str(email_from)+'\n'
	msg+='has attempted to contact you via the college website. In order to keep your contact details private\n'
	msg+='we have contacted you on their behalf. Below is the message intended for you.\n\nCollege Webteam.'
	msg+='\n\nSUBJECT\n'+str(subject)
	msg+='\n--------------------------\nMESSAGE\n'+str(message)
	msg+='\n Of course you can change that password once you are logged in. \nTo login please visit http://www.orfik.com/login \n \n\n\nYour host,\nCompsoc SSC'
	send_mail('St. Stephens website Contact',msg,'computer.society.ssc@gmail.com',[email_to],fail_silently=False)
def create_calender(events):
	'''
	creates a list which acts as a calender'''
	
