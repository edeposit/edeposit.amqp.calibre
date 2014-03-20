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


class ConversionRequest(namedtuple("ConversionRequest", [])):
    pass


class ConversionResponse(namedtuple("ConversionResponse", [])):
    pass



def reactToAMQPMessage(message, response_callback, UUID):
    pass
