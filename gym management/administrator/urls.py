from django.urls import path
from . import views
from .all_views import member,enquirys,attendance,history,notes

urlpatterns = [
    path('',views.home,name='main'),
    path('fees',views.fees,name='fees'),
    path('payment',views.payment,name='payment'),

    path('attendance_home',attendance.attendance_home,name='attendance_home'),
    path('list_attendance',attendance.list_attendance,name='list_attendance'),
    path('view_attendance_day/<str:attendance_id>/',attendance.view_attendance_day,name='view_attendance_day'),
    path('take_attendance',attendance.take_attendance,name='take_attendance'),
    path('take_attendance_all',attendance.take_attendance_all,name='take_attendance_all'),
    path('choice_attendance/<str:member_id>/',attendance.choice_attendance,name='choice_attendance'),
    path('absent_members',attendance.absent_members,name='absent_members'),




    path('enquirys',enquirys.enquirys,name='enquirys'),
    path('add_enquiry',enquirys.add_enquiry,name='add_enquiry'),
    path('delete_enquiry/<str:enquiry_id>/',enquirys.delete_enquiry,name='delete_enquiry'),
    path('update_enquiry',enquirys.update_enquiry,name='update_enquiry'),



    # path('enquirys_lists',enquirys.enquirys_lists,name='enquirys_today'),

    path('enquirys_today',enquirys.enquirys_today,name='enquirys_today'),
    path('enquirys_expired',enquirys.enquirys_expired,name='enquirys_expired'),
    path('enquirys_reminder',enquirys.enquirys_reminder,name='enquirys_reminder'),
    path('enquirys_date_search',enquirys.enquirys_date_search,name='enquirys_date_search'),
    
    





    # path('add_member/<str:enquiry_id>/',member.add_member,name='add_member'),
    path('add_member',member.add_member,name='add_member'),
    path('members',member.members,name='members'),
    path('member/<str:member_id>/',member.member,name='member'),
    path('member_login',member.member_login,name='member_login'),
    path('edit_member',member.edit_member,name='edit_member'),
    path('update_package',member.update_package,name='update_package'),
    
    path('hold_member',member.hold_member,name='hold_member'),
    path('hold_member_list',member.hold_member_list,name='hold_member_list'),
    path('achievement',member.achievement,name='achievement'),
    
 
 
 
    
    path('expiry_members',member.expiry_members,name='expiry_members'),
    path('expiry_today',member.expiry_today,name='expiry_today'),
    path('expiry_expired',member.expiry_expired,name='expiry_expired'),
    path('expiry_reminder',member.expiry_reminder,name='expiry_reminder'),
    
    path('history',history.history,name='history'),
    
    path('notes',notes.notes,name='notes'),
    path('add_note',notes.add_note,name='add_note'),
    path('delete_note/<str:note_id>/',notes.delete_note,name='delete_note'),
    
    
]
