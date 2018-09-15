from django.contrib import admin
from weight.models import Weight

# Register your models here.
# admin.site.register(Weight)


class WeightAdmin(admin.ModelAdmin):
    list_display = ('date', 'weight', 'body_fat', 'user')
    list_filter = ('user', 'date')


admin.site.register(Weight, WeightAdmin)
