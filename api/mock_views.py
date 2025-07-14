from rest_framework.decorators import api_view
from rest_framework.response import Response
import uuid

@api_view(['POST'])
def mock_report(request):
    return Response({"report_id": str(uuid.uuid4())}, status=201)

@api_view(['POST'])
def mock_upload(request):
    return Response({"file_id": str(uuid.uuid4())}, status=201)
