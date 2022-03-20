from django.shortcuts import render, redirect
from ..models import Attendance, Member, Absentees
from datetime import date, datetime
from ..counter import count_attendance_page


now_shift = "Morning" if datetime.today().strftime("%p") == 'AM' else "Evening"


def today_attendance_obj() -> Attendance:
    try:
        atd = Attendance.objects.get(date=date.today())
    except:
        atd = Attendance.objects.create()
        # for  member in Member.objects.all():
        #     atd.absentees.add(member)
    return atd

def toUpdate_members(shift=False) -> Member:
    atd = today_attendance_obj()
    members = []
    for member in Member.objects.order_by("name"):
        if member not in atd.members.all() and member not in atd.absentees.all() and member not in Absentees.objects.all() and not member.hold:
            if shift:
                members.append(member)

            elif member.shift_type == now_shift:
                members.append(member)

    return members

def attendance_home(req):

    return render(req, "administrator/attendance/attendance_home.html",
                  {
                      "page_name": "Attendance",

                      # "today_Present":today_attendance_obj().members.count(),
                      # "today_absentees":today_attendance_obj().absentees.count(),
                      # "toUpdate":len(toUpdate_members()),
                      # "absentees_count":Absentees.objects.count(),

                      "list_attendance": Attendance.objects.all()[:3:-1],
                      "count": count_attendance_page(),


                  })


def choice_attendance(req, member_id=None):
    member_id = str(member_id)
    member_id = member_id.split('_')
    # atd = Attendance.objects.get(date=date.today())
    atd = today_attendance_obj()
    # today_attendance_obj()
    member = Member.objects.get(id=member_id[1])

    # if req.method == 'POST':
    if member_id[0] == 'P':
        atd.members.add(member)
        atd.absentees.remove(member)

        try:
            Absentees.objects.get(member=member).delete()
        except:
            pass
        # try:
        #     absentees = Absentees.objects.get(member=member)
        #     if absentees.date != date.today():
        #         print(absentees.date)
        #         absentees.Present_count += 1
        #         absentees.save()

        # except:
        #     Absentees.objects.create(member=member, Present_count=1).save()

    if member_id[0] == 'A':
        atd.members.remove(member)
        atd.absentees.add(member)

        try:
            absentees = Absentees.objects.get(member=member)
            if absentees.date != date.today():
                print(absentees.date)
                absentees.days_count += 1
                absentees.save()

        except:
            Absentees.objects.create(member=member, days_count=1).save()

    # atd.absentees.remove(member)
    # atd.save()
    if member_id[2] == 'today':
        return redirect("take_attendance")
    else:
        return redirect("take_attendance_all")


def take_attendance(req):
    now_shift = "Morning" if datetime.today().strftime("%p") == 'AM' else "Evening"

    atd = today_attendance_obj()
    members = toUpdate_members()

    if req.method == 'POST':
        data = req.POST
        members = []
        now_shift = "All "
        members_all = Member.objects.filter(name__startswith=data['queries']) | Member.objects.filter(
            memberId__startswith=data['queries']) | Member.objects.filter(number__startswith=data['queries']).order_by("name")
        for member in members_all:

            if member in toUpdate_members(True):
                members.append(member)

    return render(req, "administrator/attendance/take_attendance.html",
                  {
                      "page_name": "Take attendance",
                      "attendance_date": atd.date,
                      "members": members,
                      "now_shift": now_shift,
                      "update": len(members),

                      "absentees": atd.absentees.order_by("name"),
                      "present_members": atd.members.order_by("name"),

                      "present_count": atd.members.count(),
                      "absentees_count": atd.absentees.count(),
                      "count": count_attendance_page(),



                  })


def take_attendance_all(req):
    now_shift = "All "

    atd = today_attendance_obj()
    # members = toUpdate_members()

    # for member in Member.objects.all():
    #         members.append(member)

    members = []
    for member in Member.objects.filter(hold=False).order_by("name"):
        if member not in atd.members.all() and member not in atd.absentees.all() and member not in Absentees.objects.all():
            members.append(member)

    if req.method == 'POST':
        data = req.POST
        members = []
        members_all = Member.objects.filter(name__startswith=data['queries']) | Member.objects.filter(
            memberId__startswith=data['queries']) | Member.objects.filter(number__startswith=data['queries']).order_by("name")
        
        for member in members_all:
            if member in toUpdate_members(True):
                members.append(member)

    return render(req, "administrator/attendance/take_attendance.html",
                  {
                      "page_name": "Take attendance to all",
                      "attendance_date": atd.date,
                      "members": members,
                      "now_shift": now_shift,
                      "update": len(members),

                      "absentees": atd.absentees.order_by("name"),
                      "present_members": atd.members.order_by("name"),

                      "present_count": atd.members.count(),
                      "absentees_count": atd.absentees.count(),
                      "count": count_attendance_page(),



                  })


def list_attendance(req):
    attendance_list = []

    for attendance in Attendance.objects.order_by("-date"):
        attendance_list.append({
            "date": attendance.date,
            "id": attendance.id,
            "presented": attendance.members.count(),
            "absentees": attendance.absentees.count()
        })

    if req.method == 'POST':

        data = req.POST
        try:
            attendance = Attendance.objects.get(date=data['date'])
            attendance_list = []
            attendance_list.append({
                "date": attendance.date,
                "id": attendance.id,
                "presented": attendance.members.count(),
                "absentees": attendance.absentees.count()
            })
        except:
            pass

    return render(req, 'administrator/attendance/list_attendance.html', {
        "page_name": "View attendance",
        "attendance_list": attendance_list,
        "count": count_attendance_page(),

    })


def view_attendance_day(req, attendance_id):
    atd = Attendance.objects.get(id=attendance_id)

    return render(req, 'administrator/attendance/view_attendance_day.html', {
        "page_name": str(atd.date) + " attendance",
        "members": atd.members.all(),
        "absentees": atd.absentees.all(),
        "count": count_attendance_page(),


    })


def absent_members(req):

    absentees = []
    
    for member in Absentees.objects.order_by("-days_count"):
        if member.days_count > 0:
            absentees.append(member)

    return render(req, "administrator/attendance/absent_members.html",
                  {
                      "page_name": "Absent members",
                      "absentees": absentees,
                      "count": count_attendance_page(),


                  })
