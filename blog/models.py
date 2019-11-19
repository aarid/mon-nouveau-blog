from django.conf import settings
from django.db import models
from django.utils import timezone

# effacer manuellement la liste des requêtes
from django.db import reset_queries
reset_queries()

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#Ibrahim
class Joueur(models.Model):
    cleJoueur= models.CharField(max_length=10, primary_key=True)
    nomJoueur = models.CharField(max_length= 50, null=True)
    motDePasse = models.CharField(max_length= 100, null=True)


#Aguibou
class Reponse(models.Model):
    cleReponse = models.IntegerField(primary_key=True)
    description = models.CharField(max_length= 200, null=True)

    def __str__(self):
        return self.description

class Question(models.Model):
    idQuestion = models.IntegerField().primary_key = True
    description = models.CharField(max_length=200, null=True)
    
    #reponses = models.ManyToManyField(Reponse)

    def __str__(self):
        return self.description


class Image(models.Model):
    cleImage = models.IntegerField().primary_key = True
    image = models.ImageField()
    auteur = models.CharField(max_length=100)
    date_creation = models.DateTimeField(default=timezone.now) 
    designation = models.CharField(max_length=100)
    matiere_technique = models.CharField(max_length=100)
    domaine = models.CharField(max_length=50)
    titre = models.CharField(max_length=200)
    sujet = models.TextField()
    
    #joueurs = models.ManyToManyField(Joueur, related_name="images", blank=True)
    questions = models.ManyToManyField(Question, through='Concerner', through_fields=('idImage','idQuestion') )
    
    def afficher_image(self):
        # Pas totalement fini, 1ere étape...
        print(self.image)
        
class Concerner(models.Model):
    idImage = models.ForeignKey(Image, on_delete = models.CASCADE)
    idQuestion = models.ForeignKey(Question, on_delete = models.CASCADE) 

class Avis(models.Model):
    cleAvis = models.IntegerField(primary_key = True)
    aime = models.BooleanField()
    commentaire = models.CharField(max_length = 500, null=True)
    #cleJoueur = models.ForeignKey(Joueur,on_delete = models.CASCADE)
    cleImage = models.ForeignKey(Image,on_delete = models.CASCADE)
