
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from whois.settings import sendResponse


def register():

    return sendResponse(204)


@csrf_exempt
def authCheckService(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            res = sendResponse(4001)
            return JsonResponse(res)
        
        if 'action' not in data:
            res = sendResponse(4002)
            return JsonResponse(res)
        
        if data['action'] == 'register':
            res = register()
            return JsonResponse(res)
        else:
            res = sendResponse(4003)
            return JsonResponse(res)

    else:
        res = sendResponse(405)
        return JsonResponse(res)
