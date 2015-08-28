from django.contrib import admin
from django import forms

from modular_blocks import modules
from modular_blocks.fields import ListTextField

from .models import User


# widget for the admin editing
# of sidebar_left and sidebar_right
class ListInput(forms.CheckboxSelectMultiple):
    def __init__(self, **kwargs):
        # TODO we should alert the user here...
        kwargs.pop('choices', None)
        # TODO add a function to ModuleLibrary
        blocks = [(name, name) for name, x in modules.blocks.items()]
        kwargs['choices'] = blocks
        super(ListInput, self).__init__(**kwargs)


    def _format_value(self, value):
        return ','.join(value)


class UserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        ListTextField: {
            'widget': ListInput,
        },
    }
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'sidebar_left',
        'sidebar_right',
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
        'email',
    )


admin.site.register(User, UserAdmin)
