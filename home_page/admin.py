from django.contrib import admin

# Register your models here.
from home_page.models import Department, FeedBack

admin.site.register(Department)
admin.site.register(FeedBack)
