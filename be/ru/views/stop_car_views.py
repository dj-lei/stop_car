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
            car_number = request.GET.get('car_number')
            proxy = get_proxy().get("proxy")
            etcp_params['carNumber'] = car_number
            response_etcp = get_html(etcp_url, etcp_headers, etcp_params, proxy, request_type='GET')

            stop_where_body['REQUESTS'][0]['REQ_COMM_DATA']['car_id'] = car_number[:-5]
            response_stop_where = get_html(stop_where_url, stop_where_headers, stop_where_body, proxy, request_type='POST')

            result = {'CarNumber': car_number, 'ETCP': response_etcp.content.decode(), 'StopWhere': response_stop_where.content.decode()}
            return JsonResponse({'content': result})
    except Exception as e:
        traceback.print_exc()


def run(request):
    try:
        if request.method == 'POST':
            stop_car = request.FILES.get('file')
            table = pd.read_csv(stop_car, encoding='gbk')
            result = []
            for index, car_number in enumerate(table.iloc[:, [0]].values):
                proxy = get_proxy().get("proxy")
                etcp_params['carNumber'] = car_number[0]
                response_etcp = get_html(etcp_url, etcp_headers, etcp_params, proxy, request_type='GET')

                stop_where_body['REQUESTS'][0]['REQ_COMM_DATA']['car_id'] = car_number[0][:-5]
                response_stop_where = get_html(stop_where_url, stop_where_headers, stop_where_body, proxy, request_type='POST')
                print(index, car_number[0], response_etcp.content.decode(), response_stop_where.content.decode())
                result.append({'CarNumber': car_number[0], 'ETCP': response_etcp.content.decode(), 'StopWhere': response_stop_where.content.decode()})
            return JsonResponse({'content': result})
    except Exception as e:
        traceback.print_exc()
