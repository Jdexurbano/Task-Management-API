from django.http import JsonResponse

def get_route(request):
    route = [
        'api/',
    ]

    return JsonResponse(route, safe = False)