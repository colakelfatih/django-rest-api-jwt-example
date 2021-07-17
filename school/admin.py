#from school.serializers import SchoolSerializer
from django.contrib import admin
#from django.apps import apps
from .models import ClassName, Student


#Tüm modelleri göster
"""
app = apps.get_app_config('school')
for model_name, model in app.models.items():
    admin.site.register(model)
"""

# Register your models here.
admin.site.register(Student)
admin.site.register(ClassName)
