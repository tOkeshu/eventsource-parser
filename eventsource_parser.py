from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

class EventSource(object):

    def parse(self, source):
        self.data = []
        self.type = None
        self.id = None
        self.extra = ''
        self.retry = None

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
                self.data.append(value)
            elif field == 'event':
                self.type = value
            elif field == 'id':
                self.id = value
            elif field == 'retry':
                self.retry = int(value)

        if not dispatch:
            return None, source

        if self.data:
            self.data = '\n'.join(self.data)

        if self.retry:
            if self.type or self.data:
                self.extra = ('retry: %s\n\n' % self.retry) + self.extra
            else:
                self.type, self.data = 'retry', self.retry

        return Event(self.id, self.type, self.data), self.extra

