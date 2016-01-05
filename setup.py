from setuptools import setup

readme = open('README.md').read()

from example import __version__ as version

setup(
    name="example",
    version=version,
    url='https://github.com/DLRSP/example',
    license='MIT',
    description="Django example Projects",
    author='Davide La Rosa',
    author_email='davide.larosa.coins@gmail.com',
    packages=['example', ],
    long_description=readme,
    include_package_data=True,
    zip_safe=False,
    dependency_links=['https://github.com/DLRSP/django-errors'],
    install_requires=['django_nose',
					  'django==1.8.7',
					  'django-errors',
					  ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: BTC ',
    ]
)
