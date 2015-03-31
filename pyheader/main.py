import os
import re

#TODO - if .header file exists, use that, but otherwise default to another one
from pyheader.local import HTML_HEADER
from pyheader.core import *
import ipdb


class Header():

    def __init__(self, config):

        ipdb.set_trace()

        self.header = '\n\n'

        for cfg_line in config:

            item_instance = cfg_line[0]
            items = cfg_line[1]

            if len(items) > 0:

                for item in items:

                    line = item_instance(item)

                    self.header += str(line) + '\n'

            else:

                line = item_instance()

                self.header += str(line) + '\n'

            self.header += '\n'

    def __str__(self):

        return self.header


if __name__ == '__main__':

    base_path = os.getcwd() + '/'

    #TODO - add support for changing the directory in which this is run
    path = base_path

    cfg = HTML_HEADER

    file_list = os.listdir(path)

    header = Header(cfg)

    for file in file_list:

        if file.endswith('.html'):

            with open(path+file, 'r+') as f:

                original = f.read()

                new_header = 'START#-->{header}<!--#HEADER'.format(
                    header=header,
                )

                modified = re.sub(r'(?s)START\#-->(.*?)<!--\#HEADER', new_header, original)

                f.seek(0)
                f.write(modified)
                f.truncate()
