from django.contrib import admin
from .models import PersonalInformation, InstitutionsAttended, WorkExperience


admin.site.register(PersonalInformation)
admin.site.register(InstitutionsAttended)
admin.site.register(WorkExperience)
