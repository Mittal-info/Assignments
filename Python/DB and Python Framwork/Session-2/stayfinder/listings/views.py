
from django.http import HttpResponse


pg_data = [
    {'name': 'Sunrise PG', 'area': 'Navrangpura', 'monthly_rent': 8000},
    {'name': 'Comfort Stay', 'area': 'Satellite', 'monthly_rent': 10000},
    {'name': 'Green House PG', 'area': 'Maninagar', 'monthly_rent': 5000},
    {'name': 'Royal Residency', 'area': 'Vastrapur', 'monthly_rent': 12000},
    {'name': 'Happy Home PG', 'area': 'Bopal', 'monthly_rent': 6500},
    {'name': 'City Living PG', 'area': 'CG Road', 'monthly_rent': 4000},
]


def home(request):
    return HttpResponse("<h1>StayFinder</h1><p>Find your perfect stay, feel at home!</p>")


def pg_list(request):
    html = "<h1>Available PGs</h1><ul>"

    for pg in pg_data:
        html += f"<li>{pg['name']} - {pg['area']} - ₹{pg['monthly_rent']}/month</li>"

    html += "</ul>"

    return HttpResponse(html)


def pg_detail(request, pg_id):
    if pg_id < 1 or pg_id > len(pg_data):
        return HttpResponse('PG not found', status=404)

    pg = pg_data[pg_id - 1]

    html = f"""
    <h1>{pg['name']}</h1>
    <p>Area: {pg['area']}</p>
    <p>Monthly Rent: ₹{pg['monthly_rent']}</p>
    """

    return HttpResponse(html)
