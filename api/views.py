from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import Person
from .serializers import PersonSerializer

@api_view(['GET'])
def get_data(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_data(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()