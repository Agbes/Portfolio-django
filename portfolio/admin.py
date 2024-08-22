from django.contrib import admin
from .models import Propos, Projects, Competences, Diplomes, Langages, FormulaireSoumission

@admin.register(Propos)
class ProposAdmin(admin.ModelAdmin):
    list_display = ('nom_prenom', 'sous_titre', 'created_at', 'updated_at')
    search_fields = ('nom_prenom', 'sous_titre')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description', 'created_at', 'updated_at')
    search_fields = ('project_name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Competences)
class CompetencesAdmin(admin.ModelAdmin):
    list_display = ('competences_name', 'description', 'i_link', 'created_at', 'updated_at')
    search_fields = ('competences_name', 'description', 'i_link')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Diplomes)
class DiplomesAdmin(admin.ModelAdmin):
    list_display = ('diplomes_name', 'description', 'annees', 'etablissement', 'created_at', 'updated_at')
    search_fields = ('diplomes_name', 'description', 'annees', 'etablissement')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(Langages)
class LangagesAdmin(admin.ModelAdmin):
    list_display = ('langages_name', 'description', 'i_link', 'created_at', 'updated_at')
    search_fields = ('langages_name', 'description', 'i_link')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(FormulaireSoumission)
class FormulaireSoumissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_soumission')
    search_fields = ('name', 'email')
    list_filter = ('date_soumission',)
    ordering = ('-date_soumission',)
