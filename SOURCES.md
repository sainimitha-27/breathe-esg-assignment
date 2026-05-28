# SOURCES.md

## 1. SAP Fuel and Procurement Data

### Research
I researched typical SAP export formats including flat-file CSV exports, IDoc structures, and OData services. For the prototype, I selected CSV exports because they are common in enterprise reporting workflows and easy to simulate realistically.

### Sample Data
The SAP sample data contains:
- plant codes
- fuel types
- quantities
- units
- procurement activities

### Realistic Challenges
- inconsistent units
- plant code mapping
- non-standard date formats
- incomplete procurement descriptions

---

## 2. Utility Electricity Data

### Research
I researched how facilities teams typically download electricity usage data from utility portals. CSV exports are commonly used for reporting and operational analysis.

### Sample Data
The utility sample data contains:
- meter IDs
- electricity usage in kWh
- billing periods
- tariff-related metadata

### Realistic Challenges
- billing cycles not aligned with calendar months
- missing meter metadata
- inconsistent unit naming

---

## 3. Corporate Travel Data

### Research
I reviewed travel platform structures used by systems such as Concur and Navan. Travel exports commonly include flights, hotel stays, and ground transportation records.

### Sample Data
The travel sample data contains:
- airport codes
- travel categories
- travel distances
- hotel stays

### Realistic Challenges
- missing distance values
- inconsistent transport categories
- incomplete route metadata

---

## Limitations

This prototype focuses on ingestion, normalization, analyst review, and audit traceability. It does not implement:
- real enterprise integrations
- OCR pipelines
- automated emission factor calculations
- production-scale infrastructure