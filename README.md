EventSource Parser
==================

A framework agnostic EventSource Parser.
```python
    >>> source =
    """
    id: 1
    event: chat
    data: hey, how are you?

    id: 2
    event: chat
    data: fine, thank you

    :ping
    """
    >>> from eventsource_parser import parse
    >>> event, rest = parse(source)
    >>> event
    Event(1, 'chat', 'hey, how are you?')
    >>> rest
    "id: 2\nevent: chat\ndata: fine, thank you\n\n:ping\n"
    >>> event, rest = parse(rest)
    >>> event
    Event(2, 'chat', 'fine, thank you')
    >>> rest
    ":ping\n"
    >>> event, rest = parse(rest)
    >>> event
    None
    >>> rest
    ""
```

License
-------

Licensed under the Apache License, Version 2.0.

