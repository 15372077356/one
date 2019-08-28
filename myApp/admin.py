from django.contrib import admin
from .models import Grades,Students
# Register your models here.
#  站点配置

class GradesAdmin(admin.ModelAdmin):
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    ist_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5
    # search_fields = []
    # list_per_page =

#注册
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id','gname','gdate','ggirlnum','gboynum','isDelete']
    # ist_filter = ['gname']
    # search_fields = ['gname']
    # list_per_page = 5
admin.site.register(Grades,GradesAdmin)
admin.site.register(Students,StudentsAdmin)
