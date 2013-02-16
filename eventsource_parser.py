from collections import namedtuple


Event = namedtuple('Event', ['id', 'type', 'data'])

class EventSource(object):

    def parse(self, source):
        return Event(None, None, 'somedata'), ''

