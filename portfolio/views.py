from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .models import Propos, Projects, Competences, Diplomes, Langages, FormulaireSoumission
from .forms import MonFormulairePersonnalise
import logging

logger = logging.getLogger(__name__)
class PortfolioView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajout des données du portfolio
        context['propos'] = Propos.objects.all()
        context['projects'] = Projects.objects.all()
        context['competences'] = Competences.objects.all()
        context['diplomes'] = Diplomes.objects.all()
        context['langages'] = Langages.objects.all()
        context['form'] = MonFormulairePersonnalise()  # Formulaire à inclure dans le contexte
        return context

    
    def post(self, request, *args, **kwargs):
        logger.info("avant if.........")
        form = MonFormulairePersonnalise(request.POST)
        if form.is_valid():
            logger.info("Dans iffffffffffffff")
            FormulaireSoumission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect('index')
        logger.info("apres ifffffffffffffff")
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)