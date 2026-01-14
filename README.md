Task Manager – Microservices (Google Cloud Run)
Opis projektu

Projekt przedstawia prostą aplikację Task Manager, zrealizowaną
w architekturze mikroserwisowej. System składa się z dwóch niezależnych
mikroserwisów, które komunikują się ze sobą za pomocą REST API.

Celem projektu jest zaprezentowanie:

architektury mikroserwisowej,

konteneryzacji aplikacji (Docker),

wdrożenia aplikacji do chmury Google Cloud Run,

komunikacji pomiędzy mikroserwisami,

podstawowej obsługi uwierzytelniania w Django.

Projekt został wykonany w ramach przedmiotu Chmury obliczeniowe.

Architektura systemu

System składa się z dwóch mikroserwisów:

Auth Service

Mikroserwis odpowiedzialny za:

obsługę uwierzytelniania,

panel administracyjny Django,

udostępnienie endpointów REST API,

demonstrację mechanizmu logowania.

Tasks Service

Mikroserwis odpowiedzialny za:

zarządzanie listą zadań,

udostępnienie REST API,

test komunikacji z mikroserwisem Auth Service.

Każdy mikroserwis:

działa w osobnym kontenerze Docker,

jest wdrażany jako niezależna usługa w Google Cloud Run.

Technologie

Python 3.11

Django

Django REST Framework

Gunicorn

Docker

Docker Compose

Google Cloud Build

Google Cloud Run

Uruchomienie lokalne (Docker)
Wymagania

Docker

Docker Compose

Instrukcja uruchomienia

W katalogu głównym projektu wykonaj:

docker compose up --build


Po uruchomieniu aplikacji dostępne są:

Auth Service: http://localhost:8001

Tasks Service: http://localhost:8002

Wdrożenie do chmury (Google Cloud Run)

Projekt został wdrożony do chmury Google Cloud z wykorzystaniem usługi
Google Cloud Run, umożliwiającej uruchamianie kontenerów bez zarządzania
infrastrukturą serwerową.

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
Obsługa odbywa się poprzez:

przeglądarkę internetową (panel admina Django),

REST API.

Auth Service – panel administracyjny

Auth Service udostępnia panel administracyjny Django przeznaczony
do celów administracyjnych i demonstracyjnych.

Dostęp:

/admin/


Przykład:

https://auth-service-468382717388.europe-central2.run.app/admin/


Po wejściu na stronę użytkownik może:

zalogować się do panelu administratora,

przeglądać modele Django,

zarządzać danymi aplikacji.

Użytkownicy i logowanie
🔐 Rejestracja użytkowników

Aplikacja nie udostępnia publicznej rejestracji użytkowników.

Jest to świadoma decyzja projektowa, ponieważ celem projektu jest:

demonstracja architektury mikroserwisowej,

konteneryzacja i wdrożenie do chmury,

komunikacja REST API.

👤 Tworzenie konta administratora (superuser)

Konto administratora tworzone jest ręcznie za pomocą mechanizmu Django.

Lokalnie
cd auth-service
python manage.py createsuperuser


Po utworzeniu konta możliwe jest logowanie do panelu admina:

http://127.0.0.1:8000/admin/

W chmurze (Google Cloud Run)

Wersja chmurowa aplikacji nie posiada publicznej rejestracji ani
automatycznego tworzenia użytkowników.

Panel admina dostępny jest wyłącznie do:

celów demonstracyjnych,

prezentacji działania kontenera,

sprawdzenia poprawności działania usługi.

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
