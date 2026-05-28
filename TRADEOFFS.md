# TRADEOFFS.md

## Tradeoffs

### 1. No Real SAP Integration
I used CSV-based SAP exports instead of direct SAP APIs or OData services because implementing enterprise SAP connectivity was outside the scope of a 4-day prototype.

### 2. No PDF OCR Parsing
Utility bills were handled as CSV exports instead of PDF parsing and OCR. OCR pipelines introduce additional complexity and would require more time for reliable extraction and validation.

### 3. No Real-Time Data Pipelines
The system uses manual uploads instead of real-time streaming or scheduled ingestion jobs. This simplified deployment and reduced infrastructure complexity.

### 4. Simplified Authentication
The prototype uses Django admin authentication instead of implementing role-based enterprise access controls and SSO integrations.

### 5. No Emission Factor Engine
The system focuses on ingestion, normalization, review, and audit workflows. Actual carbon emission calculations and factor libraries were intentionally left out of scope.