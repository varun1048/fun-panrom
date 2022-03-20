# import this
from django.shortcuts import render, redirect
from ..models import  Member ,Absentees,Attendance
from .history import add_history
from ..counter import *
import datetime
# from ..forms import *


def add_member(req):

    if req.method == 'POST':
        data = req.POST
        new_member = Member.objects.create(
            name = data["name"], 
            memberId=data["memberId"], 
            number = data["number"], 
            joined = data["joined"], 
            expiry = data["expiry"], 
            shift_type = data['Shift'],
            # image  = data['image'], 
            )
        
        new_member.save()
        return redirect(f'member/{new_member.id}/')
        
    return render(req, 'administrator/members/add_member.html',{
        "page_name": "Add Member",
        "count": count_members_page(),
    })
    # return redirect(f'http://localhost:8000/admin/administrator/member/add/')


def member_login(req):

    if req.method == 'POST':

        try:
            member = Member.objects.get(memberId=req.POST["id"])

        except:
            return render(req, 'administrator/members/members_login.html', {
                "count": count_members_page(),

                "message": "No data"
            })

        return render(req, 'administrator/members/member_login.html', {
            "count": count_members_page(),
            "member": member,
        })

    return render(req, 'administrator/members/members_login.html', {
    })


def member(req, member_id):
    member = Member.objects.get(id=member_id)

    return render(req, 'administrator/members/member.html', {
        "member": member,
        "page_name": member.name,
        "count": count_members_page(),
        "hold": "unchecked"
    })


def members(req):
    members_color()
    members = Member.objects.all()
    if req.method == 'POST':
        data = req.POST
        members = Member.objects.filter(name__startswith=data['queries']) | Member.objects.filter(
            memberId__startswith=data['queries']) | Member.objects.filter(number__startswith=data['queries'])

    return render(req, 'administrator/members/members.html', {
        "page_name": "Members",
        "members": members[::-1],
        "count": count_members_page()
    })



def edit_member(req):
    if req.method == 'POST':
        data = req.POST['id']
        return redirect(f'admin/administrator/member/{data}/change/')


def update_package(req):
    if req.method == 'POST':
        data = req.POST
        member = Member.objects.get(id=data['id'])
        if data['password'] == "1":

            member.expiry = data['date']
            member.save()
            members_color()
            add_history("package updated", member.info())

            # print()

        id = data['id']
        return redirect(f'member/{id}/')


def hold_member(req):
    if req.method == 'POST':
        data = req.POST
        member = Member.objects.get(id=data['id'])

        try:
            if bool(data["hold"]):
                member.hold = True

            if bool(data["date"]):
                member.hold_date = data["date"]

            if bool(data["reason"]):
                member.hold_reason = data["reason"]

            member.save()

        except:
            member.hold = False
            member.hold_date = None

            member.save()
        members_color()
        id = data['id']
        return redirect(f'member/{id}/')

    members = []
    for member in Member.objects.order_by("hold_date")[::-1]:
        if member.hold == True:
            members.append(member)
    return render(req, "administrator/members/hold_member.html", {
        "page_name": "All holden members",

        "members": members,
        "count": count_members_page(),

    })


def hold_member_list(req):

    if req.method == 'POST':
        data = req.POST
        members = []
        if data["type"] == "today":
            page_name = "Rejoing today members"
            for member in Member.objects.filter(hold=True) and Member.objects.filter(hold_date=datetime.date.today()) .order_by("hold_date")[::-1]:
                members.append(member)

        if data["type"] == "expired":
            page_name = "Expired holden members"

            for member in Member.objects.filter(hold=True):
                try:
                    if str(datetime.date.today()-member.hold_date)[0] != "-" and member.hold_date != datetime.date.today():
                        members.append(member)
                except:
                    pass

        if data["type"] == "reminder":
            page_name = "Reminder holden members"

            for member in Member.objects.filter(hold=True):
                try:
                    reminder_count = str(
                        datetime.date.today()-member.hold_date)[0:3]
                    if reminder_count == '-1 ' or reminder_count == '-2 ' or reminder_count == '-3 ':
                        # if reminder_count in ['-1 ','-2 ','-3 ']:
                        members.append(member)
                except:
                    pass

        return render(req, "administrator/members/hold_member.html", {
            "page_name": page_name,
            "members": members,
            "count": count_members_page(),


        })
    else:
        members = []
        page_name = "Rejoing today members"
        for member in Member.objects.filter(hold=True) and Member.objects.filter(hold_date=datetime.date.today()) .order_by("hold_date")[::-1]:
            members.append(member)

        return render(req, "administrator/members/hold_member.html", {
            "page_name": page_name,
            "members": members,
            "count": count_members_page()
        })


def achievement(req):
    from datetime import datetime
# ---------------------------------------------------------------------------------
    this_month = datetime.today().strftime("%m")
    month_name =datetime.today().strftime("%b")
    page_type = "this"
    members = []

    if req.method == 'POST':
        import datetime
        today = datetime.date.today()
        first = today.replace(day=1)
        lastMonth = first - datetime.timedelta(days=1)
        
        month_name =lastMonth.strftime("%b")
        page_type = "previous"
    
        this_month = lastMonth.strftime("%m")
        
    for day in Attendance.objects.all():
        if day.date.strftime("%m") == this_month:
            for member in day.members.all():
                members.append(member)
    
    all_members = list(set(members))
    toper=[]
    for member in all_members:
        toper.append({"member":member,"count":members.count(member),"counting":0})  
    top_members = sorted(toper, key=lambda d: d['count'],reverse=True)
    counting = 1
    for member in top_members:
        member["counting"] = counting
        counting += 1
    
    return render(req, 'administrator/members/achievement.html', {
        "page_name": f"Achievement of {month_name}",
        "members": top_members,
        "page_type":page_type,
        "count": count_members_page(),
    })


def expiry_members(req):

    expired = Member.objects.order_by("expiry")

    return render(req, 'administrator/members/expiry_members.html', {
        "page_name": "Expiry all",
        
        "count": count_members_page(),
        "members": expired,

    })


def expiry_today(req):
    
    today = []
    for member in Member.objects.order_by("expiry"):
        if member.expiry == datetime.date.today():
            today.append(member)

    return render(req, 'administrator/members/expiry_members.html', {
        "page_name": "Today expiry members",
        "count": count_members_page(),

        "members": today,
    })


def expiry_expired(req):
    expired = []
    for member in Member.objects.order_by("-expiry"):
        if str(datetime.date.today()-member.expiry)[0] != "-" and member.expiry != datetime.date.today():
            expired.append(member)

    return render(req, 'administrator/members/expiry_members.html', {
        "page_name": "Expired members",
        "count": count_members_page(),
        "members": expired,
    })


def expiry_reminder(req):
    reminder = []
    date = datetime.date.today()
    for i in range(20):
        date += datetime.timedelta(days=1)
        for member in Member.objects.filter(expiry=date):
            reminder.append(member)

    return render(req, 'administrator/members/expiry_members.html', {
        "page_name": "Reminder members in two days",
        "count": count_members_page(),

        "members": reminder,
    })


def members_color():

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

 