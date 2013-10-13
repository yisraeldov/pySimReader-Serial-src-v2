from distutils.core import setup
import py2exe

setup(
    windows=[
    {
    "script": "pySimReader.py",
    "icon_resoureces":[(1, "PYSIM.ico")]
    }
    ],
    options = {'py2exe': {'bundle_files': 1}},
    zipfile = None,

    )
