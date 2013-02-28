# encoding: utf-8

from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

def parse(source):
    eid   = None
    etype = None
    data  = []
    retry = None
    extra = ''

    if not isinstance(source, unicode):
        source = unicode(source, 'utf-8')

    dispatch = False
    cursor   = 0
    lines    = source.splitlines()

    for line in lines:
        if not line:
            dispatch = True
            extra = source[cursor+1:]
            break

        if not ':' in line:
            field, value = line, ''
        else:
            field, value = line.split(':', 1)

        if value and value[0] == ' ':
            value = value[1:]

        if field == 'data':
            data.append(value)
        elif field == 'event':
            etype = value
        elif field == 'id':
            eid = value
        elif field == 'retry':
            retry = int(value)

        cursor += len(line) + 1

    if not dispatch:
        return None, source
    if (eid, etype, data, retry) == (None, None, [], None):
        return None, extra

    if data:
        data = '\n'.join(data)

    if retry:
        if etype or data:
            extra = (u'retry: %s\n\n%s' % (retry, extra))
        else:
            etype, data = 'retry', retry

    return Event(eid, etype, data), extra

