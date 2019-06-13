from django.shortcuts import render
from appointment.models import Doctor, Reception


def index(req):
    """Индексная страница выбора врача"""
    return render(req, 'select-doc.html', context={'doctors': Doctor.objects.all()})


def make_record(req):
    """Страница записи к врачу"""
    from datetime import timezone

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

    """Сформируем на вывод только те записи, которые еще актуальны"""
    all_record_to_doc = doc_query.records.in_bulk()
    filter_record = []
    for item, value in all_record_to_doc.items():
        if value.date > datetime.now(timezone.utc):
            filter_record.append(value)

    return render(req, 'reception.html', context={
        'current_doc': doc_query,
        'end_work_time': end_work_time,
        'doc_records': filter_record
    })


def add_record(req):
    import datetime as dt
    from django.http import HttpResponse
    from django.core.exceptions import ObjectDoesNotExist

    if req.method == 'POST':
        fio = req.POST.get('fio', False)
        record_date = req.POST.get('date', False)
        record_time = req.POST.get('time', False)
        doc_id = req.POST.get('doc_id', False)

        if not fio or not record_date or not record_time:
            return HttpResponse('Ошибка! Все поля формы обязательны.')

        if int(record_time.split(':')[1]) != 00:
            return HttpResponse('Вводимые значения записи только часы.')

        """Получим выбранную дату в формате datetime"""
        record_date_time = dt.datetime.strptime(record_date + ' ' + record_time, '%Y-%m-%d %H:%M')

        if dt.datetime.now() > record_date_time:
            return HttpResponse('Ошибка! Выбранная дата не должна быть в прошлом.')

        """Проверим введеное время на соответствие графика врача, и на свободное время"""
        curr_doc_query = Doctor.objects.get(id=doc_id)

        if record_time > str((dt.datetime.combine(dt.date(1, 1, 1), curr_doc_query.end_work_time) - dt.timedelta(hours=1)).time())\
                or record_time < str(curr_doc_query.start_work_time.strftime('%H:%M')):
            return HttpResponse('Введеное время не соответствует времени работы врача.')

        try:
            result = curr_doc_query.records.get(date=record_date_time)
        except ObjectDoesNotExist:
            result = False

        if result:
            return HttpResponse('На выбранное время уже есть запись')

        """После валидации значение, запишем к врачу"""
        Reception.objects.create(to_doc=curr_doc_query, date=record_date_time, pacient_fio=fio)

    return render(req, 'done.html')
