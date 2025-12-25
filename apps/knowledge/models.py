from django.db import models
from markdownx.models import MarkdownxField # Pour le contenu riche

class Category(models.Model):
    """Catégorie de tutoriel (ex: Docker, Réseau, Python)"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="Identifiant URL (ex: docker-basics)")
    icon = models.CharField(max_length=50, help_text="Nom de l'icône (ex: 🐳 ou fa-docker)")
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    """Un article de documentation"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="tutorials")
    summary = models.TextField(blank=True, help_text="Court résumé pour la carte d'aperçu")
    
    # Le contenu principal en Markdown
    content = MarkdownxField()
    
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False, help_text="Cochez pour rendre visible sur le site")

    def __str__(self):
        return self.title
    
    # Pour le futur (Goal 3 IA)
    # On pourra ajouter un champ "vector_embedding" ici pour que ton IA 
    # puisse lire tes tutos et répondre aux questions des visiteurs !