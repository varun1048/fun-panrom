from .models import Enquirys, Member, Attendance,Absentees
import datetime


def enquirys_info():

    today = []
    for enquiry in Enquirys.objects.order_by("joining_date"):
        if enquiry.joining_date == datetime.date.today():
            today.append(enquiry)

    expired = []
    for enquiry in Enquirys.objects.order_by("joining_date"):
        if str(datetime.date.today()-enquiry.joining_date)[0] != "-" and enquiry.joining_date != datetime.date.today():
            expired.append(enquiry)

    reminder = []
    date = datetime.date.today()
    for i in range(20):
        date += datetime.timedelta(days=1)
        for enquiry in Enquirys.objects.filter(joining_date=date):
            reminder.append(enquiry)

    return {
        "total": Enquirys.objects.count(),
        "today": len(today),
        "expired": len(expired),
        "reminder": len(reminder),
    }

def hold_info():
    today = 0
    expired = 0
    reminder = 0
    for member in Member.objects.filter(hold=True) and Member.objects.filter(hold_date=datetime.date.today()) :
        today += 1

    for member in Member.objects.filter(hold=True):
        try:
            if str(datetime.date.today()-member.hold_date)[0] != "-" and member.hold_date != datetime.date.today():
                expired += 1
                
        except:
            pass

    for member in Member.objects.filter(hold=True):
        try:
            reminder_count = str(
                datetime.date.today()-member.hold_date)[0:3]
            if reminder_count == '-1 ' or reminder_count == '-2 ' or reminder_count == '-3 ':
                reminder += 1
        except:
            pass
    
    

    return {
        "total": Member.objects.filter(hold=True).count(),
        "today": today,
        "expired": expired,
        "reminder": reminder,
    }
        
def expiry_info():
    today = 0
    expired = 0
    reminder = 0

    for member in Member.objects.order_by("expiry"):
        if member.expiry == datetime.date.today():
            today += 1

    
    for member in Member.objects.order_by("-expiry"):
        if str(datetime.date.today()-member.expiry)[0] != "-" and member.expiry != datetime.date.today():
            expired += 1 



    date = datetime.date.today()
    for i in range(20):
        date += datetime.timedelta(days=1)
        for member in Member.objects.filter(expiry=date):
            reminder += 1



    return {
        "today": today,
        "expired": expired,
        "reminder": reminder,
    }

def attendance_info():
    atd = None
    try:
        atd = Attendance.objects.get(date=datetime.date.today())
    except:
        atd = Attendance.objects.create()

    all_shift = 0
    for member in Member.objects.filter(hold=False):
        if member  not in atd.members.all()  and  member not in atd.absentees.all() and member not in Absentees.objects.all():

            all_shift += 1

        # "today_Present":today_attendance_obj().members.count(),
        # "today_absentees":today_attendance_obj().absentees.count(),
        # "toUpdate":len(toUpdate_members()),
        # "absentees_count":Absentees.objects.count(),
    return {
        # "all_shift": all_shift,
        "today_Present": atd.members.count(),
        "today_absentees": atd.absentees.count(),
        "to_update":all_shift,
        
        "absentees_count":Absentees.objects.count(),
        

    }

def today()->dict:
    enquirys = enquirys_info()
    expiry = expiry_info()
    hold = hold_info()
    return  {
        "total" : enquirys["today"] + expiry["today"] + hold["today"], 
        "total_enquirys_expiry" : enquirys["today"] + expiry["today"] , 
        "enquirys":enquirys["today"],
        "expiry":expiry["today"],
        "hold":hold["today"],
        }

def absentees_count():
    count = 0
    for member in Absentees.objects.all():
        if member.days_count > 0:
            count +1
            
    return count

def achievement():
    from datetime import datetime
    this_month = datetime.today().strftime("%m")
    month_name =datetime.today().strftime("%b")
    members = []

        
    for day in Attendance.objects.all():
        if day.date.strftime("%m") == this_month:
            for member in day.members.all():
                members.append(member)
    
    all_members = list(set(members))
    toper=[]
    for member in all_members:
        toper.append({"member":member,"count":members.count(member)})  
    top_members = sorted(toper, key=lambda d: d['count'],reverse=True)[:10]

    
    return {"top_members":top_members,"month_name":month_name}

def count_main() -> dict:
    return {
    "today":today(),
    "members": Member.objects.all().count(),
    "hold": hold_info(),
    "expiry": expiry_info(),
    "enquiry": enquirys_info(),
    "attendance":attendance_info(),
    "absentees":Absentees.objects.count(),
    "achievement":achievement,
}
    
def count_members_page() -> dict:
    
    return {
    "today":today(),
    "members": Member.objects.all().count(),
    "hold": hold_info(),
    "expiry": expiry_info(),
    "name":"members"
}
    
    
    
def count_enquiry_page() -> dict:
    return {
    "today":today(),
    "enquiry": enquirys_info(),
    "name":"enquiry"
}

def count_expiry_page() -> dict:
    return {
    "today":today(),
    "enquiry": expiry_info(),
    "name":"expiry"
}


def count_attendance_page() -> dict:
    return {
    "today":today(),
    "attendance":attendance_info(),
    "absentees":Absentees.objects.all().count(),
}
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
