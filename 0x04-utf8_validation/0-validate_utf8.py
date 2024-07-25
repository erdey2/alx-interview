#!/usr/bin/python3
""" utf-8 validation module """


def validUTF8(data):
    """ a function to validate utf-8 """
    try:
        maskeddata = [n & 255 for n in data]
        bytes(maskeddata).decode("UTF-8")
        return True
    except Exception:
        return False
