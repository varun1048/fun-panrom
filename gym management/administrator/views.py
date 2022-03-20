from django.shortcuts import render
from .counter import count_main
from .models import  Member ,Absentees,Attendance
import datetime

def home(req):

    for member in Member.objects.all():
        # expired

        joined_count = str(datetime.date.today()-member.joined)[0:2]
        reminder_count = str(datetime.date.today()-member.expiry)[0:3]
        # print(f"{member.joined}\t{joined_count}joined\n{member.expiry}\t{reminder_count}expiry")

        member.color = ""
        member.color_message = "-"

        if joined_count == '0:' or joined_count == '1 ' or joined_count == '2 ' or joined_count == '3 ':
            member.color = "info"
            member.color_message = "New member day " + \
                str(int(str(datetime.date.today()-member.joined)[0])+1)

        if reminder_count == '-1 ' or reminder_count == '-2 ' or reminder_count == '-3 ':
            member.color = 'warning'

            member.color_message = f"Package expire {reminder_count[1]} in days"

        if member.expiry == datetime.date.today():
            member.color = "success"
            member.color_message = "Today payment"

        elif str(datetime.date.today()-member.expiry)[0] != "-" and member.expiry != datetime.date.today():
            member.color = "danger"
            member.color_message = "Package expired  " + \
                str(datetime.date.today()-member.expiry)[0:2] + " day ago."

        if member.hold:
            member.color = "secondary"
            if member.color_message == '-':
                member.color_message ="Holden till " + str(member.hold_date)
            else:
                member.color_message = member.color_message + \
                    "Holden till " + str(member.hold_date)
        try:
            ab = str(Absentees.objects.get(member=member).days_count)
            if member.color_message == '-':
                member.color  = "muted text-dark"
                member.color_message = "  ( A  - "+ ab +" )"
                
            else:
                member.color_message = member.color_message + "   ( A - "+ ab +" )"
        except:
            pass
        
        member.save()

 

    return render(req, 'administrator/home2.html', {
        "count": count_main(),
    })

def fees(req):
    return render(req, 'fee.html', {
    })

def payment(req):
    return render(req, 'payment.html', {
    })
