from setuptools import setup

setup(
    name="pocketbook",
    version="1.0",
    description="Web application for storing thoughts and ideas",
    author="mewteebee",
    url="https://github.com/mewteebee/flask-blog-app",
    packages="pocketbook",
    install_requires=["flask","pymongo","dotenv"]

)