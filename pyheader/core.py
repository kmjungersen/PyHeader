import re


class CSSFile():

    def __init__(self, path):

        self.path = path

    def __str__(self):

        base_string = '<link href="{path}" rel="stylesheet" type="text/css">'

        link = base_string.format(
            path=self.path,
        )

        return link


class JSFile():

    def __init__(self, path):

        self.path = path

    def __str__(self):

        base_string = '<script src="{path}"></script>'

        script = base_string.format(
            path=self.path,
        )

        return script


class DjangoStaticFileToken():

    def __init__(self, *args):

        pass

    def __str__(self):

        token = '{% load staticfiles %}'

        return token


class Misc():

    def __init__(self, string):

        self.string = string

    def __str__(self):

        return self.string