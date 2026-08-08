# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import collect_all


APP_NAME = "BylickiLabs-Python-Reverse-Engineering-Inspector"
PROJECT_ROOT = Path(SPECPATH).resolve()


numpy_datas, numpy_binaries, numpy_hiddenimports = collect_all("numpy")
scipy_datas, scipy_binaries, scipy_hiddenimports = collect_all("scipy")

datas = []
datas += numpy_datas
datas += scipy_datas

binaries = []
binaries += numpy_binaries
binaries += scipy_binaries

hiddenimports = []
hiddenimports += numpy_hiddenimports
hiddenimports += scipy_hiddenimports


a = Analysis(
    [str(PROJECT_ROOT / "main.py")],
    pathex=[str(PROJECT_ROOT)],
    binaries=binaries,
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
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
)


coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=APP_NAME,
)