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

    def testParseType(self):
        ev = EventSource()
        event, extra = ev.parse("event: event-type\ndata: somedata\n\n")
        self.assertEqual(event, Event(None, "event-type", "somedata"))
        self.assertEqual(extra, '');

    def testParseId(self):
        ev = EventSource()
        event, extra = ev.parse("id: 1234\ndata: somedata\n\n")
        self.assertEqual(event, Event("1234", None, "somedata"))
        self.assertEqual(extra, '');

main()

