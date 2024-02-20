from django.contrib import admin

from . import models
from state.models.node import NodeType


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('project', 'title', 'completed')
    autocomplete_field = ('project',)

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'project',
                    ('title', 'description'),
                    'node_type',
                    ('completed', 'completed_on'),
                )
            },
        ),
    )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'follows':
            kwargs['queryset'] = modles.Node.objects.filter(
                node_type=,
                disabled_account=False,
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)

