# FeedStream

FeedStream is a hackathon-built RSS reader for browsing, organizing, and saving
articles from selected content sources in one cleaner feed experience.

Built for Big Red Hacks 2025.

## Features

- Browse articles loaded from RSS sources.
- View article cards with titles, publish dates, links, and images.
- Organize content around sources, bookmarks, and topic groups.
- Protect browse and bookmark views behind authentication.
- Run locally with Docker, a Next.js frontend, and a Django REST backend.

## Tech Stack

- **Frontend:** Next.js, TypeScript, Tailwind CSS, shadcn/ui
- **Backend:** Django, Django REST Framework
- **Data:** PostgreSQL models for sources, articles, bookmarks, and tags
- **Infrastructure:** Docker, nginx
- **RSS:** feedparser, dateparser

## Architecture

```text
Next.js frontend
    |
    | source and article requests
    v
Django REST API
    |
    | parse RSS feeds
    v
Source and Article models
```

## Key Backend Areas

- `backend/aggregator` manages RSS sources, articles, feed loading, and bookmarking.
- `backend/users` handles user-related data and followed sources.
- `backend/core` contains shared backend application structure.

## Key Frontend Areas

- `frontend/app/page.tsx` contains the landing page.
- `frontend/app/browse/page.tsx` displays RSS article cards.
- `frontend/app/bookmark/page.tsx` displays saved source groups.
- `frontend/components` contains reusable UI pieces such as navigation, search, filters, and cards.

## Running Locally

### Docker

```bash
docker compose up --build
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deployment

The project includes nginx and Docker configuration for deployment.

Original site links:

- http://18.118.36.75/
- https://feedstream.duckdns.org/
