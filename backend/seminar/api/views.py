from arxiv.models import Paper
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaperSerializer


@api_view(['GET'])
def list_papers(request):
    """
    Lists all research papers.

    @param request: A HTTP request
    @return: JSON containing research paper data
    """
    if request.method == 'GET':
        papers = Paper.objects.all()
        serializer = PaperSerializer(papers, many=True)

        return Response(serializer.data)
