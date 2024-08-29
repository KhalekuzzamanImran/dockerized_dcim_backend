from pop.models import POP, POPDevice, POPDeviceState
from django.contrib import admin


class POPAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'status', 'latitude', 'longitude', 'network_status', 'user', 'is_active']
    list_per_page = 20


admin.site.register(POP, POPAdmin)


class POPDeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'pop_name', 'code', 'name', 'is_active', 'status']
    list_per_page = 20


admin.site.register(POPDevice, POPDeviceAdmin)


class POPDeviceStateAdmin(admin.ModelAdmin):
    list_display = ['id', 'device_code', 'topic', 'time_range']
    list_per_page = 20


admin.site.register(POPDeviceState, POPDeviceStateAdmin)



    