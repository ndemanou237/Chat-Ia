from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nom')
    description = models.TextField(verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Crée le')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Mis à jour le')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Proprietaire')

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.name    

class ChatMessage(models.Model):
    projet = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Projet')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Utilisateur')
    message = models.TextField(verbose_name='Message')
    response = models.TextField(verbose_name='Reponse', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'{self.user} - {self.message[:50]}'
        

