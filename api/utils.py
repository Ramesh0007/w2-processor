from io import BytesIO
from pdfminer.high_level import extract_text
import re
import httpx
from django.conf import settings


BASE_URL = "http://localhost:8000/mockapi"

headers = {
    "X-API-Key": settings.FINPRO_API_KEY,
}


def extract_w2_fields(uploaded_file):
    # Ensure file pointer is at the start
    uploaded_file.seek(0)

    # Read file into memory buffer (required for extract_text)
    file_bytes = uploaded_file.read()
    buffer = BytesIO(file_bytes)

    text = extract_text(buffer)

    # DEBUG: print(text) if needed

    data = {
        "ein": re.search(r"EIN:\s*(\d{2}-\d{7})", text).group(1),
        "ssn": re.search(r"SSN:\s*(\d{3}-\d{2}-\d{4})", text).group(1),
        "wages": re.search(r"Box 1:\s*\$?([\d,]+\.\d{2})", text).group(1),
        "federal_tax_withheld": re.search(r"Box 2:\s*\$?([\d,]+\.\d{2})", text).group(1),
    }

    return data




async def report_to_api(data):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/reports", json=data, headers=headers)
        response.raise_for_status()
        return response.json()

async def upload_to_api(report_id, file):
    async with httpx.AsyncClient() as client:
        files = {'file': (file.name, file.read())}
        data = {'report_id': report_id}
        response = await client.post(f"{BASE_URL}/files", data=data, files=files, headers=headers)
        response.raise_for_status()
        return response.json()
