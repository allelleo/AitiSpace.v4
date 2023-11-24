import datetime

from fastapi import APIRouter, Request

from spacelog.models import Log
from spacelog.schemas import LogInput

api_v1 = APIRouter()

server_time = datetime.timedelta(hours=3)


@api_v1.post('/log')
async def new_log(r: Request, data: LogInput):
    new = await Log.create(
        project=data.project,
        service=data.service,
        level=data.level,
        message=data.message,
        code=data.code
    )
    return new.id


async def get_info_logs(time):
    time = str(time - server_time)[:-9]
    logs = await Log.filter(time_created__startswith=time, level='INFO')
    return len(logs)


async def get_warning_logs(time):
    time = str(time - server_time)[:-9]
    logs = await Log.filter(time_created__startswith=time, level='WARNING')
    return len(logs)


async def get_critical_logs(time):
    time = str(time - server_time)[:-9]
    logs = await Log.filter(time_created__startswith=time, level='CRITICAL')
    return len(logs)


@api_v1.get('/log_count')
async def log_count(r: Request):
    now = datetime.datetime.now()
    labels = [now]
    for i in range(1, 60 + 1):
        labels.append(now - datetime.timedelta(minutes=i))
    labels.reverse()

    info = []
    for i in labels:
        info.append(await get_info_logs(i))

    warning = []
    for i in labels:
        warning.append(await get_warning_logs(i))
    critical = []
    for i in labels:
        critical.append(await get_critical_logs(i))
    l = []
    for i in labels:
        l.append(
            f"{i.hour if len(str(i.hour)) == 2 else '0' + str(i.hour)}:{i.minute if len(str(i.minute)) == 2 else '0' + str(i.minute)}"
        )
    data = {
        'labels': l,
        'datasets': [
            {
                'data': info,
                'label': "INFO",
                'borderColor': "#3e95cd",
                'fill': False
            }, {
                'data': warning,
                'label': "WARNING",
                'borderColor': "#FFFF00",
                'fill': False
            }, {
                'data': critical,
                'label': "CRITICAL",
                'borderColor': "#FF0000",
                'fill': False
            }
        ]
    }
    return data
