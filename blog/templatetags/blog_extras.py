from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.html import format_html

from django.contrib.auth import get_user_model
user_model = get_user_model()

register = template.Library()

@register.filter
def author_details(author: user_model, current_user=None):
  if not isinstance(author, user_model):
    # return empty string as safe default
    return ""

  if author == current_user:
    return format_html("<strong>me</strong>")

  if author.first_name and author.last_name:
    name = f'{author.first_name} {author.last_name}'
  else:
    name = author.username
  if author.email:
    name = format_html(f'<a href="mailto:{author.email}">{name}</a>')
  return format_html(name)