from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

class EventSource(object):

    def parse(self, source):
        self.data = ''
        self.type = None
        self.id = None
        self.extra = ''

        dispatch = False
        lines = source.splitlines()
        for line in lines:
            if dispatch:
                self.extra += line + '\n'
                continue
            if not line:
                dispatch = True
                continue

            field, value = line.split(':', 1)
            if value[0] == ' ':
                value = value[1:]

            if field == 'data':
                self.data += value + '\n'
            elif field == 'event':
                self.type = value
            elif field == 'id':
                self.id = value

        self.data = self.data[:-1]
        return Event(self.id, self.type, self.data), self.extra

