# Breathe ESG Tech Intern Assignment

## Overview

This project is a prototype ESG ingestion and audit review platform built using Django REST Framework and React.

The system supports:

* ESG data ingestion
* record normalization
* suspicious data detection
* analyst approval workflows
* audit trail tracking

The platform handles ESG records from:

* SAP operational systems
* utility electricity data
* corporate travel data

---

## Features

### Backend

* Django admin dashboard
* Raw vs normalized record separation
* Scope 1, Scope 2, Scope 3 categorization
* Suspicious record flagging
* Approval and rejection workflows
* Audit logging and traceability

### Frontend

* React dashboard
* ESG statistics cards
* Normalized ESG records table
* Simple analytics visualization

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

### SAP Data

Contains:

* fuel usage
* procurement information
* operational activities

### Utility Data

Contains:

* electricity consumption
* meter-based energy data

### Travel Data

Contains:

* flight emissions
* hotel stays
* transportation records

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

## Backend Setup

```bash
cd backend
pip install django djangorestframework pandas
python manage.py migrate
python manage.py runserver
```

Backend Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## Frontend Setup

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

## Goals

This prototype focuses on:

* ESG workflow simulation
* auditability
* suspicious data handling
* normalization pipelines
* analyst review processes

The project prioritizes realistic ESG operational workflows over production-scale infrastructure.

---

## Assignment Context

This project was developed as part of the Breathe ESG Tech Intern Assignment.
