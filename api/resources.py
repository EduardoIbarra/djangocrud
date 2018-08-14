from tastypie.resources import ModelResource
from api.models import Movie
from tastypie.authorization import Authorization

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        authorization = Authorization()