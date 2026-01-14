# Task Manager – Microservices (Google Cloud Run)

## Opis projektu

Projekt przedstawia prostą aplikację typu **Task Manager**, zrealizowaną
w architekturze **mikroserwisowej**. System składa się z dwóch niezależnych
mikroserwisów, które komunikują się ze sobą za pomocą **REST API**.

Celem projektu jest zaprezentowanie:
- architektury mikroserwisowej,
- konteneryzacji aplikacji (Docker),
- wdrożenia aplikacji do chmury **Google Cloud Run**,
- komunikacji pomiędzy mikroserwisami.

Projekt został wykonany w ramach przedmiotu **Chmury obliczeniowe**.

---

## Architektura systemu

System składa się z dwóch mikroserwisów:

### Auth Service
Mikroserwis odpowiedzialny za:
- obsługę uwierzytelniania,
- panel administracyjny Django,
- udostępnienie endpointów REST API.

### Tasks Service
Mikroserwis odpowiedzialny za:
- zarządzanie listą zadań,
- udostępnienie REST API,
- komunikację z mikroserwisem Auth Service.

Każdy mikroserwis:
- działa w osobnym kontenerze Docker,
- jest wdrażany jako niezależna usługa w Google Cloud Run.

---

## Technologie

- Python 3.11  
- Django  
- Django REST Framework  
- Gunicorn  
- Docker  
- Docker Compose  
- Google Cloud Build  
- Google Cloud Run  

---

## Uruchomienie lokalne (Docker)

### Wymagania
- Docker
- Docker Compose

### Instrukcja uruchomienia

W katalogu głównym projektu wykonaj polecenie:

```bash
docker compose up --build
Po uruchomieniu aplikacji dostępne będą:

Auth Service: http://localhost:8001

Tasks Service: http://localhost:8002

Wdrożenie do chmury (Google Cloud Run)
Projekt został wdrożony do chmury Google Cloud z wykorzystaniem usługi
Google Cloud Run, która umożliwia uruchamianie kontenerów bez konieczności
zarządzania infrastrukturą serwerową.

Auth Service
URL:

arduino

https://auth-service-468382717388.europe-central2.run.app
Dostępne endpointy:

/admin/ – panel administracyjny Django

/api/ – REST API

Tasks Service
URL:

arduino

https://tasks-service-468382717388.europe-central2.run.app
Dostępne endpointy:

/api/tasks/ – lista zadań

/api/auth-test/ – test komunikacji z Auth Service

Jak korzystać z aplikacji
Aplikacja nie posiada interfejsu graficznego (frontend).
Obsługa odbywa się poprzez:

panel administracyjny Django,

REST API dostępne z poziomu przeglądarki lub narzędzi typu curl / Postman.

Auth Service – panel administracyjny
Panel administracyjny Django służy do celów demonstracyjnych
oraz zarządzania danymi aplikacji.

Dostęp

https://auth-service-468382717388.europe-central2.run.app/admin/
Po wejściu na stronę użytkownik może:

zalogować się do panelu administratora,

zarządzać danymi systemowymi,

przeglądać konfigurację aplikacji.

Logowanie
Aby zalogować się do panelu administratora, należy użyć konta superusera.

Konto administratora tworzone jest lokalnie za pomocą polecenia:


python manage.py createsuperuser
Dane logowania ustalane są podczas tworzenia konta administratora.

Tasks Service – REST API
Lista zadań
Endpoint:



/api/tasks/
Przykład:



https://tasks-service-468382717388.europe-central2.run.app/api/tasks/
Po wywołaniu endpointu użytkownik otrzymuje listę przykładowych zadań
w formacie JSON.

Test komunikacji mikroserwisów
Tasks Service komunikuje się z Auth Service poprzez REST API.

Endpoint testowy:


/api/auth-test/
Przykład:


https://tasks-service-468382717388.europe-central2.run.app/api/auth-test/
Poprawna odpowiedź:

json

{
  "status": "usługa uwierzytelniania dostępna"
}
Oznacza to, że:

oba mikroserwisy działają poprawnie,

komunikacja pomiędzy nimi została prawidłowo skonfigurowana.

Testy działania
Test REST API

curl https://tasks-service-468382717388.europe-central2.run.app/api/tasks/
Test komunikacji mikroserwisów

curl https://tasks-service-468382717388.europe-central2.run.app/api/au