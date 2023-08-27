#!/usr/bin/env python
import re
import uuid
import warnings

warnings.warn("This package has been renamed to snowflake_uuid and will be removed shortly. Please update immediately.", DeprecationWarning, stacklevel=2)

SNOWFLAKE_FILE = '/etc/snowflake'

def snowflake(snowflake_file=SNOWFLAKE_FILE):
    """
    Get the snowflake ID from the specified file. If the file is unreadable for
    some reason (perhaps it doesn't exist), this will return None. However, if
    the first line of the file is not a UUID, we decide the file contains other
    things besides a snowflake ID and raise a ValueError.
    """
    res = None
    f = open(snowflake_file, "r")
    for line in f:
        if re.match("[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}", line.strip()) is not None:
            res = line.strip()
        else:
            # this is not a snowflake file!
            raise ValueError("The specified file doesn't appear to contain a snowflake.")
    f.close()
    return res

def _write_new_id(snowflake_file=SNOWFLAKE_FILE):
    """
    Unsafe! This erases the existing ID.
    """
    snowflake_id = str(uuid.uuid4())
    f = open(snowflake_file, "w")
    f.write(snowflake_id + "\n")
    f.close()
    return snowflake_id

def make_snowflake(snowflake_file=SNOWFLAKE_FILE):
    """
    If a snowflake ID exists, returns it. Otherwise, creates one.
    """
    try:
        current = snowflake(snowflake_file)
    except IOError as e:
        if e.errno == 2:
           current = None # if no file exists, we'll create it.
        else:
            raise # but if something else happens, fail

    if not current:
        _write_new_id(snowflake_file)
    return snowflake(snowflake_file)
