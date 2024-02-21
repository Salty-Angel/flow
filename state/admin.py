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
    list_filter = (
        'project',
        'completed',
        'node_type',
    )
    autocomplete_field = ('project',)
    filter_horizontal = ('follows', 'can_be_completed_by', 'depends_on')

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
        (
            'Can Be Completed By',
            {
                'fields': ('can_be_completed_by',),
            },
        ),
        (
            'Follows',
            {
                'fields': ('follows',),
            },
        ),
        (
            'Depends On',
            {
                'fields': ('depends_on',),
            },
        ),
    )

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.myself = obj
        return super().get_form(request, obj, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'follows':
            kwargs['queryset'] = (
                models.Node.objects.filter(
                    node_type=NodeType.PHASE,
                    project=self.myself.project,
                )
                if hasattr(self, 'myself')
                else models.Node.objects.none()
            )
        return super().formfield_for_manytomany(db_field, request, **kwargs)
