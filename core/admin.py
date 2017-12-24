from django.contrib import admin
from core.models import Interaction

# Register your models here.

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'input', 'output']
    search_fields = ['output', 'input']
