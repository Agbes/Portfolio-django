from django.db import models

# Create your models here.

class Propos(models.Model):
    nom_prenom = models.CharField(max_length=250,default="AGBESSI Gilcheist",unique=True)
    sous_titre = models.CharField(max_length=250,default="Mathématicien & Programmeur web",unique=True)
    propos = models.TextField(max_length=500)
    photo = models.ImageField(upload_to="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nom_prenom
    

class Projects(models.Model):
    project_name = models.CharField(max_length=250,unique=True)
    description = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="image",unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.project_name
    
    
class Competences(models.Model):
    competences_name = models.CharField(max_length=250,unique=True)
    description = models.CharField(max_length=250)
    i_link = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.competences_name
    


class Diplomes(models.Model):
    diplomes_name = models.CharField(max_length=250,unique=True)
    description = models.CharField(max_length=250)
    annees = models.CharField(max_length=250)
    etablissement = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.diplomes_name
    
class Langages(models.Model):
    langages_name = models.CharField(max_length=250,unique=True)
    description = models.CharField(max_length=250)
    i_link = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.langages_name
    


class FormulaireSoumission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date_soumission}"