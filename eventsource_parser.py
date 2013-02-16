from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

class EventSource(object):

    def __init__(self):
        self.data = ''
        self.type = None
        self.id = None

    def parse(self, source):
        for line in source.splitlines():
            if not line:
                self.data = self.data[:-1]
                return Event(self.id, self.type, self.data), ''

            field, value = line.split(':', 1)
            if value[0] == ' ':
                value = value[1:]

            if field == 'data':
                self.data += value + '\n'
            elif field == 'event':
                self.type = value
            elif field == 'id':
                self.id = value

