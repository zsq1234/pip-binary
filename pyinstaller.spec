# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules
from pprint import pprint

datas = [('./pip', './pip')]
binaries = []
hiddenimports = []

hiddenimports += collect_submodules('site')
hiddenimports += collect_submodules('__future__')
hiddenimports += collect_submodules('importlib')
hiddenimports += collect_submodules('logging')
hiddenimports += collect_submodules('getpass')
hiddenimports += collect_submodules('colorsys')
hiddenimports += collect_submodules('urllib')
hiddenimports += collect_submodules('html')
hiddenimports += collect_submodules('http')
hiddenimports += collect_submodules('ipaddress')
hiddenimports += collect_submodules('mmap')
hiddenimports += collect_submodules('uuid')
hiddenimports += collect_submodules('compileall')
hiddenimports += collect_submodules('plistlib')
hiddenimports += collect_submodules('ctypes')
hiddenimports += collect_submodules('wheel')
hiddenimports += collect_submodules('setuptools')

pprint(hiddenimports)

# exit()

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pip',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# pprint(a.datas)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pip',
)
