#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Method that determines if a given data set represents a valid
    UTF-8 encoding.
    """
    numberbytes = 0

    data_1 = 1 << 7
    data_2 = 1 << 6

    for i in data:

        byte = 1 << 7

        if numberbytes == 0:

            while byte & i:
                numberbytes += 1
                byte = byte >> 1

            if numberbytes == 0:
                continue

            if numberbytes == 1 or numberbytes > 4:
                return False

        else:
            if not (i & data_1 and not (i & data_2)):
                    return False

        numberbytes -= 1

    if numberbytes == 0:
        return True

    return False
