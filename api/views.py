from rest_framework.response import Response
from rest_framework.decorators import api_view
from booksapi.models import BooK
from .serializers import bookSerializer

@api_view(['GET'])
def getData(request):
    BooKs = BooK.objects.all()
    serializer = bookSerializer(BooKs, many=True)
    return Response(serializer.data)
    