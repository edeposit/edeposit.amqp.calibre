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
class ConversionRequest(namedtuple("ConversionRequest", [])):
    pass

class ConversionResponse(namedtuple("ConversionResponse", [])):
    pass


def reactToAMQPMessage(message, response_callback, UUID):
    pass
