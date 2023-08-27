snowflake_uuid: Simple Persistent System-wide Unique IDs
========================================================

I've often found myself needing to have a per-machine unique identifier, but
actually getting one of these is harder than it should be. You can't just use
the MAC address, since those aren't guaranteed to be unique, especially when
you're working with a batch of cheap embedded devices. While not rocket
science, it's also not trivial to get the MAC address of a box sometimes: which
interface to use? What if you change network cards? What if you have to spoof a
MAC address? POSIX specifies gethostid(1), but on Linux the man page notes
under "Bugs" that "It is impossible to ensure that the identifier is globally
unique." Indeed, my laptop and my work computer have the same hostid value.

snowflake_uuid is a trivial wrapper around Python's uuid library to create a
persistent, per-machine UUID (called a 'snowflake', not to be confused with the
[data warehousing project](https://www.snowflake.com)) and give you a nice API
to mess with it. Usage is simple:

    >>> import snowflake_uuid
    >>> snowflake_uuid.snowflake()
    '7232c1c3-f6d1-4aec-bedd-c7e4c10dc8d3'

There's also a script that can be run from the command line:

    $ snowflake
    7232c1c3-f6d1-4aec-bedd-c7e4c10dc8d3

Installation and Setup
----------------------
To generate a machine's snowflake ID, just install snowflake:

    $ pip install snowflake_uuid

Or from source:

    $ python setup.py install

The machine's snowflake is saved in /etc/snowflake during installation. Any
user can read this file, but only users with root access can modify it. You can
also generate other snowflakes in other locations, so each user (or
application) can make their own snowflakes.

Of course, you can do all this in Python too:

    >>> import snowflake_uuid
    >>> snowflake_uuid.make_snowflake(snowflake_file='foo')
    ee2b1891-ccd3-4a23-9246-4ce40d20e740
    >>> snowflake_uuid.snowflake(snowflake_file='foo')
    ee2b1891-ccd3-4a23-9246-4ce40d20e740

Limitations
-----------
Right now, snowflake_uuid only works on Unix-y systems.

License
-------
Copyright (c) 2023, Shaddi Hasan
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
