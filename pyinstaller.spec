# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules, collect_all
from pprint import pprint
import certifi

cert_path = certifi.where()

datas = [('./pip', './pip'), (cert_path, './certifi')]
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

setuptools_info = collect_all('setuptools')

datas += setuptools_info[0]
binaries += setuptools_info[1]
hiddenimports += setuptools_info[2]

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
