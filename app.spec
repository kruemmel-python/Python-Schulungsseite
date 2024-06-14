# app.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['F:\\Flask_Webserver_Python'],
    binaries=[],
    datas=[
        ('F:\\Flask_Webserver_Python\\static', 'static'),
        ('F:\\Flask_Webserver_Python\\templates', 'templates'),
        ('F:\\Flask_Webserver_Python\\arduino', 'arduino'),
        ('F:\\Flask_Webserver_Python\\lua', 'lua'),
        ('F:\\Flask_Webserver_Python\\quiz.db', '.')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['PyQt5'],  # Schließe PyQt5 aus
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
