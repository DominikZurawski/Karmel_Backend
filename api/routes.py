# flask packages
from flask_restful import Api

# project resources
from api.event import EventsApi, EventApi
from api.patron import PatronsApi, PatronApi, PatronNameApi, PatronDrawApi, PatronDownloadImage
from api.monastery import MonasteriesApi, MonasteryApi
from api.prayer import PrayersApi, PrayerApi, PrayerApiDate, PrayerDownloadById, PrayerDownloadByName
from api.file import FilesApi, FileApi, File_nameApi
from api.chunk import ChunkApi, Chunk_idApi
from api.image import ImageFilesApi, ImageFileApi, ImageFile_nameApi

def create_routes(api: Api):
    

    api.add_resource(EventsApi, '/events/')
    api.add_resource(EventApi, '/event/<event_id>')
    
    api.add_resource(PatronsApi, '/patrons/')
    api.add_resource(PatronDrawApi, '/draw/patron/')  #losuje
    ##/draw/   zrobić losowanie patrona
    api.add_resource(PatronApi, '/patron/<patron_id>')  
    api.add_resource(PatronNameApi, '/patron/name/<patron>')  
    api.add_resource(PatronDownloadImage, '/PatronImage/<filename>')

    api.add_resource(MonasteriesApi, '/monasteries/')
    api.add_resource(MonasteryApi, '/monastery/<monastery_id>')
    
    api.add_resource(PrayersApi, '/prayers/')
    api.add_resource(PrayerApi, '/prayer/<prayer_id>')
    api.add_resource(PrayerApiDate, '/prayerdate/<date>')
    api.add_resource(PrayerDownloadById, '/downloadID/<myid>')
    api.add_resource(PrayerDownloadByName, '/downloadName/<filename>')
    #api.add_resource(PrayerApi, '/prayer/<date>')

    api.add_resource(FilesApi, '/files/')
    api.add_resource(FileApi, '/file/<_id>')
    api.add_resource(File_nameApi, '/filename/<filename>')

    #api.add_resource(ChunksApi, '/chunks/')  #to many data !!!
    api.add_resource(ChunkApi, '/chunk/<_id>')
    api.add_resource(Chunk_idApi, '/chunk/id/<files_id>')

    api.add_resource(ImageFilesApi, '/images/')
    api.add_resource(ImageFileApi, '/image/<_id>')
    api.add_resource(ImageFile_nameApi, '/Imagefilename/<filename>')

    """Adds resources to the api.

    :param api: Flask-RESTful Api Object

    :Example:

        api.add_resource(HelloWorld, '/', '/hello')
        api.add_resource(Foo, '/foo', endpoint="foo")
        api.add_resource(FooSpecial, '/special/foo', endpoint="foo")

    """
    '''
    api.add_resource(SignUpApi, '/authentication/signup/')
    api.add_resource(LoginApi, '/authentication/login/')

    api.add_resource(UsersApi, '/user/')
    api.add_resource(UserApi, '/user/<user_id>')



    api.add_resource(MealsApi, '/meal/')
    api.add_resource(MealApi, '/meal/<meal_id>')

    '''


