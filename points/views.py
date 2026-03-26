import json

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from . import services


class MapView(View):
    """GET: render map with pre-loaded points. POST: save a new point."""

    def get(self, request):
        points = services.get_all_points()
        points_data = [{"latitude": p.latitude, "longitude": p.longitude} for p in points]
        return render(request, "points/map.html", {"points_data": points_data})

    def post(self, request):
        try:
            data = json.loads(request.body)
            point = services.create_point(data.get("latitude"), data.get("longitude"))
        except (json.JSONDecodeError, ValueError) as exc:
            return JsonResponse({"error": str(exc)}, status=400)

        return JsonResponse(
            {"id": point.id, "latitude": point.latitude, "longitude": point.longitude},
            status=201,
        )


class PointsView(View):
    """GET: render points list template."""

    def get(self, request):
        points = services.get_all_points()
        return render(request, "points/list.html", {"points": points})
