from django.test import TestCase
from .models import Artist,categories,Craft
# Create your tests here.
#test the Artist model
class ArtistTestClass(TestCase):
    #this method will be run before each test
    def setUp(self):
        self.artist=Artist(first_name="collins",last_name="njau",email="collinsnjau39@gmail.com")


    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.artist,Artist))

    #test for the save method
    def test_save_method(self):
        self.artist.save_artist()
        artists=Artist.objects.all()#returns a list with artists
        self.assertTrue(len(artists)>0)#because we saved the list should have a length>0



class CraftTestClass(TestCase):
    def setUp(self):
        #create new Artist and save
        self.artist=Artist(first_name="collins",last_name="njau",email="collinsnjau39@gmail.com")
        self.artist.save_artist()

        #create categotry and save
        self.category=categories(name="African made")
        self.category.save()

        #create a craft
        self.craft=Craft(craft_name="shambala",craft_price="200",craft_description="This is a test craft",artist=self.artist)
        self.craft.save()

        #add categotry
        self.craft.category.add(self.category)


    def tearDown(self):
        Craft.objects.all().delete()
        categories.objects.all().delete()
        Artist.objects.all().delete()

    #test for getting crafts posted today
    def test_get_crafts_today(self):
        today_craft=Craft.todayCraft()
        self.assertTrue(len(today_craft)>0)

    def test_get_crafts_all(self):
        all_craft=Craft.allCrafts()
        self.assertTrue(len(all_craft)>0)    
