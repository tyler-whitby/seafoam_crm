#stronghold new mware class
from django.utils.deprecation import MiddlewareMixin
from stronghold.middleware import LoginRequiredMiddleware

class SiteLoginRequiredMiddleware(MiddlewareMixin, LoginRequiredMiddleware):
    pass