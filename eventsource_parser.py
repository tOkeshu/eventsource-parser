from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

def parse(source):
    eid   = None
    etype = None
    data  = []
    retry = None
    extra = ''

    dispatch = False
    lines = source.splitlines()

    for line in lines:
        if dispatch:
            extra += line + '\n'
            continue
        if not line:
            dispatch = True
            continue

        field, value = line.split(':', 1)
        if value[0] == ' ':
            value = value[1:]

        if field == 'data':
            data.append(value)
        elif field == 'event':
            etype = value
        elif field == 'id':
            eid = value
        elif field == 'retry':
            retry = int(value)

    if not dispatch:
        return None, source

    if data:
        data = '\n'.join(data)

    if retry:
        if etype or data:
            extra = ('retry: %s\n\n' % retry) + extra
        else:
            etype, data = 'retry', retry

    return Event(eid, etype, data), extra

