from setuptools import setup

try:
    readme = open('README.md').read()
except:
    readme = u"Django Example Projects"

from example import __version__ as version

setup(
    name="example",
    version=version,
    url='https://github.com/DLRSP/example',
    license='MIT',
    description="Django Example",
    author='Davide La Rosa',
    author_email='dlrsp.py@gmail.com',
    packages=['example', ],
    long_description=readme,
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-jenkins',
                      'django<2.3',
                      'django-errors',
                      'django-sp'
                      ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

