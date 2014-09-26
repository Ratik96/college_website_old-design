from django.contrib import admin
import attendence

admin.site.register(attendence.models.attend)
admin.site.register(attendence.models.student_attendence)
admin.site.register(attendence.models.paper_attendence)
