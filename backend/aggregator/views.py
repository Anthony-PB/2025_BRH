from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

"""
Get Sources


"""

@api_view(['GET'])
def index(request):
    """
    API root endpoint for the aggregator app
    """
    return Response({
        "message": "Content Aggregator API",
        "version": "1.0",
        "endpoints": {
            "users": "/api/users/",
            "articles": "/api/articles/",
            "sources": "/api/sources/",
            "groups": "/api/groups/"
        }
    })

#def sourceCreateView(generics.CreateAPIView):


# You can add more views here later:
# @api_view(['GET'])
# def article_list(request):
#     return Response({"articles": []})