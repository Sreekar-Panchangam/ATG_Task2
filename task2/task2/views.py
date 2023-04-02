from django.views.generic import TemplateView

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class ConfirmSignUpView(TemplateView):
    template_name = 'confirm.html' 
