from setuptools import setup
from example import __version__ as version

with open('requirements.txt') as fd:
    requirements = [line.strip() for line in fd if line.strip()]

testing_requirements = [
    'codecov',
    'django_nose',
]

linting_requirements = [
    'flake8',
    'pylint',
    'bandit<1.7',
]

with open('README.md') as fd:
    long_description = fd.read()

if 'a' in version:
    dev_status = '3 - Alpha'
elif 'b' in version:
    dev_status = '4 - Beta'
else:
    dev_status = '5 - Production/Stable'

setup(
    name="example",
    version=version,
    url='https://github.com/DLRSP/example',
    license='MIT',
    description="Django Example",
    author='DLRSP',
    author_email='dlrsp.dev@gmail.com',
    packages=['example', ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    tests_require=testing_requirements,
    extras_require={
        'testing': testing_requirements,
        'linting': linting_requirements,
    },
    classifiers=[
        f'Development Status :: {dev_status}',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
