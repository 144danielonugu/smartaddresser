from django.contrib import admin
from addressapp import models
# Register your models here.
admin.site.register(models.address)
admin.site.register(models.Note)
