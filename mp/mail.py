#!/usr/bin/python
#coding:utf-8
from django.http import HttpResponse
import urllib
import json
import hashlib
from django.db import connections
import logging
import random
import string
#import datetime
from datetime import date, datetime,time as time2
import time
import urllib2
import requests
#cursor = connections['default'].cursor()
import xml.etree.ElementTree as ET
#from flask import Flask, request, jsonify
#from datetime import date, datetime
import pytz
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

import pay


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date, time2)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))
def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
    	for row in cursor.fetchall()
    	]

def index(request):
    pay.send_order_mail('1514813084')
    resp = HttpResponse('sb', content_type="application/json")

    return resp
