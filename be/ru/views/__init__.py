import os
import io
import re
import json
import traceback
import pandas as pd
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseBadRequest
from io import BytesIO
from ru.utils.common import *
from ru.spider.spider import *
from ru.config.platform_params import *

profile = os.environ.get('env', 'develop')
if profile == 'product':
    redis_addr = "http://121.41.42.251:5010"
else:
    redis_addr = "http://121.41.42.251:5010"
