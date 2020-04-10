# Register your models here.
from django.contrib import admin
from forward_and_spot.models import Auction, Group
from forward_and_spot.models import Player


class PlayerAdmin(admin.ModelAdmin):
    fields = [ 'user', 'id']


admin.site.register(Auction)
# admin.site.register(Player)
admin.site.register(Group)

admin.site.register(Player, PlayerAdmin)
#  admin.site.register(Group, GroupAdmin)




# class GroupAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'name': ('name',)}


