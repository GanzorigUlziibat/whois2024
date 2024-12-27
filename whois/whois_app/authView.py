
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def register():
    pass


@csrf_exempt
def authCheckService(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except Exception as e:
            res = 'Error json'
            return JsonResponse(res, safe=False)

        if 'action' not in data:
            res = 'No action'
            return JsonResponse(res, safe=False)

        if data['action'] == 'register':
            res = register()  # object bh
            return JsonResponse(res, safe=False)
        else:
            res = 'Error action'
            return JsonResponse(res, safe=False)

    else:
        pass


def sendResponse():
    "resultCode"
    "resultMessage"
    "data"
    "size"
    "action"
    "curDate"
