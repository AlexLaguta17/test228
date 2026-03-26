import pytest
from django.db.models import QuerySet

from points.models import Point
from points.services import create_point, get_all_points


@pytest.mark.django_db
class TestCreatePoint:
    def test_creates_point_with_correct_coordinates(self):
        point = create_point(latitude=51.5, longitude=-0.1)

        assert point.pk is not None
        assert point.latitude == 51.5
        assert point.longitude == -0.1

    def test_persists_point_to_database(self):
        create_point(latitude=40.7, longitude=-74.0)

        assert Point.objects.count() == 1

    def test_returns_point_instance(self):
        result = create_point(latitude=0.0, longitude=0.0)

        assert isinstance(result, Point)

    def test_raises_on_latitude_too_high(self):
        with pytest.raises(ValueError):
            create_point(latitude=91.0, longitude=0.0)

    def test_raises_on_latitude_too_low(self):
        with pytest.raises(ValueError):
            create_point(latitude=-91.0, longitude=0.0)

    def test_raises_on_longitude_too_high(self):
        with pytest.raises(ValueError):
            create_point(latitude=0.0, longitude=181.0)

    def test_raises_on_longitude_too_low(self):
        with pytest.raises(ValueError):
            create_point(latitude=0.0, longitude=-181.0)

    def test_accepts_boundary_coordinates(self):
        point = create_point(latitude=90.0, longitude=180.0)

        assert point.pk is not None


@pytest.mark.django_db
class TestGetAllPoints:
    def test_returns_empty_queryset_when_no_points(self):
        result = get_all_points()

        assert result.count() == 0

    def test_returns_all_saved_points(self):
        create_point(latitude=10.0, longitude=20.0)
        create_point(latitude=30.0, longitude=40.0)

        result = get_all_points()

        assert result.count() == 2

    def test_returns_queryset(self):
        result = get_all_points()

        assert isinstance(result, QuerySet)

    def test_newest_point_first(self):
        first = create_point(latitude=1.0, longitude=1.0)
        second = create_point(latitude=2.0, longitude=2.0)

        result = get_all_points()

        assert result[0].pk == second.pk
        assert result[1].pk == first.pk
