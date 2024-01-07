from django.conf import settings
from django.utils import timezone

class CustomDebugMiddleware:

    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.start_time = None
        self.website = {
            'url': 'https://www.djangoproject.com',  # You may enter any website you want to show
            'debug': settings.DEBUG,
            'response_time': None
        }

    def __call__(self, request, *args, **kwargs):

        # print('calling - app_customddlware')  # To ensure that this function is being called when you run project
        response = self.get_response(request)

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):

        self.start_time = timezone.now()
    
    def process_template_response(self, request, response):

        # print('calling - process-template-response')  # To ensure that this function is being called when you run project
        
        # response.context_data['website_url'] = 'https://www.djangoproject.com'  # You may enter any website you want to show

        if settings.DEBUG:
            response.context_data['website'] = self.website
            response.context_data['website']['response_time'] = timezone.now() - self.start_time

        return response