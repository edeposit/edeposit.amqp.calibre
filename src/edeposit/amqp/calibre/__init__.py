#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
#= Imports ====================================================================
from collections import namedtuple

import sh


#= Variables ==================================================================


#= Functions & objects ========================================================
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


class ConversionRequest(namedtuple("ConversionRequest", ["input_type",
                                                         "output_type",
                                                         "data"])):
    def __init__(self, input_type, output_type, data):
        if input_type not in INPUT_FORMATS:
            raise ValueError("Unsupported input type!")

        if output_type not in OUTPUT_FORMATS:
            raise ValueError("Unsupported output type!")

        if input_type == output_type:
            raise ValueError("Input and output types are the same.")


class ConversionResponse(namedtuple("ConversionResponse", ["type",
                                                           "data"])):
    pass


def reactToAMQPMessage(message, response_callback, UUID):
    pass


# TESTs
c = ConversionRequest("epub", "pdf", "xexexe")
print c