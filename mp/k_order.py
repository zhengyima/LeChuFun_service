from django.http import HttpResponse

import json
from django.db import connections

from datetime import date, datetime,time

import math

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date,date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def index(request):

    ano = request.GET['ano']
    raw = {}

    cursor = connections['klook'].cursor()
    cursor.execute("select pno,ptitle,pprice,pprice_old from activity_package where ano = %s", (ano,))
    raw['act_package'] = dictfetchall(cursor)
    cursor.close()

    for package in raw['act_package']:
        cursor = connections['klook'].cursor()
        cursor.execute("select rdetail from activity_package_rule where pno = %s",(package['pno'],))
        package['rule'] = dictfetchall(cursor)
        cursor.close()

    response = HttpResponse(json.dumps(raw), content_type="application/json")
    return response