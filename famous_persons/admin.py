from django.contrib import admin

from famous_persons.models import Person, Role


class PersonAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "time_create", "time_update", "is_published", "role")
    list_display_links = ("title",)
    search_fields = ("title", "content")
    list_filter = ("role", "is_published")


admin.site.register(Person, PersonAdmin)
admin.site.register(Role)
