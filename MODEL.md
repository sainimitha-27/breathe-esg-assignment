# MODEL.md

## Goal
Build a data model that can ingest ESG activity data from three sources, normalize it, and support analyst review and audit locking.

## Design principles
- Support multiple client companies
- Keep raw uploaded data separate from normalized data
- Track the source of every row
- Store approval status and audit history
- Allow unit normalization

## Core entities

### 1. Company
Represents the enterprise client.

Fields:
- id
- name
- created_at

### 2. SourceUpload
Represents one upload or import batch from a source.

Fields:
- id
- company_id
- source_type (SAP / Utility / Travel)
- file_name
- uploaded_at
- uploaded_by
- status (pending / processed / failed)

### 3. RawRecord
Stores each original row exactly as received.

Fields:
- id
- source_upload_id
- raw_data (JSON)
- row_number
- parse_status
- error_message

### 4. NormalizedRecord
Stores cleaned and standardized data.

Fields:
- id
- company_id
- source_upload_id
- scope (1 / 2 / 3)
- category (fuel / electricity / travel)
- activity_type
- quantity
- unit
- normalized_quantity
- normalized_unit
- period_start
- period_end
- status (pending_review / approved / rejected)
- suspicious_flag
- approved_by
- approved_at
- locked

### 5. AuditLog
Tracks every change.

Fields:
- id
- normalized_record_id
- action
- old_value
- new_value
- changed_by
- changed_at

## Why this design
- Raw data is preserved for traceability
- Normalized data is used for analysis and audit
- SourceUpload groups records into batches
- AuditLog keeps a complete history
- Status fields support analyst review

## What this model handles
- SAP fuel/procurement CSV data
- Utility electricity CSV data
- Travel CSV data
- Unit conversion and normalization
- Approval workflow
- Audit trail

## What I am intentionally not handling
- Real SAP API integration
- PDF OCR for utility bills
- Automatic emission factor lookup from live APIs
- Complex multi-step workflow approvals