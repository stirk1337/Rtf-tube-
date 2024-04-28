from django.contrib import admin
from .models import Video, Ip, Comment, History

admin.site.register(Video)
admin.site.register(Ip)
admin.site.register(Comment)
admin.site.register(History)
