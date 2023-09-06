from django.contrib import admin
from .models import Job, Jobtype, Industry, Category, Skill

# Register your models here.
admin.site.register(Job)   
admin.site.register(Jobtype) 
admin.site.register(Industry)   
admin.site.register(Category) 
admin.site.register(Skill) 