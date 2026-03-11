from django.views.generic import TemplateView
from web_project import TemplateLayout



class testView(TemplateView):


    def get_user_data(self):
        user_data = {
            'name': 'Saiful Islam',
            'age': 30,
            'email': 'john@example.com',
            'city': 'New York'
        }

        return user_data


    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        context['user_data'] = self.get_user_data()

        return context
