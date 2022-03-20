from django.contrib import admin
from .models import Enquirys,Member,Attendance,Absentees,History,Notes
# Register your models here.
admin.site.register(Enquirys)
admin.site.register(Member)
admin.site.register(Attendance)
admin.site.register(Absentees)
admin.site.register(History)
admin.site.register(Notes)
