# W-2 PDF Processor (Technical Assessment - Prudent.AI)

This project is an asynchronous Django service that accepts W-2 PDF files, extracts important tax-related fields, and reports them to a third-party (mocked) API.

---

## 🚀 Features

- ✅ Async API endpoint using Django
- ✅ Parses W-2 PDF (text-based) using `pdfminer.six`
- ✅ Extracts:
  - Employer Identification Number (EIN)
  - Social Security Number (SSN)
  - Wages (Box 1)
  - Federal Tax Withheld (Box 2)
- ✅ Sends extracted data and file to mocked third-party API using `httpx`
- ✅ Robust error handling for file input and API failures

---

## 🛠️ Tech Stack

- Python 3.9+
- Django 5.x
- Django REST Framework
- pdfminer.six (for PDF text extraction)
- httpx (for async HTTP requests)
- PostgreSQL / SQLite (configurable)

---

## 📂 API Endpoints

| Method | Endpoint           | Description                           |
|--------|--------------------|---------------------------------------|
| POST   | `/upload-w2/`      | Upload W-2 PDF and extract/report data|
| POST   | `/mockapi/reports` | Mocked endpoint to receive W-2 fields |
| POST   | `/mockapi/files`   | Mocked endpoint to receive W-2 file   |

---

## 🔐 Authentication

All API calls to the mocked third-party require:

## X-API-Key: FinPro-Secret-Key


This is set in `.env` via `FINPRO_API_KEY`.

---

## 📄 Assumptions

Please refer to `DESIGN.md` for assumptions, architecture decisions, and Future Considerations.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Ramesh0007/w2-processor.git
cd w2-processor
### 2. Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3. Install Requirements
pip install -r requirements.txt

### 4. Configure Environment Variables
Create a .env file in the root directory and update:

FINPRO_API_KEY=FinPro-Secret-Key

### Testing the API
### Start the Django server:

python manage.py runserver

### Open Postman and Create a New Request
Method: POST

URL: http://127.0.0.1:8000/upload-w2/

### Add Headers

| Key         | Value               |
| ----------- | ------------------- |
| `X-API-Key` | `FinPro-Secret-Key` |

### Set the Body
Select Body tab.

Choose form-data.

Add a new key:

Key: file (must be exactly file)

Type: File

Value: Select your sample-w2.pdf

### You should receive:


{
  "report_id": "some-uuid",
  "file_id": "some-uuid"
}