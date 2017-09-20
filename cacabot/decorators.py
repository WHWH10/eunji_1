import json
from functools import wraps
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

def bot(view_fn):
    @wraps(view_fn)
    @csrf_exempt
    @csrf_protect
    def wrap(request, *args, **kwargs):
        if request.method == 'POST':
            request.JSON = json.loads(request.body.decode('urf8'))
        else:
            request.JSON = {}
        return JsonResponse(view_fn(request, *args, **kwargs) or {})
    return wrap
