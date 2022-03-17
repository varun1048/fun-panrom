from django.shortcuts import render, redirect
from ..models import Notes
from ..counter import count_members_page


def notes(req):
    page_name = "Notes"

    return render(req, 'administrator/notes.html', {
        "page_name": page_name,
        "notes": Notes.objects.all()[::-1],
        "count": count_members_page(),
    })


def add_note(req):
    page_name = "Add note"
    if req.method == "POST":
        data = req.POST
        Notes.objects.create(
            title=data['title'], content=data['content']).save()
        return redirect('notes')
    return render(req, 'administrator/notes.html', {
        "page_name": page_name,

        "count": count_members_page(),
    })


def delete_note(req, note_id):
    
    try:
        Notes.objects.get(id=note_id).delete()
    except:
        pass
    
    return redirect('notes')
