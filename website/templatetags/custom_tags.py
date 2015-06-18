from django import template

register = template.Library()
from website.models import Reporter

@register.filter(name='get_reporter_pic')
def reporte_picture(username):
    return Reporter.objects.filter(user__username=username)[0].profile_picture.url