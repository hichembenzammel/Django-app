from this import d
from django.contrib import admin,messages
from django.forms import DurationField
from .models import *
# Register your models here.

class ProjectInline(admin.StackedInline):
    model=Projet


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name'
    )
    fields=(
        ('last_name','first_name'),
        'email'
    )
    search_fields=(
        'last_name','first_name'
    )
    inlines=[ProjectInline]

class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name'
    )
    fields=(
        ('last_name','first_name'),
        'email'
    )
    search_fields=(
        'last_name','first_name'
    )

class ProjectDurationFilter(admin.SimpleListFilter):
    parameter_name="dure"
    title="Durée"

    def lookups(self, request, model_admin):
        return(
            ('1 Month','Less than 1 month'),
            ('3 Months','Less than 3 months'),
            ('Greater than 3 Months','Greater than 3 months')
        )
    def queryset(self, request, queryset):
        if self.value()=="1 Month":
            return queryset.filter(dure__lte=30)
        if self.value()=="3 Months":
            return queryset.filter(dure__gt=30, dure__lte=90)
        if self.value()=="Greater than 3 Months":
            return queryset.filter(dure__gt=90)

def set_Valid(modeladmin,request,queryset):
    rows=queryset.update(isValid=True)
    if rows==1:
        msg="1 projet was"
    else:
        msg=f"{rows} projects were"
    messages.success(request,message= f"{msg} Successfully marked as valid")

set_Valid.short_description="Validate"

@admin.register(Projet)
class ProjectAdmin(admin.ModelAdmin):

    def set_Invalid(modeladmin,request,queryset):
        number = queryset.filter(isValid=False)
        if number.count()>0:
            messages.error(request,"Projects already set to Not Valid")
        else:
            rows=queryset.update(isValid=False)
            if rows==1:
                msg="1 projet was"
            else:
                msg=f"{rows} projects were"
        messages.success(request,message= f"{msg} Successfully marked as invalid")
        
    set_Invalid.short_description="set invalidate"

    actions=[set_Valid,"set_Invalid"]
    action_on_bottom= True
    action_on_top=True
    
    
    
    list_filter=(
        'creator',
        'isValid',
        ProjectDurationFilter
    )
    
    list_display=(
        'project_name','supervisor','dure','creator','isValid'
    )
    fieldsets=[
        (
            'state',
            {
                'fields': ('isValid',)
            }
        ),
        (
            'About',
            {
                'fields':('project_name',
                ('creator','supervisor'),
                'besoin',
                'description')
                
            }
        ),
        (
            'Durations',
            {
                'classes':('collapse',),
                'fields':('dure','temp_allocated')
            }
        )
    ]
    radio_fields={
        'supervisor':admin.VERTICAL
    }
    autocomplete_fields=['supervisor']
    empty_value_display='-empty-'
    

admin.site.register([MemberShip])
admin.site.register(Student,StudentAdmin)
admin.site.register(Coach,CoachAdmin)
# admin.site.register(Projet,ProjectAdmin)