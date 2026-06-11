# build.spec — PyInstaller configuration for Choice MFB Credit App
#
# HOW TO USE:
#   pyinstaller build.spec
#
# This creates a "dist/ChoiceMFB_Credit" folder containing everything.
# That folder is then wrapped into a .exe installer using Inno Setup.

import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Collect all data files that streamlit and plotly need
datas = []
datas += collect_data_files('streamlit')
datas += collect_data_files('plotly')
datas += collect_data_files('sklearn')
datas += collect_data_files('altair')

# Add the app files
datas += [
    ('choice_mfb_credit_app_v2.py', '.'),
    ('scorecard_model.pkl',      '.'),
    ('ews_model.pkl',            '.'),
]

# Hidden imports that PyInstaller might miss
hiddenimports = (
    collect_submodules('streamlit') +
    collect_submodules('sklearn') +
    collect_submodules('plotly') +
    [
        'sklearn.utils._cython_blas',
        'sklearn.neighbors.typedefs',
        'sklearn.neighbors.quad_tree',
        'sklearn.tree._utils',
        'sklearn.utils._weight_vector',
        'sklearn.ensemble._gb_losses',
        'joblib',
        'openpyxl',
        'pandas',
        'numpy',
        'plotly.express',
        'plotly.graph_objects',
    ]
)

block_cipher = None

a = Analysis(
    ['launcher.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'PyQt5', 'PyQt6', 'wx', 'IPython'],
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
    name         = 'ChoiceMFB_Credit',
    debug        = False,
    bootloader_ignore_signals = False,
    strip        = False,
    upx          = True,
    console      = False,             # No black console window
    disable_windowed_traceback = False,
    target_arch  = None,
    codesign_identity = None,
    entitlements_file = None,
    icon         = 'icon.ico',        # Optional: add your bank's icon
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip        = False,
    upx          = True,
    upx_exclude  = [],
    name         = 'ChoiceMFB_Credit',
)
