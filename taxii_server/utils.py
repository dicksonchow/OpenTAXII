import os
import sys
import pytz
import logging
import structlog
import urlparse

from datetime import datetime


import intelworks.logging


def get_path_and_address(domain, address):
    parsed = urlparse.urlparse(address)

    if parsed.scheme:
        return None, address
    else:
        return address, domain + address



class SimpleRenderer(object):

    def __call__(self, logger, name, event_dict):
        if 'exception' in event_dict:
            message = '\n%s' % event_dict['exception']
        else:
            message = event_dict['event']
        return '%(timestamp)s [%(logger)s] %(level)s: %(message)s' % dict(message=message, **event_dict)


def configure_logging(config):
    intelworks.logging.configure(config)


