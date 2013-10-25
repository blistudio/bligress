from django import template
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

register = template.Library()

import re

@register.filter()
def itemsurl(value, board_id):
    matches = re.findall('TASK-(\d+)', value)
    for match in matches:
        location = reverse('kanban:taskshow', args=[board_id, match]);
        value = value.replace('TASK-%s' % (match), '<a href="%s">TASK-%s</a>' % (location, match))
    matches = re.findall('BOARD-(\d+)', value)
    for match in matches:
        location = reverse('kanban:boardshow', args=[match]);
        value = value.replace('BOARD-%s' % (match), '<a href="%s">BOARD-%s</a>' % (location, match))
    return mark_safe(value)

