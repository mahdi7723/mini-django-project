from django.contrib import admin

from app.models import jobPost, Location, Author, skills


class jobAdmin(admin.ModelAdmin):
    list_display = ('title', 'salary', 'date', 'author', 'location', skills)
    list_filter = ('date', 'salary', 'expiry', 'skills', 'author', 'location')
    search_fields = ('title', 'description')
    search_help_text = "Write in your query and hit enter"


# Register your models here.
admin.site.register(jobPost, jobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(skills)
