from django.db.models import QuerySet

from .models import Point


def create_point(latitude, longitude) -> Point:
    """Validate and save a new geographic point to the database."""
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except (TypeError, ValueError):
        raise ValueError("latitude and longitude must be valid numbers.")
    if not (-90.0 <= latitude <= 90.0):
        raise ValueError(f"Latitude {latitude} is out of range [-90, 90].")
    if not (-180.0 <= longitude <= 180.0):
        raise ValueError(f"Longitude {longitude} is out of range [-180, 180].")
    return Point.objects.create(latitude=latitude, longitude=longitude)


def get_all_points() -> QuerySet:
    """Return all saved points ordered by creation time (newest first)."""
    return Point.objects.all()
