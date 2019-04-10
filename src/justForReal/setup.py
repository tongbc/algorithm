from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

filename = 'test'
full_filename = 'test.pyx'

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension(filename, [full_filename])]
)
