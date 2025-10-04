from chat.models import Message
from django.contrib import admin


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'content', 'sent_on']
    list_filter = ['course', 'sent_on']
    search_fields = ['content']
    raw_id_fields = ['user', 'course']
