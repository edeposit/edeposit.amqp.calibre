#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
#= Imports ====================================================================
from collections import namedtuple


#= Variables ==================================================================
# see for details
# http://manual.calibre-ebook.com/faq.html#what-formats-does-app-support-conversion-to-from
INPUT_FORMATS = [
    "cbz",
    "cbr",
    "cbc",
    "chm",
    "djvu",
    "docx",
    "epub",
    "fb2",
    "html",
    "htmlz",
    "lit",
    "lrf",
    "mobi",
    "odt",
    "pdf",
    "prc",
    "pdb",
    "pml",
    "rb",
    "rtf",
    "snb",
    "tcr",
    "txt",
    "txtz"
]

OUTPUT_FORMATS = [
    "azw3",
    "epub",
    "fb2",
    "oeb",
    "lit",
    "lrf",
    "mobi",
    "htmlz",
    "pdb",
    "pml",
    "rb",
    "pdf",
    "rtf",
    "snb",
    "tcr",
    "txt",
    "txtz"
]


#= Functions & objects ========================================================
class ConversionRequest(namedtuple("ConversionRequest", ["input_format",
                                                         "output_format",
                                                         "b64_data"])):
    """
    Args:
        input_format (str): see INPUT_FORMATS for list of valid formats
        output_format (str): see OUTPUT_FORMATS for list of valid formats
        b64_data (base64 str): base64 encoded file
    """
    def __init__(self, input_format, output_format, b64_data):
        if input_format not in INPUT_FORMATS:
            raise ValueError("Unsupported input format!")

        if output_format not in OUTPUT_FORMATS:
            raise ValueError("Unsupported output format!")

        if input_format == output_format:
            raise ValueError("Input and output formats are the same.")


class ConversionResponse(namedtuple("ConversionResponse", ["format",
                                                           "b64_data",
                                                           "protocol"])):
    """
    Args:
        type (str): see OUTPUT_FORMATS for details
        b64_data (base64 str): base64 encoded converted data
        protocol (str): protocol of the conversion
    """
    pass


def reactToAMQPMessage(message, response_callback, UUID):
    pass
