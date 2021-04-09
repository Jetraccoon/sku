from api.views import csv


def setup_routes(app):
    app.router.add_route('GET', '/api', csv)
