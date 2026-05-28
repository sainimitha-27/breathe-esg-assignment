# Breathe ESG Tech Intern Assignment

## Overview

This project is a prototype ESG ingestion and audit review system built using Django REST Framework and React.

The system ingests:

* SAP fuel and procurement data
* Utility electricity data
* Corporate travel data

The platform normalizes records, supports analyst review workflows, flags suspicious records, and maintains audit logs for traceability.

---

## Features

### Backend Features

* Multi-source ESG ingestion
* Scope 1 / Scope 2 / Scope 3 categorization
* Raw vs normalized data separation
* Suspicious data flagging
* Approval and rejection workflows
* Audit trail tracking
* Django admin dashboard

### Frontend Features

* ESG dashboard summary cards
* Normalized ESG records table
* React + Vite frontend

---

## Tech Stack

### Backend

* Django
* Django REST Framework
* SQLite
* Pandas

### Frontend

* React
* Vite

---

## Source Types

### 1. SAP Data

Contains:

* fuel consumption
* procurement activities
* plant-level operational data

### 2. Utility Data

Contains:

* electricity consumption
* meter usage
* billing period information

### 3. Travel Data

Contains:

* flight travel
* hotel stays
* ground transport

---

## Project Structure

```text
BREATHE_ESG
│
├── backend
├── frontend
├── MODEL.md
├── DECISIONS.md
├── TRADEOFFS.md
├── SOURCES.md
├── README.md
```

---

## Running the Backend

```bash
cd backend
pip install django djangorestframework pandas
python manage.py migrate
python manage.py runserver
```

Backend URL:

```text
http://127.0.0.1:8000/admin/
```

---

## Running the Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL:

```text
http://localhost:5173/
```

---

## Prototype Goals

This prototype focuses on:

* ESG data ingestion
* normalization workflows
* analyst review
* suspicious record handling
* audit traceability

The implementation prioritizes realistic workflows over production-scale infrastructure.

---

## Notes

This project was developed as part of the Breathe ESG Tech Intern Assignment.
