# Map Points

A Django application for saving and visualizing geographic points on an interactive map.

## Features

- Click anywhere on the map to save a point
- All saved points are displayed as markers on map load
- Browse all saved points in a sortable list view

## Local Development

```bash
# 1. Clone and enter the project
git clone https://github.com/AlexLaguta17/test228.git
cd project

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env with your local DB credentials

# 6. Run migrations and start server
python manage.py migrate
python manage.py runserver
```

Open http://localhost:8000

## Docker

```bash
# 1. Configure environment
cp .env.example .env
# Edit .env if needed (defaults work out of the box)

# 2. Build and start
docker compose up --build

# 3. Open in browser
# http://0.0.0.0:8000
```

## Running Tests

```bash
# Activate venv and export env vars first
pytest
```
