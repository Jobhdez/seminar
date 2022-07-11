from arxiv.models import Paper
from .evaluator import evaluate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PaperSerializer
from rest_framework.parsers import JSONParser
from .serializers import LinearAlgebraSerializer
from rest_framework import status
import json
from .evaluator import Vec, Matrix

@api_view(['GET'])
def list_papers(request):
    """
    Lists all research papers.

    @param request: A HTTP request
    @return: JSON response containing research paper data
    """
    if request.method == 'GET':
        papers = Paper.objects.all()
        serializer = PaperSerializer(papers, many=True)

        return Response(serializer.data)

@api_view(['POST'])
def compute_linear_algebra_expression(request):
    """
    Given a Linear Algebra expression this view evaluates it.

    @param request: Http POST request
    @return: linear algbera expression
    """
    serializer = LinearAlgebraSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        data = serializer.data
        algebra_expr = data['expression']
        algebra_expr = eval(algebra_expr)
        algebra_expr = evaluate(algebra_expr)

        return Response({"expression":algebra_expr}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
