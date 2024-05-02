from django.template import Library
from ..models import Home

register = Library()


@register.simple_tag
def all_home():
    return Home.objects.all()