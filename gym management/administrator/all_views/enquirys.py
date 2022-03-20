from telnetlib import PRAGMA_HEARTBEAT
from django.shortcuts import render, redirect
from ..models import Enquirys
from .history import add_history
from ..counter import count_enquiry_page
import datetime


def enquirys(req):
    enquirys = Enquirys.objects.all()[::-1]
    if req.method == 'POST':
        data = req.POST
        enquirys = Enquirys.objects.filter(name__startswith=data['queries']) | Enquirys.objects.filter(
            number__startswith=data['queries'])

    return render(req, 'administrator/enquirys/enquirys.html', {
        "page_name": "All enquirys ",
        "count": count_enquiry_page(),
        "enquirys": enquirys,


    })


def add_enquiry(req):
    if req.method == 'POST':
        data = req.POST

        number = data["number"][:5]+"-"+data["number"][5:]
        small_message = data["message"] if len(
            data['message']) < 15 else data['message'][:10]+"..."

        New_enquiry = Enquirys.objects.create(
            name=data['name'],
            number=number,
            message=data['message'],
            small_message=small_message,
            joining_date=data['date'],
            visit_type=data['visit_type']
        )
        New_enquiry.save()
        add_history("enquiry added", New_enquiry.info())

        return redirect("enquirys")

    return render(req, 'administrator/enquirys/add_enquiry.html', {
        "count": count_enquiry_page(),

    })


def delete_enquiry(req, enquiry_id):
    
    enquiry = Enquirys.objects.get(id=enquiry_id)
    add_history("enquiry deleted", enquiry.info())
    enquiry.delete()

    return redirect('enquirys')


def update_enquiry(req):
    if req.method == 'POST':
        data = req.POST
        
        try:
            enquiry = Enquirys.objects.get(id=data['id'])
            enquiry.joining_date = data['date']
            enquiry.save()
        
        except:
            pass
    return redirect('enquirys')



















def enquirys_today(req):
    today = []
    for enquiry in Enquirys.objects.order_by("joining_date"):
        if enquiry.joining_date == datetime.date.today():
            today.append(enquiry)

    return render(req, 'administrator/enquirys/enquirys.html',
                  {
                      "page_name": "Today joining Enquirys",
                      "count": count_enquiry_page(),
                      "enquirys": today,

                  })


def enquirys_expired(req):
    expired = []
    for enquiry in Enquirys.objects.order_by("joining_date"):
        if str(datetime.date.today()-enquiry.joining_date)[0] != "-" and enquiry.joining_date != datetime.date.today():
            expired.append(enquiry)

    return render(req, 'administrator/enquirys/enquirys.html',
                  {
                      "page_name": "Expired enquirys",
                      "count": count_enquiry_page(),
                      "enquirys": expired,

                  })


def enquirys_reminder(req):
    reminder = []
    date = datetime.date.today()
    for i in range(20):
        date += datetime.timedelta(days=1)
        for enquiry in Enquirys.objects.filter(joining_date=date):
            reminder.append(enquiry)

    return render(req, 'administrator/enquirys/enquirys.html', {
        "page_name": "Reminder enquirys",
        "count": count_enquiry_page(),

        "enquirys": reminder,

    })


def enquirys_date_search(req):
    enquirys = []
    if req.method == 'POST':
        data = req.POST
        for enquiry in Enquirys.objects.filter(When__startswith=data['date']):
            enquirys.append(enquiry)

    return render(req, 'administrator/enquirys/enquirys.html',
                  {
                      "page_name": "Enrolled date",
                      "count": count_enquiry_page(),
                      "enquirys": enquirys,

                  })
