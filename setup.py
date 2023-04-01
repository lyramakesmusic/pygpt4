from setuptools import setup, find_packages

setup(
    name="gpt4",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=0.27.0",
    ],
)
