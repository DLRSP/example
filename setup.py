from setuptools import setup

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements("requirements/py38-django32.txt", session="hack")

try:
    requirements = [str(ir.req) for ir in install_reqs]
except Exception:
    requirements = [str(ir.requirement) for ir in install_reqs]

setup(install_requires=requirements)
