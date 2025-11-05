# Copilot Instructions

This document provides guidance for AI coding agents to effectively contribute to this project.

## Architecture Overview

This is a full-stack web application with a Next.js frontend, a Django backend, and a PostgreSQL database. The entire application is containerized using Docker.

- **Frontend (`/frontend`):** A Next.js/React application using TypeScript. It handles the user interface and client-side logic. Key libraries include `tailwindcss` for styling and a custom `authContext` for authentication. UI components are built with shadcn/ui and located in `/frontend/components/ui`.

- **Backend (`/backend`):** A Django project serving a REST API. It's structured into several apps:
    - `aggregator`: Fetches and processes data from external sources like RSS feeds.
    - `users`: Manages user authentication and profiles.
    - `core`: Contains shared utilities, including database helpers in `core/db_utils.py`.

- **Database:** The project uses PostgreSQL. The backend uses Django's built-in migration system.

- **Deployment:** The application is designed to be deployed with Docker and uses `docker-compose.yml` to orchestrate the services. Nginx is used as a reverse proxy.

## Developer Workflows

### Running the Full Stack

The recommended way to run the application is using Docker:

```bash
docker-compose up --build
```

This will build the containers for the frontend, backend, and database and run them.

### Frontend Development

To work on the frontend locally:

1.  Navigate to the `frontend` directory: `cd frontend`
2.  Install dependencies: `npm install`
3.  Set up your environment variables by copying `.env.example` to `.env` and adding your `MONGODB_URI`.
4.  Start the development server: `npm run dev`

The frontend will be available at `http://localhost:3000`.

### Backend Development

To work on the backend:

1.  Ensure you have a Python environment set up with the dependencies from `backend/requirements.txt`.
2.  The backend is a standard Django project. Use `manage.py` for management commands. For example, to run the development server:
    ```bash
    python backend/manage.py runserver
    ```

## Key Files and Directories

- `docker-compose.yml`: Defines the services, networks, and volumes for the application stack.
- `frontend/api/`: Contains frontend API client logic for authentication and data fetching.
- `backend/aggregator/views.py`: An example of how data is fetched and processed from external sources.
- `backend/users/serializers.py`: Defines the shape of the User API data.
- `backend/core/db_utils.py`: Contains helper functions for interacting with the database.
- `backend/migrations/`: This directory contains database migrations. Use standard Django `migrate` commands.

## Conventions

- The backend exposes a REST API that the frontend consumes. API endpoints are defined in the `urls.py` file of each Django app.
- Frontend components in `frontend/components/` are generally high-level, while reusable, atomic UI elements are in `frontend/components/ui/`.
- Follow existing patterns for code style and organization.
