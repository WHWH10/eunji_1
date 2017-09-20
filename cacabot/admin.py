from django.contrib import admin

from . models import CaKeyfriend
from . models import CaKeyboard
from . models import CaMessage
from . models import CaChatroom

# Register your models here.
class CaMessageAdmin(admin.ModelAdmin):
      list_display = ('userkey','msgtype','message')
      list_filter = ['userkey'] 

admin.site.register(CaKeyfriend)
admin.site.register(CaKeyboard)
admin.site.register(CaMessage,CaMessageAdmin)
admin.site.register(CaChatroom)
