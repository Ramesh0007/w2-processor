# DESIGN.md

## Objective
Build a Django async API to process W-2 PDF files, extract fields, and report to a mock API.

## Architecture
- DRF async endpoint `/upload-w2/`
- PDF parsed using `pdfminer.six`
- Async reporting to mock API using `httpx`
- Clear error handling and modular design

## Assumptions
- No sample W-2 provided → used standard IRS W-2 format
- Text-based PDF, not scanned images
- EIN, SSN, and Box values appear with expected labels in text

## Future Considerations
- Add OCR fallback for scanned PDFs
- Add schema validation for API responses
- Use Celery for long-running tasks
