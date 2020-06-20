from setuptools import setup


long_description = open("README.md", "r").read()

setup(
    name='mathew',
    version='0.0.1',
    description='My personal universal math lib',
    url='https://github.com/larsvommars/mathlib',
    author='LarsVomMars',
    author_email='dev@kroenner.eu',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['mathew'],
    zip_save=False
)
