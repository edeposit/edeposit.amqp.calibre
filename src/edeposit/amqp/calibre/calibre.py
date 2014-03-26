#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
#= Imports ====================================================================
import sh


#= Variables ==================================================================



#= Functions & objects ========================================================
def check():
    """
    Check, if the 'ebook-convert' program is installed.

    Raises:
        UserWarning: if not.
    """
    try:
        output = sh.ebook_convert("ebook-convert", _ok_code=[1])
    except sh.CommandNotFound:
        raise UserWarning(
            "'ebook-convert' not found. Do you have callibre installed?"
        )

    if "Usage:" not in output:
        raise UserWarning(
            "'ebook-convert' reacts strangely. Post this to developers:\n" +
            output
        )


def convert(input_type, output_type, b64_data):
    pass


#= Main program ===============================================================
if __name__ == '__main__':
    check()