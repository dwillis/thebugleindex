from django.contrib import admin
from models import Subject, Episode, Mention, Speaker, Segment

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('number', 'sub_episode', 'date', 'title')
    prepopulated_fields = {'slug': ('title',)}

class SpeakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
class MentionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'segment', 'speaker', 'timestamp')

class SegmentAdmin(admin.ModelAdmin):
    list_display = ('episode', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Mention, MentionAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Segment, SegmentAdmin)
