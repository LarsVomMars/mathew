from Cython.Build import cythonize
from setuptools import setup, Extension

extensions = [
    Extension("primes", ["cython/prime.pyx"]),
    Extension("helper", ["cython/helper.pyx"]),
    Extension("linalg", ["cython/linalg.pyx"])
]

setup(
    name="mathew",
    ext_modules=cythonize("cython/*.pyx")  # Might use extensions idk
)
