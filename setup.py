from setuptools import find_packages
from setuptools import setup

setup(
    name="event-service",
    version="0.0.1",
    url="https://gitlab.agilesof.com/brandi-dev/brandi-event-service",
    description="The API responsible for managing RASP candidate events",
    packages=find_packages(),
    install_requires=['flask', 'marshmallow']
)