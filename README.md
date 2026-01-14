# Task Manager – Microservices (Google Cloud)

## Opis projektu
Projekt przedstawia prostą aplikację typu **Task Manager**, zrealizowaną
w architekturze **mikroserwisowej**. System składa się z dwóch niezależnych
mikroserwisów, które komunikują się ze sobą za pomocą REST API.

Celem projektu jest zaprezentowanie:
- architektury mikroserwisowej,
- konteneryzacji aplikacji (Docker),
- wdrożenia aplikacji do chmury **Google Cloud Run**,
- komunikacji między mikroserwisami.

Projekt został wykonany w ramach przedmiotu **Chmury obliczeniowe**.

---

## Architektura systemu

System składa się z dwóch mikroserwisów:

### 1. Auth Service
Mikroserwis odpowiedzialny za:
- obsługę uwierzytelniania,
- panel administracyjny Django,
- udostępnienie endpointu testowego.

### 2. Tasks Service
Mikroserwis odpowiedzialny za:
- zarządzanie listą zadań,
- udostępnienie REST API,
- komunikację z mikroserwisem Auth Service.

Każdy mikroserwis:
- jest uruchamiany w osobnym kontenerze Docker,
- jest wdrażany jako niezależna usługa w Google Cloud Run.

---

## Technologie
- Python 3.11
- Django
- Django REST Framework
- Docker
- Google Cloud Run
- Google Cloud Build

---

## Uruchomienie lokalne (Docker)

### Wymagania
- Docker
- Docker Compose

### Instrukcja
W katalogu głównym projektu należy wykonać polecenie:

```bash
docker compose up --build
