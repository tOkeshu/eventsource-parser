from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

class EventSource(object):

    def parse(self, source):
        data = ''
        event_type = None

        for line in source.splitlines():
            if line.startswith('data:'):
                data += line[6:] if line[5] is ' ' else line[5:]
                data += '\n'
            elif line.startswith('event:'):
                event_type = line[7:] if line[6] is ' ' else line[6:]

        data = data[:-1]
        return Event(None, event_type, data), ''

