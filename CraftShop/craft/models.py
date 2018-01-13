from django.db import models
import datetime as dt

# Create your models here.
class Artist(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()

    #make class readable from shell
    def __str__(self):
        return self.first_name

    #save method
    def save_artist(self):
        self.save()




class categories(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Craft(models.Model):
    craft_name=models.CharField(max_length=30)
    craft_price=models.CharField(max_length=10)
    craft_description=models.CharField(max_length=200)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    category=models.ManyToManyField(categories)
    post_date = models.DateTimeField(auto_now_add=True)
    craft_image=models.ImageField(upload_to='crafts/',blank=True)


    #get crafts from today
    @classmethod
    def todayCraft(cls):
        today=dt.date.today()
        craft=cls.objects.filter(post_date__date = today)
        return craft

    @classmethod
    def allCrafts(cls):
        allCraft=cls.objects.all()
        return allCraft

    #filter method
    @classmethod
    def search_by_name(cls,search_term):
        craft=cls.objects.filter(craft_name__icontains=search_term)
        return craft

    def __str__(self):
        return self.craft_name
