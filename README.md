## Cloud deployment (Google Cloud Run)

### Auth Service
URL:
https://auth-service-XXXXX.europe-central2.run.app

Endpoints:
- /admin/
- /api/

### Tasks Service
URL:
https://tasks-service-XXXXX.europe-central2.run.app

Endpoints:
- /api/tasks/
- /api/auth-test/

The services are containerized using Docker and deployed independently
to Google Cloud Run. The tasks-service communicates with the auth-service
to verify authentication availability.
