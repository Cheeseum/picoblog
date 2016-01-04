from .settings import site as site_settings

def site(request):
    return {'site': site_settings.settings}
