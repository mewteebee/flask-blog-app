from setuptools import setup

setup(
    name="pocketbook",
    version="1.0",
    description="Web application for storing thoughts and ideas",
    author="mewteebee",
    url="https://pocketbook.azurewebsites.net/",
    install_requires=["flask","pymongo","dotenv"]

)