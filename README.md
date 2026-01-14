# Task Manager – Microservices (Google Cloud Run)

## Opis projektu
Projekt przedstawia prostą aplikację typu **Task Manager**, zrealizowaną
w architekturze **mikroserwisowej**. System składa się z dwóch niezależnych
mikroserwisów, które komunikują się ze sobą za pomocą REST API.

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
- udostępnienie endpointu testowego.

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
- Docker
- Google Cloud Build
- Google Cloud Run

---

## Uruchomienie lokalne (Docker)

### Wymagania
- Docker
- Docker Compose

### Instrukcja uruchomienia
W katalogu głównym projektu należy wykonać polecenie:

```bash
docker compose up --build

Po uruchomieniu aplikacji:

Auth Service: http://localhost:8001

Tasks Service: http://localhost:8002

Wdrożenie do chmury (Google Cloud Run)

Projekt został wdrożony do chmury Google Cloud z wykorzystaniem usługi
Google Cloud Run, która umożliwia uruchamianie kontenerów bez konieczności
zarządzania infrastrukturą serwerową.

Auth Service

URL:

https://auth-service-468382717388.europe-central2.run.app


Dostępne endpointy:

/admin/ – panel administracyjny Django

/api/ – REST API

Tasks Service

URL:

https://tasks-service-468382717388.europe-central2.run.app


Dostępne endpointy:

/api/tasks/ – lista zadań

/api/auth-test/ – test komunikacji z Auth Service

Obsługa aplikacji

Aplikacja nie posiada interfejsu graficznego (frontend).
Obsługa odbywa się poprzez przeglądarkę internetową oraz REST API.

1. Auth Service – panel administracyjny

Auth Service udostępnia panel administracyjny Django, który służy do
zarządzania danymi aplikacji oraz celów demonstracyjnych.

Dostęp:
/admin/


Przykład:

https://auth-service-468382717388.europe-central2.run.app/admin/


Po wejściu na stronę użytkownik może:

zalogować się do panelu administratora,

zarządzać danymi systemowymi,

przeglądać konfigurację aplikacji.

2. Tasks Service – zarządzanie zadaniami (REST API)

Tasks Service udostępnia REST API umożliwiające pobieranie listy zadań.

Lista zadań

Endpoint:

/api/tasks/


Przykład:

https://tasks-service-468382717388.europe-central2.run.app/api/tasks/


Po wywołaniu endpointu użytkownik otrzymuje listę przykładowych zadań
w formacie JSON.

3. Test komunikacji mikroserwisów

Tasks Service komunikuje się z Auth Service poprzez REST API.

Endpoint testowy:
/api/auth-test/


Przykład:

https://tasks-service-468382717388.europe-central2.run.app/api/auth-test/


Poprawna odpowiedź:

{
  "status": "usługa uwierzytelniania dostępna"
}


Oznacza to, że:

oba mikroserwisy działają poprawnie,

komunikacja pomiędzy nimi została poprawnie skonfigurowana.

Testy działania
Test REST API
curl https://tasks-service-468382717388.europe-central2.run.app/api/tasks/

Test komunikacji mikroserwisów
curl https://tasks-service-468382717388.europe-central2.run.app/api/auth-test/

Podsumowanie

Projekt spełnia założenia architektury mikroserwisowej:

mikroserwisy są niezależne,

aplikacja została skonteneryzowana,

usługi zostały wdrożone do chmury Google Cloud Run,

komunikacja pomiędzy mikroserwisami odbywa się przez REST API.
