from django.contrib import admin
from .models import *
# Register your models here.
class playerlistAdmin(admin.ModelAdmin):
	list_display = ['id','player','mail','ifok','time']
	list_display_links = ['id']
	list_filter = ['ifok','time']
	search_fields = ['player','mail']
admin.site.register(playerlist,playerlistAdmin)

class paperlistAdmin(admin.ModelAdmin):
	list_display = ['id','title','pags','ifok','time']
	list_display_links = ['id']
	list_filter = ['ifok','time']
	search_fields = ['title','pags']
admin.site.register(paperlist,paperlistAdmin)

admin.site.site_title="板栗洞"
admin.site.site_header="板栗洞"

from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['action_time','user','content_type','object_id','object_repr','action_flag','change_message']
admin.site.register(LogEntry,LogEntryAdmin)

class SessionAdmin(admin.ModelAdmin):
	list_display = ['session_key','session_data','expire_date']
admin.site.register(Session,SessionAdmin)

class ContentTypeAdmin(admin.ModelAdmin):
	list_display = ['app_label','model']
admin.site.register(ContentType,ContentTypeAdmin)