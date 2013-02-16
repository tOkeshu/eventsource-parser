EventSource Parser
==================

A framework agnostic EventSource Parser.

    >>> source =
    """
    id: 1
    event: chat
    data: hey, how are you?

    id: 2
    event: chat
    data: fine, thanks you

    :ping
    """
    >>> ev = EventSource
    >>> event, rest = ev.parse(source)
    >>> event
    Event(1, 'chat', 'hey, how are you?')
    >>> rest
    "id: 2\nevent: chat\ndata: fine, thanks you\n\n:ping\n"
    >>> event, rest = ev.parse(rest)
    >>> event
    Event(2, 'chat', 'fine, thanks you')
    >>> rest
    ":ping\n"
    >>> event, rest = ev.parse(rest)
    >>> event
    None
    >>> rest
    ""

License
-------

Licensed under the Apache License, Version 2.0.

