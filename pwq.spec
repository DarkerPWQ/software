# -*- mode: python -*-
a = Analysis(['pwq.py'],
             pathex=['D:\\realpro'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pwq.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='D:\\01.ico')
