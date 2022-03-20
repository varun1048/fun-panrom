from django.shortcuts import render
from ..models import History

def history(req):
    page_name = "All history"
    history = History.objects.all()[::-1]

    if req.method == 'POST':
        history = []
        page_name = "History by date"
        data = req.POST
        for hty in History.objects.filter(date__startswith=data['date']):
            history.append(hty)

    return render(req, 'administrator/history.html', {
        "page_name": page_name,
        "history": history
    })


def add_history(event, content):
    new_history = History.objects.create(event=event, content=content)
    new_history.save()

