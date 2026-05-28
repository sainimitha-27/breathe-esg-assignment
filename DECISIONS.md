# DECISIONS.md

## Key Decisions

### 1. CSV Uploads for All Sources
I chose CSV uploads for SAP, utility, and travel data because CSV exports are common in enterprise workflows and realistic for a prototype with a 4-day timeline.

### 2. Django REST Framework
I used Django REST Framework because it provides rapid backend development, admin tooling, ORM support, and strong support for structured data models.

### 3. Separate Raw and Normalized Records
I separated raw uploaded data from normalized records to preserve traceability and support audit workflows.

### 4. Manual Analyst Review Workflow
I added approval, rejection, suspicious flags, and audit locking to simulate realistic ESG analyst review processes.

### 5. Scope Categorization
Records are categorized into Scope 1, Scope 2, and Scope 3 emissions depending on source type and activity category.

## Assumptions

- SAP data is exported as CSV instead of using direct SAP APIs.
- Utility data is uploaded as CSV exports from utility portals.
- Travel data is exported from corporate travel platforms.
- Analysts manually review suspicious records before approval.

## Questions I Would Ask the PM

- What emission factor library should be used?
- Should approvals support multiple reviewer levels?
- What data retention policies are required?
- Should integrations support real-time ingestion?