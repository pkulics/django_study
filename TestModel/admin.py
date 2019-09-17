from django.contrib import admin
from TestModel.models import Test,Contect,Tag
# Register your models here.

class ContectAdmin_bac(admin.ModelAdmin):
    fields = ('name','email')


class ContectAdmin_bak(admin.ModelAdmin):
    fieldsets = ([
        'Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes':('collapse',), #CSS
            'fields':('age',),
        }]
        )

class TagInline(admin.TabularInline):
    model = Tag


class ContectAdmin_b(admin.ModelAdmin):
    inlines = [TagInline] # inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes':('collapse',),
            'fields':('age',),
        }]
    )


class ContectAdmin(admin.ModelAdmin):
    list_display = ('name','age','email') #  list
    search_fields = ('name',)
    inlines = [TagInline] # inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes':('collapse',),
            'fields':('age',),
        }]
    )
admin.site.register(Contect,ContectAdmin)
admin.site.register([Test])
