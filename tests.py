from unittest import TestCase, main
from eventsource_parser import EventSource, Event

class EventSourceTests(TestCase):

    def testParseData(self):
        ev = EventSource()
        event, extra = ev.parse("data:somedata\n\n")
        self.assertEqual(event, Event(None, None, 'somedata'))
        self.assertEqual(extra, '')

    def testParseMultiLinedata(self):
        ev = EventSource()
        event, extra = ev.parse("data:some\ndata:data\n\n")
        self.assertEqual(event, Event(None, None, 'some\ndata'))
        self.assertEqual(extra, '')

main()

