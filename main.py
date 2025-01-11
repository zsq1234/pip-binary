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

sys.stderr.write(f"Main: {sys.argv}\n")
sys.stderr.write(f"Main: {len(sys.argv)}\n")
sys.stderr.write(f"Main: {sys.argv[1]}\n")

if len(sys.argv) > 1 and sys.argv[1].endswith('.py'):
    path = sys.argv[1]
    sys.stderr.write(f"Main: run {path}\n")
    sys.argv = sys.argv[1:]
    a = runpy.run_path(path, run_name="__main__")
    sys.stderr.write(f"Main: {a}\n")
else:
    runpy.run_module("pip", run_name="__main__")
