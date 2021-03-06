#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
"""
AMQP communication wrapper for calibre's ``ebook-convert`` program.
"""
# Imports =====================================================================
from calibre import convert

from structures import ConversionRequest
from structures import ConversionResponse


# Functions ===================================================================
def _instanceof(instance, class_):
    """Check type by matching ``.__name__``."""
    return type(instance).__name__ == class_.__name__


def reactToAMQPMessage(message, send_back):
    """
    React to given (AMQP) message. `message` is usually expected to be
    :py:func:`collections.namedtuple` structure filled with all necessary data.

    Args:
        message (\*Request class): only :class:`.ConversionRequest` class is
                                   supported right now

        send_back (fn reference): Reference to function for responding. This is
                  useful for progress monitoring for example. Function takes
                  one parameter, which may be response structure/namedtuple, or
                  string or whatever would be normally returned.

    Returns:
        ConversionResponse: response filled with data about conversion and\
                            converted file.

    Raises:
        ValueError: if bad type of `message` structure is given.
    """
    if _instanceof(message, ConversionRequest):
        return convert(
            message.input_format,
            message.output_format,
            message.b64_data
        )

    raise ValueError(
        "Unknown type of request: '" + str(type(message)) + "'!"
    )
