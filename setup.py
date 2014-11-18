import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='pdf-autoprint',
    version='0.1.0',
    description='Add auto printing javascript to PDFs',
    long_description=(read('README.md')),
    url='http://github.com/millerhare/pdf-autoprint',
    license='MIT',
    py_modules=['pdf-autoprint'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['PyPDF2'],
    scripts=['pdf-autoprint.py'],
)
