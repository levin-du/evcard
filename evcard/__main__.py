# -*- coding: utf-8 -*-

"""Allow evcard to be executable through `python -m evcard`."""

from __future__ import absolute_import

from .cli import main

if __name__ == "__main__":  # pragma: no cover
    main(prog_name="evcard")



