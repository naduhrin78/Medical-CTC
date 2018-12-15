from django.contrib import admin
from md_ctc.models import Profile, Scan
# Register your models here.


class TableLayout(admin.ModelAdmin):
    list_display = ('user', 'ct_scan', 'cancer', 'created')


admin.site.register(Scan, TableLayout)

admin.site.register(Profile)
