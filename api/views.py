# api/views.py
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import sync_and_async_middleware
from asgiref.sync import sync_to_async
from .utils import extract_w2_fields, report_to_api, upload_to_api

@csrf_exempt
async def async_upload_view(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    file = request.FILES.get('file')
    if not file:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    try:
        extracted_data = await sync_to_async(extract_w2_fields)(file)
        print(extracted_data,'extracted_data1')
        report_response = await report_to_api(extracted_data)
        report_id = report_response.get("report_id")

        # rewind the file pointer to upload again
        file.seek(0)
        file_response = await upload_to_api(report_id, file)

        return JsonResponse({
            "report_id": report_id,
            "file_id": file_response.get("file_id")
        }, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
