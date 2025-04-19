from django.template.loader import render_to_string

class View:
    def __init__(self, view_name, params):
        self.view_name = view_name
        self.params = params

    def render(self):
        """
        Render the view with the given parameters.
        """
        return render_to_string(self.view_name, self.params)