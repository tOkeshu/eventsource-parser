from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

class EventSource(object):

    def parse(self, source):
        data = ''
        for line in source.splitlines():
            if line.startswith('data:'):
                data += line[5:] + '\n'
        data = data[:-1]
        return Event(None, None, data), ''

