from django.shortcuts import render
from django.views.generic import (DetailView,UpdateView,)
from .models import (Report,Am,Pm,Eve)
import requests
import datetime
import precipitation
import daily_report


def weather_today(request):
    y_date = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
    today = datetime.date.today()
    yest = False

    try:
        x = Report.objects.get(date=y_date)
        a = Am.objects.get(date=y_date)
        p = Pm.objects.get(date=y_date)
        e = Eve.objects.get(date=y_date)
        yest = True
    except:
        yest = False

    if yest == True:
        x.delete()
        a.delete()
        p.delete()
        e.delete()
        daily_report.create_daily_report()
        yest = False

    if yest == False:
        try:
            y = Report.objects.get(date=today)
        except:
            daily_report.create_daily_report()
            y = Report.objects.get(date=today)

    object = y
    return render(request, 'weather_today.html',context={'object':object})
