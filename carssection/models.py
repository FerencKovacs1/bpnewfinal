from django.db import models

class Carssection(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    #add fckstg

#manage.py makemigration
#migrate
    def __str__(self):
        return self.title   #show the title helyett obkjcs  #how to look in shell and orm

    def snippet(self):
        return self.body[:50] + '...'
#majd tt azt kell csinálni hogy csak a képet adja vissza mega title szöveget a modellrőlés a
#és akkor ez olyan lesz hogy mutatja az új autókat és akkor majd a kép és név lesz alatt és lehet majd választani
#képre kattintva pedig tovább visza az autónak az oldalára
