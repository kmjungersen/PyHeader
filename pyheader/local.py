##### foo

from pyheader.core import *

HTML_HEADER = [
    (DjangoStaticFileToken, []),
    (CSSFile, [
        "{% static 'inventory/site.css' %}",
        "//maxcdn.bootstrapcdn.com/bootswatch/3.3.4/flatly/bootstrap.min.css",
    ]),
    (JSFile, [
        "https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js",
        "http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js",
        "{% static 'inventory/elements.js' %}",
    ]),
]