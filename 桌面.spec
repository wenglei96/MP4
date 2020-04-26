# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['视频下载\\桌面.py'],
             pathex=['视频下载\\web.py', '视频下载\\main.py', '视频下载\\dirbc.py', '视频下载\\m3u8.py', '视频下载\\delete.py', 'D:\\Develop_Python\\MP4'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='桌面',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='桌面')
