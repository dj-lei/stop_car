from ru.views import *


def index(request):
    try:
        if request.method == 'GET':
          return HttpResponse('Hello World!')
    except Exception as e:
        traceback.print_exc()


def query(request):
    try:
        if request.method == 'GET':
          result = []
          for i in range(0, 10):
            result.extend([{'CarNumber': '10', 'ETCP': 'AA', 'JIETINGCHE': 'BB'},{'CarNumber': '11', 'ETCP': 'CC', 'JIETINGCHE': 'DD'}])
          return JsonResponse({'content': result})
    except Exception as e:
        traceback.print_exc()


def run(request):
    try:
        if request.method == 'GET':
          return HttpResponse('Hello World!')
    except Exception as e:
        traceback.print_exc()
