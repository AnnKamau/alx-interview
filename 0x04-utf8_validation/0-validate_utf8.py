#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding.
"""
def validUTF8(data):
    """
    Validates if a list of integers represents valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Get only the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Check how many bytes the current character consists of
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte characters are allowed to be one byte
            if num_bytes == 0:
                continue

            # UTF-8 characters are between 1 and 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Else we are dealing with a continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes to process
        num_bytes -= 1

    return num_bytes == 0
