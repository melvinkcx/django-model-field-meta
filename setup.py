import os

import setuptools


def get_version():
    package_init = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'model_field_meta', '__init__.py')
    with open(package_init) as f:
        for line in f:
            if line.startswith('__version__ ='):
                return line.split('=')[1].strip().strip('"\'')


def get_long_description():
    with open("README.md", "r") as fh:
        return fh.read()


setuptools.setup(
    name="django-model-field-meta",
    version=get_version(),
    author="Melvin Koh",
    author_email="melvinkcx@gmail.com",
    description="Django model field metadata and utilities",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/melvinkcx/django-model-field-meta",
    packages=setuptools.find_packages(exclude=["tests.*"]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
    ],
    python_requires='>=3.0',
)
