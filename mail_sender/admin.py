from django.contrib import admin

from mail_sender.models import Customer, SendSettings, ContentEmail, EmailLogs


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name',)


@admin.register(SendSettings)
class SendSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'send_time', 'period', 'status',)


@admin.register(ContentEmail)
class ContentEmailAdmin(admin.ModelAdmin):
    list_display = ('headliner', 'text',)


@admin.register(EmailLogs)
class EmailLogsAdmin(admin.ModelAdmin):
    list_display = ('data_last_sent', 'status_issue', 'server_respond',)



