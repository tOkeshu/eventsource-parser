# encoding: utf-8
from unittest import TestCase, main
from eventsource_parser import Event, parse

class EventSourceTests(TestCase):

    def testParseData(self):
        event, extra = parse("data:somedata\n\n")
        self.assertEqual(event, Event(None, None, 'somedata'))
        self.assertEqual(extra, '')

    def testParseMultiLinedata(self):
        event, extra = parse("data:some\ndata:data\n\n")
        self.assertEqual(event, Event(None, None, 'some\ndata'))
        self.assertEqual(extra, '')

    def testParseType(self):
        event, extra = parse("event: event-type\ndata: somedata\n\n")
        self.assertEqual(event, Event(None, "event-type", "somedata"))
        self.assertEqual(extra, '');

    def testParseId(self):
        event, extra = parse("id: 1234\ndata: somedata\n\n")
        self.assertEqual(event, Event("1234", None, "somedata"))
        self.assertEqual(extra, '');

    def testParseMultipleEvents(self):
        event, extra = parse("data: an event\n\ndata: another event\n\n")
        self.assertEqual(event, Event(None, None, "an event"))
        self.assertEqual(extra, 'data: another event\n\n');
        event, extra = parse(extra)
        self.assertEqual(event, Event(None, None, "another event"))
        self.assertEqual(extra, '');

    def testRetryParsing(self):
        event, extra = parse("retry: 10\ndata: an event\n\ndata: last event\n\n")
        self.assertEqual(event, Event(None, None, "an event"))
        self.assertEqual(extra, 'retry: 10\n\ndata: last event\n\n');
        event, extra = parse(extra)
        self.assertEqual(event, Event(None, 'retry', 10))
        self.assertEqual(extra, 'data: last event\n\n');

    def testIncompleteEvent(self):
        event, extra = parse("data: miss an empty line to dispatch\n")
        self.assertEqual(event, None)
        self.assertEqual(extra, "data: miss an empty line to dispatch\n")

    def testEmptyFields(self):
        event, extra = parse("nothing")
        self.assertEqual(event, None)
        self.assertEqual(extra, "nothing")

    def testUnicode(self):
        event, extra = parse(u"data: cet été il a fait beau à Lyon\n\n")
        self.assertEqual(event, Event(None, None, u"cet été il a fait beau à Lyon"))
        self.assertEqual(extra, u"")

    def testEmptyEvent(self):
        event, extra = parse(":comment\n\ndata: an event\n\n")
        self.assertEqual(event, None)
        self.assertEqual(extra, "data: an event\n\n")

main()

