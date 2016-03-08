#from django.settings import MEDIA_URL
from django import template
from urlparse import urlparse

from django.conf import settings
register = template.Library()


@register.filter
def get_path(url):
    return str(settings.BASE_DIR) + url

@register.filter
def beautiful(tag):
    return tag.replace('-', ' ').title()


@register.filter
def simpler(tag):
    return tag.replace(' ', '-').replace('_', '-').lower()


class UrlNode(template.Node):
    def __init__(self):
        pass
    def render(self, context):
        request = context['request']
        ab_uri = request.build_absolute_uri('')
        url_data = urlparse(ab_uri)
        return url_data.scheme+'://'+url_data.netloc


class UrlNode_without_http(template.Node):
    def __init__(self):
        pass
    def render(self, context):
        request = context['request']
        ab_uri = request.build_absolute_uri('')
        url_data = urlparse(ab_uri)
        return url_data.netloc



@register.tag
def base_url(parser, token):
    return UrlNode()


@register.tag
def base_url_without_http(parser, token):
    return UrlNode_without_http()


@register.filter
def base_ip(path):
    import socket
    return socket.gethostbyname(socket.gethostname()) + ':8000/'+path

@register.filter
def media(path):
    return settings.MEDIA_URL + path
