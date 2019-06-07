from django.shortcuts import render
from appointment.models import Doctor, Reception


def index(req):
    """Индексная страница выбора врача"""
    return render(req, 'select-doc.html', context={'doctors': Doctor.objects.all()})


def make_record(req):
    """Страница записис к врачу"""
    from datetime import datetime, timedelta, date

    try:
        doc_id = int(req.GET.get('doc_id', ''))
    except ValueError:
        print('Wrong doc_id param, must be int')
        return

    """Получим записи о враче"""
    doc_query = Doctor.objects.get(id=doc_id)

    """И тут фила, ярофть и мофь питона во всей красе, отнимем 1 час от графика доктора для корректного
    ограничения времени записи на стороне клиента. Худшего костыля я не видел,
    но питон не может от времени отнять время просто так."""
    end_work_time = (datetime.combine(date(1, 1, 1), doc_query.end_work_time) - timedelta(hours=1)).time()

    all_record_to_doc = doc_query.records.all()

    return render(req, 'reception.html', context={
        'current_doc': doc_query,
        'end_work_time': end_work_time,
        'doc_records': all_record_to_doc
    })


def add_record(req):
    from datetime import datetime, timedelta, date
    from django.http import HttpResponse

    if req.method == 'POST':
        fio = req.POST.get('fio', False)
        record_date = req.POST.get('date', False)
        record_time = req.POST.get('time', False)

        record_date_time = datetime.strptime(record_date + ' ' + record_time, '%Y-%m-%d %H:%M')

        if not fio or not record_date or not record_time:
            HttpResponse('Ошибка! Все поля формы обязательны')

        print(date.today())

        # if date.today() > date(date):
        #     HttpResponse('Ошибка! Дата должна быть не в прошлом')

    return render(req, 'done.html')
