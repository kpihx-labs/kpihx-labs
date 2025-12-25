from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # L'interface d'administration
    path('admin/', admin.site.urls),
    
    # Support pour l'upload d'images dans le Markdown
    path('markdownx/', include('markdownx.urls')),
    
    # Nos applications
    path('', include('apps.core.urls')), # La page d'accueil
    # path('docs/', include('apps.knowledge.urls')), # On activera ça quand on aura fait les vues
]

# En mode DEBUG (Dev), Django sert les fichiers médias (images uploadées)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)