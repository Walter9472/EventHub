from django.contrib import admin

from .models import Event,Ticket


# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "start_date", "end_date","price", "category","owner","capacity")
    search_fields = ("title","owner")
    list_filter = ( "location", "start_date", "end_date", "category","owner")

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("buyer", "event","seat", "purchase_date","status")
    search_fields = ("buyer", "event","seat")
    list_filter = ("buyer", "event","seat", "purchase_date","status")