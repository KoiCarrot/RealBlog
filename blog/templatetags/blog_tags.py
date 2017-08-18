from django import template
from ..models import Category
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post'))