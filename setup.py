from setuptools import setup


long_description = open("README.md", "r").read()

setup(
    name='mathew',
    version='0.0.4',
    description='My personal math lib',
    url='https://github.com/larsvommars/mathew',
    author='LarsVomMars',
    author_email='dev@kroenner.eu',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['mathew'],
    zip_save=False
)
