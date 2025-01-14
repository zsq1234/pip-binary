#!/usr/bin/env python
import sys

# /!\ This version compatibility check section must be Python 2 compatible. /!\
PYTHON_REQUIRES = (3, 8)

if PYTHON_REQUIRES != (0, 0):
    def version_str(version):  # type: ignore
        return ".".join(str(v) for v in version)

    if sys.version_info[:2] < PYTHON_REQUIRES:
        raise SystemExit(
            "This version of pip does not support python " +
            version_str(sys.version_info[:2]) +
            " (requires >= " +
            version_str(PYTHON_REQUIRES) +
            ")."
        )
# /!\ Version check done. We can use Python 3 syntax now. /!\

import os
import runpy

lib = os.path.dirname(__file__)
sys.path.insert(0, lib)

if getattr(sys, 'frozen', False):
    os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(sys._MEIPASS, 'certifi', 'cacert.pem')

if len(sys.argv) > 1 and sys.argv[1].endswith('.py'):
    path = sys.argv[1]
    sys.argv = sys.argv[1:]
    runpy.run_path(path, run_name="__main__")
else:
    runpy.run_module("pip", run_name="__main__")
