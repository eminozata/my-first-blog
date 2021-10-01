from django.contrib import admin

# Register your models here.
from .models import ArchivePost,Contact

admin.site.register(ArchivePost)
admin.site.register(Contact)
