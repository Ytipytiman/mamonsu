# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['mamonsu_win32.py'],
             pathex=['C:\\Projects\\Extensions\\mamonsu'],
             binaries=[],
             datas=[],
             hiddenimports=[
                'mamonsu.plugins.pgsql.archive_command',
                'mamonsu.plugins.pgsql.bgwriter',
                'mamonsu.plugins.pgsql.cfs',
                'mamonsu.plugins.pgsql.checkpoint',
                'mamonsu.plugins.pgsql.connections',
                'mamonsu.plugins.pgsql.databases',
                'mamonsu.plugins.pgsql.health',
                'mamonsu.plugins.pgsql.instance',
                'mamonsu.plugins.pgsql.oldest',
                'mamonsu.plugins.pgsql.pg_buffercache',
                'mamonsu.plugins.pgsql.pg_locks',
                'mamonsu.plugins.pgsql.pg_stat_statement',
                'mamonsu.plugins.pgsql.pg_wait_sampling',
                'mamonsu.plugins.pgsql.plugin',
                'mamonsu.plugins.pgsql.pool',
                'mamonsu.plugins.pgsql.prepared_transaction',
                'mamonsu.plugins.pgsql.relations_size',
                'mamonsu.plugins.pgsql.xlog',
                'mamonsu.plugins.system.windows.cpu',
                'mamonsu.plugins.system.windows.disk_stats',
                'mamonsu.plugins.system.windows.helpers',
                'mamonsu.plugins.system.windows.memory',
                'mamonsu.plugins.system.windows.network',
                'mamonsu.lib.senders.log',
                'mamonsu.lib.senders.zbx',
                'mamonsu.tools.agent.agent',
                'mamonsu.tools.agent.start',
                'mamonsu',
                'mamonsu.plugins',
                'mamonsu.plugins.pgsql',
                'mamonsu.plugins.system.windows',
                'mamonsu.tools.agent',
                'mamonsu.tools.bootstrap',
                'mamonsu.tools.report',
                'mamonsu.tools.sysinfo',
                'mamonsu.tools.tune',
                'mamonsu.tools.zabbix_cli',
                'mamonsu.plugins.common.health'
             ],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='mamonsu',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
